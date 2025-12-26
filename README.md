# Gitbook2Pdf

A Python tool to convert GitBook websites into a single PDF file.

## Features

- **Solves Image Display Issues**: Handles relative image paths correctly, even in sub-chapters, ensuring all images render properly in the final PDF.
- **Modern GitBook Support**: Updated to work with the latest GitBook layouts (Next.js based) as well as legacy versions.
- **Full Content Generation**: Crawls and generates a complete PDF including all chapters found in the table of contents.

## How it works

1.  **Crawling**: The script starts from the provided GitBook URL and extracts the Table of Contents.
2.  **Scraping**: It iterates through each chapter link, fetching the content.
3.  **Image Fixing**: It dynamically fixes relative image URLs within each chapter to ensure they point to the correct absolute location.
4.  **PDF Generation**: It uses `WeasyPrint` to compile the collected HTML content into a PDF document.

## Installation

1.  Clone the repository.
2.  Install the dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: You may need to install system dependencies for `WeasyPrint` (e.g., `libpango1.0-dev`, `libcairo2-dev`) depending on your OS.*

## Usage

### With Python

Run the script providing the GitBook URL and the desired output filename:

```bash
python3 gitbook.py <url> <filename.pdf>
```

**Example:**

```bash
python3 gitbook.py https://borosan.gitbook.io/lpic1-exam-guide lpic1-guide.pdf
```

### With Docker

You can also run it using Docker to avoid installing local dependencies:

```bash
docker run -it -v `pwd`/output:/app/output zhangwenjie/gitbook2pdf <your url> <filename.pdf>
```

## Credits & AI Contribution

This repository is maintained with the help of AI.
Significant modifications and modernizations (including Python 3.12 support and new GitBook layout compatibility) were performed with the help of **Jules (Gemini 3 Pro)**.

## Original Project

Based on [gitbook2pdf](https://github.com/fuergaosi233/gitbook2pdf).
