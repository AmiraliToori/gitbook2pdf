'''
Author: robert zhang <robertzhangwenjie@gmail.com>
Date: 2022-11-12 12:05:59
LastEditTime: 2022-11-13 09:55:57
LastEditors: robert zhang
Description: 
'''
import html
import requests
import asyncio
import aiohttp
import weasyprint
import datetime
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from lxml import etree as ET
import sys
import os
import logging

# Configure logging for WeasyPrint
logger = logging.getLogger('weasyprint')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

BASE_DIR = os.path.dirname(__file__)

async def request(url, headers, timeout=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, timeout=timeout) as resp:
            return await resp.text()


def local_ua_stylesheets(self):
    return [weasyprint.CSS(os.path.join(BASE_DIR, './libs/html5_ua.css'))]


# weasyprint's monkey patch for level

def load_gitbook_css():
    with open(
        os.path.join(BASE_DIR, './libs/gitbook.css'), 'r'
    ) as f:
        return f.read()


def get_level_class(num):
    '''
    return 'level'+num
    '''
    return 'level' + str(num)


class HtmlGenerator():
    def __init__(self, base_url):
        self.html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">      
"""

        self.title_ele = ""
        self.meta_list = []
        self.body = ""
        self.html_end = """
</body>
</html>
"""
        self.base_url = base_url

    def add_meta_data(self, key, value):
        meta_string = "<meta name={key} content={value}>".format_map({
            'key': key,
            'value': value
        })
        self.meta_list.append(meta_string)

    def add_body(self, body):
        self.body = body

    def srcrepl(self, match):
        "Return the file contents with paths replaced"
        absolutePath = self.base_url
        pathStr = match.group(3)
        if pathStr.startswith(".."):
            pathStr = pathStr[3:]
        return "<" + match.group(1) + match.group(2) + "=" + "\"" + urljoin(absolutePath, pathStr) + "\"" + match.group(
            4)  + ">"

    def relative_to_absolute_path(self, origin_text):
        p = re.compile(r"<(.*?)(src|href)=\"(?!http)(.*?)\"(.*?)>")
        updated_text = p.sub(self.srcrepl, origin_text)
        return updated_text

    def output(self):
        full_html = self.html_start + self.title_ele + "".join(self.meta_list) \
                    + "<body>" + self.body + self.html_end
        return self.relative_to_absolute_path(full_html)


class ChapterParser():
    '''
    description: 解析子章节，也就是class为chapter的html内容
    param {*} self
    param {*} original 原始的text
    param {*} index_title 标题
    param {*} baselevel 章节对应的级别，例如1.1 或1.1.1这种
    return {*}
    '''    
    def __init__(self, base_url,original,index_title, baselevel=0):
        self.heads = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6}
        self.original = original
        self.baselevel = baselevel
        self.index_title = index_title
        self.base_url = base_url

    def parser(self):
        tree = ET.HTML(self.original)
        context = None
        # Try finding the main content
        main_content = tree.xpath('//main')
        if main_content:
            context = main_content[0]
        else:
            # Fallback for old structure
            if tree.xpath('//section[@class="normal markdown-section"]'):
                context = tree.xpath('//section[@class="normal markdown-section"]')[0]
            elif tree.xpath('//section[@class="normal"]'):
                context = tree.xpath('//section[@class="normal"]')[0]

        if context is None:
            return ""

        if context.find('footer'):
            context.remove(context.find('footer'))

        # Add markdown-section class for gitbook.css compatibility
        existing_class = context.get('class', '')
        if 'markdown-section' not in existing_class:
            context.set('class', existing_class + ' markdown-section')

        # 解析
        context = self.parse_img(context)
        # 解析head
        context = self.parsehead(context)
        # 返回html格式的内容
        return html.unescape(ET.tostring(context,encoding='utf-8').decode())

    def parse_img(self,context):
        el_imgs = context.xpath('//img')
        for el_img in el_imgs:
            old_src = el_img.get('src')
            if old_src:
                new_src = urljoin(self.base_url,old_src)
                el_img.set('src',new_src)
        return context

    def parsehead(self, context):
        def level(num):
            return 'level' + str(num)
        for head in self.heads:
            if context.xpath(head):
                context.xpath(head)[0].attrib['class'] = level(self.baselevel)
                break
        return context


class IndexParser():
    def __init__(self, elements, start_url):
        self.elements = elements
        self.start_url = start_url

    @classmethod
    def titleparse(cls, element):
        '''
        description: Extract text from element
        '''        
        return "".join(element.itertext()).strip()

    def parse(self):
        '''
        description: 返回一个list，list中的元素为一个字典
        return {list[{
                    'url': ,
                    'level': ,
                    'title': 
                }]}
        '''        
        found_urls = []
        content_urls = []

        for element in self.elements:
            # Check if it's an 'a' tag (new structure) or 'li' (old structure)
            if element.tag == 'a':
                href = element.get('href')
                title = self.titleparse(element)
                if href:
                    url = urljoin(self.start_url, href)
                    if url not in found_urls:
                        content_urls.append({
                            'url': url,
                            'level': 1, # Flat structure assumption
                            'title': title
                        })
                        found_urls.append(url)
            else:
                # Old logic for 'li'
                li = element
                element_class = li.attrib.get('class')
                if not element_class:
                    continue
                # 解析章节中的title和level
                if 'header' in element_class:
                    title = self.titleparse(li)
                    data_level = li.attrib.get('data-level')
                    level = len(data_level.split('.')) if data_level else 1
                    content_urls.append({
                        'url': "",
                        'level': level,
                        'title': title
                    })
                elif "chapter" in element_class:
                    data_level = li.attrib.get('data-level')
                    level = len(data_level.split('.'))
                    if 'data-path' in li.attrib:
                        data_path = li.attrib.get('data-path')
                        # url 为子章节的访问地址
                        url = urljoin(self.start_url, data_path)
                        # 解析子章节中的title
                        title = self.titleparse(li)
                        # 将url、level、title 放入content_urls中
                        if url not in found_urls:
                            content_urls.append(
                                {
                                    'url': url,
                                    'level': level,
                                    'title': title
                                }
                            )
                            found_urls.append(url)

                    # Unclickable link
                    else:
                        title = self.titleparse(li)
                        content_urls.append({
                            'url': "",
                            'level': level,
                            'title': title
                        })
        return content_urls


class Gitbook2PDF():
    def __init__(self, base_url, fname=None):
        self.fname = fname
        self.base_url = base_url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
        }
        self.content_list = []
        self.meta_list = []
        self.meta_list.append(
            ('generator', 'gitbook2pdf')
        )
        # weasyprint.HTML._ua_stylesheets = local_ua_stylesheets

    def run(self):
        content_urls = self.collect_urls_and_metadata(self.base_url)
        # 初始化一个长度为len(content_urls)的list，使用""填充长度
        self.content_list = ["" for _ in range(len(content_urls))]
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.crawl_main_content(content_urls))
        loop.close()

        # main body
        body = "".join(self.content_list)
        # 使用HtmlGenerator类来生成HTML
        html_g = HtmlGenerator(self.base_url)
        html_g.add_body(body)
        for key, value in self.meta_list:
            html_g.add_meta_data(key, value)
        html_text = html_g.output()
        css_text = load_gitbook_css()

        self.write_pdf(self.fname, html_text, css_text)

    async def crawl_main_content(self, content_urls):
        tasks = []
        for index, urlobj in enumerate(content_urls):
            # 当urljob中的url不为空时，则表示为子章节，则开始爬取内容
            if urlobj['url']:
                tasks.append(self.gettext(index, urlobj['url'], urlobj['level'],urlobj['title']))
            else:
                tasks.append(self.getext_fake(index, urlobj['title'], urlobj['level']))
        if tasks:
            await asyncio.gather(*tasks)
        print("crawl : all done!")

    async def getext_fake(self, index, title, level):
        await asyncio.sleep(0.01)
        class_ = get_level_class(level)
        string = f"<h1 class='{class_}'>{title}</h1>"
        self.content_list[index] = string

    async def gettext(self, index, url, level, title):
        '''
        description: 爬取url中的内容
        return path's html
        '''

        print("crawling : ", url)
        try:
            metatext = await request(url, self.headers, timeout=10)
        except Exception as e:
            print("retrying : ", url)
            try:
                metatext = await request(url, self.headers)
            except Exception as e:
                print(f"failed to fetch {url}: {e}")
                return

        try:
            text = ChapterParser(url,metatext, title, level ).parser()
            print("done : ", url)
            self.content_list[index] = text
        except IndexError:
            print('faild at : ', url, ' maybe content is empty?')
        except Exception as e:
             print(f"failed to parse {url}: {e}")

    def write_pdf(self, fname, html_text, css_text):
        tmphtml = weasyprint.HTML(string=html_text)
        tmpcss = weasyprint.CSS(string=css_text)
        if not os.path.exists("./output/"):
            os.makedirs("./output/")
        fname = "./output/" + fname
        htmlname = fname.replace('.pdf', '.html')
        with open(htmlname, 'w', encoding='utf-8') as f:
            f.write(html_text)
        print('Generating pdf,please wait patiently')
        tmphtml.write_pdf(fname, stylesheets=[tmpcss])
        print('Generated')

    def collect_urls_and_metadata(self, start_url):
        '''
        description: 获取页面中所有的章节url
        return {list[{
            url,
            level,
            title
        }]}
        '''
        response = requests.get(start_url, headers=self.headers)
        self.base_url = response.url
        start_url = response.url
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')

        # If the output file name is not provided, grab the html title as the file name.
        if not self.fname:
            title_ele = soup.find('title')
            if title_ele:
                title = title_ele.text
                if '·' in title:
                    title = title.split('·')[1]
                if '|' in title:
                    title = title.split('|')[1]
                title = title.replace(' ', '').replace('/', '-')
                self.fname = title + '.pdf'
        self.meta_list.append(
            ('title', self.fname.replace('.pdf', ''))
        )

        # get description meta data
        comments_section = soup.find_all(class_='comments-section')
        if comments_section:
            description = comments_section[0].text.replace('\n', '').replace('\t', '')
            self.meta_list.append(
                ('description', description)
            )

        # get author meta
        author_meta = soup.find('meta', {'name': 'author'})
        if author_meta:
            author = author_meta.attrs['content']
        else:
            author = urlparse(self.base_url).netloc
        self.meta_list.append(
            ('author', author)
        )

        # creation date and modification date : default now
        # see : https://www.w3.org/TR/NOTE-datetime
        now = datetime.datetime.utcnow().replace(microsecond=0).isoformat()
        self.meta_list.append(('dcterms.created', now))
        self.meta_list.append(('dcterms.modified', now))

        tree = ET.HTML(text)

        # Try new structure
        aside = tree.xpath("//aside[@data-testid='table-of-contents']")
        if aside:
            links = aside[0].xpath(".//a")
            return IndexParser(links, start_url).parse()
        else:
            # Try old structure
            lis = tree.xpath("//ul[@class='summary']//li")
            return IndexParser(lis, start_url).parse()
