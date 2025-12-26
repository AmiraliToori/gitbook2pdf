Copy

# Introduction

Welcome to LPIC1 Certification Exam guide. This a door to the new world, wold of files and processes. Living in this new world needs new attitudes and new skills. So be patient and first lets know how to stay alive.

You can see the overview of LPIC1 Certification [here](http://www.lpi.org/our-certifications/lpic-1-overview) and as you probably know LPIC1 is consist of two exams [101](http://www.lpi.org/our-certifications/exam-101-objectives) and [102](http://www.lpi.org/our-certifications/exam-102-objectives). Both courses are all about linux itself. We will talk about some key concepts and related commands and tools. While you are getting familiar with Linux Administrators toolbox, you are prepared for next level of LPI exam.

By Payam Borosan

* Site: [www.linuxcert.ir](http://linuxcert.ir/)
* GitBook: <https://borosan.gitbook.io/lpic1-exam-guide/>
* e-mail: p.borosan [at] gmail.com

Donation :

* coffeete (from IR): <https://www.coffeete.ir/borosan>
* bitcoin: bc1qhm5nr98su6xupv4dd6zt2m0sq2dzxh69zejm85
* ethereum: 0x6F3D43A6957CC61b74Fe85Ad52D05d91a2B13c67
* litecoin: ltc1qvxu57q2f3ay9tzu6tffkayc65te80vax9wzxn7

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-MGEHxLeLBbPQyuwZpRs%252F-MGENbJCZtipYYHI3DfY%252Flpic1-101%2526102.jpg%3Falt%3Dmedia%26token%3D844e33d2-f35e-43d3-b453-54df4c49beb6&width=768&dpr=4&quality=100&sign=e8e5b5b7&sv=2)

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-MgeUWLZy29lqV7xYkNN%252F-MgeUgl7hVfh20242FH2%252FCC-BY-NC-icon-88x31.png%3Falt%3Dmedia%26token%3D5086e294-277e-4b4b-8761-f0db180d0c5d&width=768&dpr=4&quality=100&sign=85c6408f&sv=2)

Copy

# 101.1. Determine and configure hardware settings

## **101.1 Determine and configure hardware settings**

\*\*Weight:\*\*2

\*\*Description: \*\*Candidates should be able to determine and configure fundamental system hardware.

**Key Knowledge Areas:**

* Tools and utilities to list various hardware information (e.g. lsusb, lspci, etc.)
* Tools and utilities to manipulate USB devices
* Conceptual understanding of sysfs, udev, dbus

**The following is a partial list of the used files, terms and utilities:**

* /sys/
* /proc/
* /dev/
* modprobe
* lsmod
* lspci
* lsusb

Linux treat every thing as a file. It includes programs , hardware and even processes which are running. These files are organized in directories and standardize for easier access and administration. Lets see how linux dealing with devices:

### /proc

The /proc is a virtual dicretory which contains a illusionary filesystem called procfs. It does not exist on a disk. Instead, the kernel creates it in memory. It is used to provide information about the system (originally about processes).

Some of the more important files and directories are :

**/proc/1:** A directory with information about process number 1. Each process has a directory below /proc with the name being its process identification number.

\*\*/proc/cpuinfo: \*\*Information about the processor, such as its type, make, model, and performance.

\*\*/proc/filesystems : \*\*Filesystems configured into the kernel.

\*\*/proc/interrupts: \*\*Shows which interrupts are in use, and how many of each there have been.

\*\*/proc/meminfo : \*\*Information about memory usage, both physical and swap.

The way /proc virtual directory organize processes get noticed by developers and they started to use /proc for both reading and writing information. So guess what, little by little /proc become a place which stored different kind of information. Processes information, current running Kernel information, hardware information, system information. Some one should do some thing to stop this messy place and that cause /sys introducing in kernel 2.5 .

### /sys

/sys it is a virtual directory with illusionary sysfs file system, which is created when system boots up and get vanished when system restarts or goes off.

sysfs introduced to specifically store system information and its components (mostly attached and installed hardware). An as it was planned for that its seems more organized and more standardize than procfs.

sysfs hasn't caused all the stuff move from /proc to /sys , they still exist in /proc but /sys gives us a better view of current data.

**Linux kernel modules** (LKMs) are pieces of code which can be loaded into the kernel much like a hot-swappable piece of hardware. they can be inserted into the kernel and activated without the system needing to be rebooted.

### udev

The kernel is the central part of operating system to address the hardware. And to make sure that the hardware is available for the kernel udev plays an important role.

udev is a replacement for the Device File System (DevFS) starting with the Linux 2.6 kernel series. udev plays role in Loading Kernel Module, Creating Device Files and making sure every thing is the order we need it to be. Lets see how it works:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_WIhgliGcuNIR3k%252Fhw-udev.jpg%3Fgeneration%3D1569999716054769%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=fac2f840&sv=2)

1. The linux kernel initiates the device loading and next sends out messages (uevents) to the udev daemon.
2. udev daemon catches the event and decide how to handle based on the attributes that it has received in the event. udev load required kernel module with necessary information using **modprobe**.

what is modprobe?

**modprobe** is an intelligent command for listing, inserting as well as removing modules from the kernel.( Will be explained )

3 . udev next reads its rules . udev allows us to ban devices based on their properties, like vendor ID and device ID, ... .

* Default rules are in /lib/udev/rules.d
* Custom rules are in /etc/udev/rules.d

Lets see it in action, we use and then attach a usb storage:

udev write device information to the /sys virtual directory. Also udev works as an Hardware Abstaraction Layer(HAL) and creates device file entries under /dev directory in a structured way.

What is HAL? In computers, a **hardware abstraction layer** (**HAL**) is a **layer** of programming that allows a computer OS to interact with a **hardware** device at a general or **abstract level** rather than at a detailed **hardware level**.

another example:

We have seen this information previously. Try `udevadm info --attribute-walk --name=/dev/sda` for your self. These device attributes can be used in udev rules.

### /dev

This directory contains the **device files** for every hardware device attached to the system.

> **Device files** are employed to provide the operating system and users an interface to the devices that they represent.

/dev exits from early beginning versions of linux and it was populated by devfs. (As we mentioned) devfs was a an **obsolete and no longer available.**

These days, it has been replaced by udev, a daemon that manages the contents of /dev in a temporary filesystem, \*\*(\*\*or by devtmpfs, which is a lightweight replacement for devfs that is used in some minimal systems).

Actually they are files and pointers to the under laying device hardware. Try`ls -l` to see that .

There are some common device names in .in linux World :

with the special thanks of udev (as a Hardware Abstraction Layer) and the names it provides.

#### /sys vs /dev

* The /sys filesystem (sysfs) contains files that provide information about devices: whether it's powered on, the vendor name and model, what bus the device is plugged into, etc. It's of interest to applications that manage devices.
* The /dev filesystem contains files that allow programs to access the devices themselves: write data to a serial port, read a hard disk, etc. It's of interest to applications that access devices.

A metaphor is that /sys provides access to the packaging, while /dev provides access to the content of the box.

The reason for /dev existing independently of /sys is partly historical: /dev dates back to the dawn of Unix, while /sys is a much more recent invention. If Linux was designed today with no historical background, /dev/sda might be /sys/block/sda/content.

**pesudo File Systems**

'Pseudo-' means false, pretend. So "pseudo-filesystem" means a filesystem that doesn't have actual files – rather, it has virtual entries that the filesystem itself makes up on the spot.

/dev, /proc and /sys are virtual "pseudo-filesystems" (not existing on harddisk, but only in RAM – so they do not consume any harddisk space and are completely created on boot).

### dbus

D-Bus is a message bus system, a simple way for applications to talk to one another. Beside all of dbus benefits it can read information form /dev folder and relate them with user desktop programs using signals. In fact dbus make a kind of middle layer which keeps programs a way from difficulties of dealing with /dev and /sys directories.

\*\*Notice : \*\*udev and dbus can work in all distributions because sysfs has made required information standardize.

From the administrative perspective there are some ls utilities ( lsusb, lspci , ... ) to show more information about the hardware which has been attached to our system. Lets take a quick look at them:

### lsusb

The lsusb command allows you to display information about USB buses and devices that are attached to them.

lsusb has some options:

We can also use the `-v` command-line option to display more verbose output:

`-t` tells lsusb to dump the physical USB device hierarchy as a tree. This overrides the v option.

`-V`or `--version` Print version information on standard output, then exit successfully.

try `usb-devices` , it will give us more detailed info.

### lscpu

lscpu reports information about the cpu and processing units. It does not have any further options or functionality.

### lshw

lshw is a general purpose utility, that reports detailed and brief information about multiple different hardware units such as cpu, memory, disk, usb controllers, network adapters etc. Lshw extracts the information from different /proc files.

Do remember that the lshw command executed by root (superuser):

Lets try lshw -short :

### lspci

lspci is a utility for displaying information about PCI buses in the system and devices connected to them.By default, it shows a brief list of devices.

All of lspci switches:

The `-t` option will display the output in tree format with information about bus, and how devices are connected to those buses. The output will be only using the numerical ids:

lspci has a very helpful switch to know the name of the kernel module that will be handling the operations of a particular device. (this option will work only on Kernel 2.6 version and above):

lets try a tool in order to see whether these modules have been loaded.

### lsmod

lsmod is a very simple program with no options.

it nicely formats the contents of the file /proc/modules, which contains information about the status of all currently-loaded Linux Kernel Modules (LKMs).

try `cat /proc/modules` and compare the results.

There is nothing like Drivers in linux and as we said, udev is responsible for calling related module with required information using modprobe.

### modprobe

modprobe intelligently adds or removes a module from the Linux kernel. For demonstration lets remove and add e1000 module which is for Ethernet car on my system:

and we would get disconnected and then connected again. modprobe has a long list of options try`modprobe --help` to see them.

.

.

.

Sources:

<https://www.tldp.org/HOWTO/SCSI-2.4-HOWTO/procfs.html>

<https://medium.com/@jain.sm/pseudo-file-systems-in-linux-5bf67eb6e450>

<https://stackoverflow.com/questions/16431554/how-devfs-and-dev-file-system-differ>

<https://www.tecmint.com/load-and-unload-kernel-modules-in-linux/>

<http://dwaves.de/2017/05/29/linux-difference-between-proc-sys-and-dev-sysfs/>

<https://www.linuxtopia.org/online_books/introduction_to_linux/linux_The_most_common_devices.html>

<https://unix.stackexchange.com/questions/176215/difference-between-dev-and-sys>

<https://wiki.debian.org/udev>

<https://opensource.com/article/16/11/managing-devices-linux>

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s2-sysinfo-hardware-lsusb>

<https://www.systutorials.com/docs/linux/man/8-lspci/>

<https://www.computerhope.com/unix/lsmod.htm>

<https://www.binarytides.com/linux-commands-hardware-info/>

<https://linux.die.net/man/8/modprobe>

Copy

# 101.2. Boot the system

### 101.2.Boot the system

**Weight:**3

**Description:** Candidates should be able to guide the system through the booting process.

**Key Knowledge Areas:**

* Provide common commands to the boot loader and options to the kernel at boot time
* Demonstrate knowledge of the boot sequence from BIOS to boot completion
* Understanding of SysVinit and systemd
* Awareness of Upstart
* Check boot events in the log files

**Terms and Utilities:**

* dmesg
* BIOS
* bootloader
* kernel
* initramfs
* init
* SysVinit
* systemd

Have you ever think what happens when you press power button on a pc or laptop? There is no jinni or ghost who starts dead metal heart and brings operating system up and running. Lets see how does is happen?

## Boot procedure

Lets draw a big picture to have an overview of generic boot procedure from BIOS to the shell

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_SVuG8i8YR6hZws%252Fboot-bootseq.jpg%3Fgeneration%3D1569999709104103%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=5751c8af&sv=2)

Now lets explain more each of these steps:

**1-**First system power on.

**2-**BIOS load (in modern systems it would be UEFI)

## BIOS

BIOS, which stands for Basic Input Output System, is software stored on a small memory chip on the motherboard. BIOS is responsible for POST. POST short for Power On Self Test, is the initial set of diagnostic tests performed by the computer right after it's powered on, with the intent to check for any hardware related issues.So BIOS makes POST the very first software to run when a computer is started.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_SXW5Mm1eEf0mKP%252Fboot-bios.jpg%3Fgeneration%3D1569999709444104%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=1392bb68&sv=2)

**3-**BIOS scans and goes for the primary (or chosen) disk's "boot sector" .A boot sector is a region of a hard disk, floppy disk, optical disc, or other data storage device that contains machine code to be loaded into random-access memory (RAM) by a computer system's built-in firmware like BIOS.

What exist on boot sector? MBR

## MBR

A master boot record (often shortened as MBR) is a kind of boot sector stored on a hard disk drive or other storage device that contains the necessary computer code to start the boot process.

The master boot record is located on the first sector of a disk. The specific address on the disk is Cylinder: 0, Head: 0, Sector: 1 and it is 512 bytes.

What Master Boot Record includes and how it continues the boot sequence?

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LxRKBg3iGBU2sCLSKp8%252F-LxRLkheYh_ZOywgRTUD%252Fboot-MBR.JPG%3Falt%3Dmedia%26token%3Daf0270fa-f3b4-49fd-b8e2-3eb6851d0ab6&width=768&dpr=4&quality=100&sign=5adcdc08&sv=2)

The master boot record itself holds two things : the boot loader program(or some of it) and the partition table

When the BIOS loads, it looks for data stored in the first sector of the hard drive, the MBR; using the data stored in the MBR, the BIOS activates the boot loader.

Whats magic Number? Located in the final two bytes of the **MBR** (511-512), this section must contain the hex value AA55, which officially classifies this as a valid **MBR**. An invalid **magic number** indicates a corrupt or missing **MBR**, therefore these bytes are critical to booting or using the disk.

**4-**Boot Loader is executed.

### Boot Loader

Most simply, a boot loader loads the operating system. Most boot loaders load in two stages.

**A-** In the first stage of the boot, the BIOS loads a part of the boot loader known as the **initial program loader**, or **IPL**. The **IPL** **interrogates the partition table and subsequently is able to load data wherever it may exist on the various media.** This action is used initially to locate the second stage boot loader, which holds the remainder of the loader.

**B-**The second stage boot loader is the real meat of the boot loader; many consider it the only real part of the boot loader. This contains the more **disk-intensive parts** of the loader, such as [bootloader] user interfaces and kernel loaders. (These user interfaces can range from a simple command line to the modern GUIs.)

**5-**Lilo / Grub / Grub2 begins.

There have been different boot loaders . Lilo, Grub and Grub2:

## Lilo

LILO (Linux Loader) is a boot loader for Linux and was the default boot loader for most Linux distributions in the years after the popularity of loadlin. Today, many distributions use GRUB as the default boot loader, but LILO and its variant ELILO are still in wide use. Further development of LILO was discontinued in December 2015 along with a request by Joachim Wiedorn for potential developers.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_Safh6DkJwD_BQV%252Fboot-lilo.jpg%3Fgeneration%3D1569999709345182%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=d4ee7d15&sv=2)

The configuration file of lilo is located at “/etc/lilo.conf”. Lilo reads this configuration file and it tells Lilo where it should place the bootloader. The sample configuration file is specified below:

lilo as a command has some options which might be help full:

## Grub

GRUB (GRand Unified Bootloader) is a boot loader package developed to support multiple operating systems and allow the user to select among them during boot-up. It has been developed under the GNU project GNU GRUB.

## Grub2

GRUB 2 has now replaced the GRUB. And the name GRUB was renamed to GRUB Legacy and is not actively developed, however, it can be used for booting older systems since bug fixes are still on going.

On the surface the majority of users won't notice any difference but the new version has fairly major structural changes and should be more reliable. Also the new version stores its configuration files differently

GRUB 2's major improvements over the original GRUB include:

* Supports multiboot
* Supports multiple hardware architectures and operating systems such as Linux and Windows
* Offers a Bash-like interactive command line interface for users to run GRUB commands as well interact with configuration files
* Enables access to GRUB editor
* Supports setting of passwords with encryption for security
* Supports booting from a network combined with several other minor features

Regardless of the GRUB version, a boot loader allows the user to:

1. modify the way the system behaves by specifying different kernels to use,
2. choose between alternate operating systems to boot, and
3. add or edit configuration lines to change boot options, among other things.

## Kernel boot-time Options

Kernel command line parameters are parameters that we pass on the system during the boot process. They are also known as "boot options".

We **must be at console** to pass kernel boot time command because when the system is booting up there is no Networking service. So reboot the system and Press Esc key during boot:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_ScHD9kKVTwFEUR%252Fboot-grubmenu.jpg%3Fgeneration%3D1569999709245016%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=f192bb99&sv=2)

Depending on the configuration the user may be able to choose from a menu of potential boot types or kernel versions or simple allow the default to proceed.Lets press 'e' to see some kernel parameters:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_SerrKjnBjuTNSr%252Fboot-grubmenu2.jpg%3Fgeneration%3D1569999709211936%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=ff8b7bb2&sv=2)

The Linux Kernel boot parameters are passed into a list of strings separated with white spaces:

Where ‘**name=unique keyword**‘ it **defines the part of kernel** where the value is to be associated. (max 10)

`'linux'`defines the place of executable kernel (vmlinuz/vmlinux) to run ,and obviously kernel boot options come after it.

There are many parameters that help us configure and determine all aspects of our system's operation during the boot process. Some of them are:

One of famous Kernel boot options is pasword recovery using `single` kernel parameter option. The `single` parameter guides ‘init‘ to the start computer in single user mode and disable starting all the daemons.

`/proc/cmdline` This file shows the parameters passed to the kernel at the time it is started:

**6-** Linux Kernel is read an executed.

As soon as the Linux kernel has been booted and the root file system (/) mounted, programs can be run and further kernel modules can be integrated to provide additional functions.

To mount the root file system, certain conditions must be met. The kernel needs the corresponding drivers to access the device on which the root file system is located (especially SCSI drivers). The kernel must also contain the code needed to read the file system (ext2, reiserfs, romfs, etc.). It is also conceivable that the root file system is already encrypted. In this case, a password is needed to mount the file system.

The initial ramdisk (also called initdisk or initrd) solves precisely the problems described above.

## initramfs

The Linux kernel provides an option of having a small file system loaded to a RAM disk and running programs there before the actual root file system is mounted.

The initrd contains a minimal set of directories and executables to achieve this, such as the `insmod` tool to install kernel modules into the kernel.

Its lifetime is short, only serving as a bridge to the real root file system.

**7-** The 'init' program loads and become the first process ID.

### What is init?

In Linux, init is a abbreviation for Initialization. The init is a daemon process which starts as soon as the computer starts and continue running till, it is shutdown. In-fact init is the first process that starts when a computer boots, making it the parent of all other running processes directly or indirectly and hence typically it is assigned “pid=1“.
'init' on previous linux distributions was a process with a name /sbin/int . Today 'init' is not 'init' any more, it can be any thing.

## init program solutions

In linux world we have three different types of init programs that lunch various daemons, applications and programs.

* SysV
* upstart
* Systemd

so /sbin/init can be linked to upstart or systemd.

**Sysv**

SysV is a much older system to manage service startup during the boot process in a Linux system. SysVinit has been around since basically forever.Traditionaly in SystemV, /sbin/init procedure was used to start services.

The way SysVinit does this is by setting a strict order for services to start in. Every service is assigned a priority number and init starts the services in sequence by priority.

The order in which this happens is essential, serial loading is required for dependencies, but some times parallel loading can be used to increase speed. The problem with SysVinit is that it takes careful tuning, both upstart and Systemd have been developed to make loading system configurations much more efficient.

**Upstart**

In an attempt to bring more features to the Linux initialization process, Canonical released Ubuntu 6.10 (Edgy Eft) in 2006 with Upstart. Upstart was designed with backward compatibility from the start. It could run daemons without any modification to the startup scripts. Because of this, many Linux distributions moved toward Upstart, but not all of them.

Upstart is an event-based replacement, it receives events and then runs jobs based on these events.

The problem with upstart is that it is using shell scripts and many features that existed in init already. So although it is backward compatible but it suffers from relaying on messy codes.

> if our system has /etc/init Directory, it is using upstart.

**Systemd**

A systemd, may refer to all the packages, utilities and libraries around daemon.The goal of systemd project is to provide an operating system that runs on top of the linux kernel and taking control of almost every thing after kernel loading. Consequently it has been developed to overcome the shortcomings of init.

Systemd is designed to start processes in parallel, thus reducing the boot time and computational overhead. It has a lot other features as compared to init.

Systemd is rapidly taking over the way how linux systems are starting services and it is the current standard on all major linux distributions(even Ubuntu ). Systemd is not backward compatible how ever there are so mane scripts which convert sysv command into systemd command and lets you feel comfortable.

> if our system has a directory /usr/lib/systemd , we are on systemd

**8-** Sysv or upstart or systemd (what ever your system service manager is) starts every thing. Prerequisites, services, ... and shell. and one the shell is present the user can log in.

## dmesg

dmesg command is used to **display the kernel related messages** on Unix like systems. dmesg stands for “display message or display driver“. dmesg command retrieve its data by reading the kernel ring buffer.

The kernel ring buffer is a data structure that records messages related to the operation of the kernel. A ring buffer is a special kind of buffer that is always a constant size, removing the oldest messages when new messages come in.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_SgWKMNCL0d4-o6%252Fboot-dmesgkrb.png%3Fgeneration%3D1569999709114181%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=3a188889&sv=2)

dmesg can be very useful when troubleshooting or just trying to obtain information about the hardware on a system. Its basic syntax is dmesg [options].

Using dmesg without any of its options causes it to write all the kernel messages to standard output.

we can clear dmesg logs if required with `dmesg -c` command.

**/var/log/dmesg**

The `dmesg` command shows the current content of the kernel syslog ring buffer messages while the `/var/log/dmesg` file contains what was in that ring buffer when the boot process last completed. try `cat /var/log/dmesg`.

.

.

.

Sources:

<https://www.lifewire.com>

<https://www.tecmint.com/linux-boot-process/> & <https://www.tecmint.com/best-linux-boot-loaders/>

<https://whatis.techtarget.com/definition/boot-sector> & <https://whatis.techtarget.com/definition/Master-Boot-Record-MBR>

<https://www.ibm.com/developerworks/library/l-bootload/index.html>

<https://www.interserver.net/tips/kb/what-is-lilo/>

<https://www.linuxjournal.com/article/1166>

<https://www.oreilly.com/library/view/linux-in-a/0596000251/ch04s02.html>

<https://www.cyberciti.biz/tips/10-boot-time-parameters-you-should-know-about-the-linux-kernel.html>

<https://unix.stackexchange.com/questions/89923/how-does-linux-load-the-initrd-image>

<https://developer.ibm.com/articles/l-initrd/><https://www.ibm.com/developerworks/community/blogs/mhhaque/entry/anatomy_of_the_initrd_and_vmlinuz?lang=en>

<http://www.linuxfromscratch.org/blfs/view/svn/postlfs/initramfs.html>

<https://help.ubuntu.com/community/Grub2>

<https://www.tecmint.com/systemd-replaces-init-in-linux/>

<https://fossbytes.com/systemd-vs-sys-v-vs-upstart/>

<https://unix.stackexchange.com/questions/196166/how-to-find-out-if-a-system-uses-sysv-upstart-or-systemd-initsystem>

<https://www.tecmint.com/dmesg-commands/>

<https://www.linuxtechi.com/10-tips-dmesg-command-linux-geeks/>

<https://www.quora.com/What-is-a-ring-buffer-in-Linux>

<https://unix.stackexchange.com/questions/191560/difference-between-output-of-dmesg-and-content-of-var-log-dmesg>

Copy

# 101.3. Change runlevels / boot targets and shutdown or reboot system

## **101.3 Change runlevels / boot targets and shutdown or reboot system**

**Weight:**3

**Description:** Candidates should be able to manage the SysVinit runlevel or systemd boot target of the system. This objective includes changing to single user mode, shutdown or rebooting the system. Candidates should be able to alert users before switching runlevels / boot targets and properly terminate processes. This objective also includes setting the default SysVinit runlevel or systemd boot target. It also includes awareness of Upstart as an alternative to SysVinit or systemd.

**Key Knowledge Areas:**

* Set the default runlevel or boot target
* Change between runlevels / boot targets including single user mode
* Shutdown and reboot from the command line
* Alert users before switching runlevels / boot targets or other major system events
* Properly terminate processes

**Terms and Utilities:**

* /etc/inittab
* shutdown
* init
* /etc/init.d/
* telinit
* systemd
* systemctl
* /etc/systemd/
* /usr/lib/systemd/
* wall

In previous lesson we explain the sequence of system boot in liunx, then we get introduced to Sysv, Upstart and system as different service managers in linux world. In this lesson we learn how to take control over our linux system services using these service managers.

Lets start with SysV. SysV is is nothing more than many executable scripts which are run after init process. How we can define which service should be run when computer starts ? I'm glad you asked. It seems that huge text configuration files would be needed, there is where **runlevels** come to play.

### runlevels

A runlevel is one of the modes that a Unix -based operating system will run in. Each runlevel has a certain number of services stopped or started, giving the user control over the behavior of the machine. runlevels avoid of having a few large files to edit by hand.

Conventionally, **seven** runlevels exist, numbered from zero to six. And there are some differences between Debian and RedHat based systems:

Runlevel

Debian

RedHat

**0**

**Halt**

**Halt**

**1**

**Single User Mode**

**Single User Mode**

**2**

Full,Multi-User,GUI

Multi-User, No Net

**3**

Nothing

Multi-User, with Net, No GUI

**4**

**Nothing**

**Not used**

**5**

Nothing

Full,Multi-User,GUI

**6**

**Reboot**

**Reboot**

CentsOS 5 was the last version which used SysV and from CentOS 7 Systemd is used.

### runlevel

To find the current and previous runlevels , the runlevel command is used:

In the above output, the letter ‘N’ indicates that the runlevel has not been changed since the system was booted. And, 5 is the current runlevel.

Now that we now about runlevels, How we can switch between them? well just tell 'init' what runlevel you like.

## telinit

telinit is used to change the SysV system runlevel.

Lets try it on a CentOS5 machine:

and system goes to runlevel 3 lets go back to runlevel 5:

## init

init (as a command) is a process control initialization like telinit.

#### telinit vs init

telinit is a smaller tool that informs init when it needs to switch runlevels. So we can use "telinit" to "tell init" that it needs to switch runlevel. telinit is actually linked to init command and it is possible to use init command instead but it is not recommanded.

There are several ways to change runlevels. To make a permanent change, we can edit **/etc/inittab** and change the default level that we just saw above.

### /etc/inttab

After the Linux kernel has booted, the init program reads the /etc/inittab file to determine the **behavior for each runlevel**. Unless the user specifies another value as a kernel boot parameter, the system will attempt to enter (start) the default runlevel.(CentOs5)

the **default runlevel** is determined from the`id:`entry in **/etc/inittab**. How run levels are set up by default and how they are configured depends in part on the particular distribution you are running.

The format of each line in inittab file is as follows:

`id:runlevel:action:process`

Here is a description of these fields:

* **id (identification code)** – consists of a sequence of one to four characters that identifies its function.
* **runlevels** – lists the run levels to which this entry applies.
* **action** – specific codes in this field tell init how to treat the process. Possible values include: initdefault, sysinit, boot, bootwait, wait, and respawn.
* **process** – defines the command or script to execute.

Now lets see how SysV implements the concept of run levels.

### /etc/init.d

/etc/init.d contains scripts used by the System V init tools (SysVinit).

As we said, in SysV, init program is the first process that is run and consequently some infrastructure services are started. Files in /etc/init.d are shell scripts that respond to start, stop, restart, and (when supported) reload commands to manage a particular service. But how SysV determine which services inside /etc/init.d should be started or stopped depend on default runlevel ?Lets draw a picture:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LxAKmu7HbaGiOrz2zoK%252F-LxAOKw3vyb1UajpIVSX%252Fcustomizsysv-SysVScripts.jpg%3Falt%3Dmedia%26token%3D2bf581ab-46ec-4b25-97a8-a2f5f1bf5030&width=768&dpr=4&quality=100&sign=3b985867&sv=2)

### /etc/rc.d/

SysV uses grouping. **Scripts of each runlevel are grouped and placed in /etc/rc{runlevel}.d/** where runlevel is the runlevel.

As many services might be existed in different runlevels, the real script files are hold in /etc/init.d and /etc/rc{runlevel}.d/just point to required ones.

Lets take a look at rc.5 for example:

Each script in each runlevel is run with its startup or shutdown functions depending on if that runlevel is going up or going down. **S** means **starting** script and **K** shows that it is a **killing** script .The sequence of actions is defined by the numbers. try cat command to see what is inside :

And all of these places were places that SysV uses to manage scripts and runlevels. In Sysv system we can manage services with `service`command and`chkconfig`command to define how and when services are started. We will talk about them later.

**rc.local**

But what about /etc/rc.local ? This file runs after all other init level scripts have run, so it's safe to put various commands that you want to have issued upon startup.This is also a good place to place "troubleshooting" scripts in. **But do not forget rc.local may not work properly in Upstart and Systemd.** Test it, search it and do required configuration before using in production environment.

Lets go back to our topic and get familiar with runlevels equivalent in systemd. Although /etc/inittab still exist in Systemd systems but that is not part of configuration, we have something called "Targets".

### systemd targets

Like runlevels there are some modes in systemd system that our system can run in, systemd runlevels are referred to as "**targets**". "**targets**" **are described as a collection of services**. Look at the equivalents:

In order to switch between Boot Targets we use systemctl tool.

### systemctl

Systemctl is a systemd utility which is responsible for Controlling the systemd system and service manager. It can does lots of thing but what we need here and use it for is changing boot targets.

To see the current boot target use `systemctl get-default` command:

To change the target use `systemctl isolate xxxxx.target` , for example:

To set the default target, run `systemctl set-default xxxxxx.target` command :

But how systemd knows what to do and how to do things ? We have something called "**Unit**". **The concept of "Unit Files" replaces the SysV init scripts for services.**

### systemd unit files

There are different types of unit files and the best way to describe unit files, is **'that is a thing which should be started'**.Yes that is a thing because there are different kinds of unit files. **Each unit file is a simple text file describing a unit, what it does, what needs to run before or afterward, and other details**

Unit files can be stored in a few different places on your system. systemd looks for system unit files in this order:

1. **/etc/systemd/system:**directory stores unit files that extend a service. This directory will take precedence over unit files located anywhere else in the system.
2. **/run/systemd/system:**directory is the runtime location for unit files.
3. **/usr/lib/systemd/system:**directory is the default location where unit files are installed by packages. Unit files in the default directory should not be altered.

**Unit files in the earlier directories override later ones.** Lets take a look at them:

### 1./etc/systemd/system

### 2./run/systemd/system

### 3./usr/lib/systemd/system

lets follow one of target unit files.Try `ls -al *.target` to see all of target files. As an instance *default.target*:

Lets take a look at that *graphical.target*:

And what it requires is *multi-user.target*, lets see:

and it requires *basic.target* :

Finally *sysinit.target* :

And *sysint.target* does not require any thing. It seems that we have reached top level target in our tree and we can go back.

Using unit files beside Targets concept make Systemd more flexible in comparison to SysV.

## wall

There are times when multiple users are logged in to a server computer, and we need to, say, restart the server to perform some maintenance task. Of course, the **correct way is to inform all** those who are logged in about the maintenance activity.

wall (an abbreviation of write to all) is a Unix command-line utility that displays the contents of a file or standard input to all logged-in users. It is typically used by root to send out shutting down message to all users just before poweroff.(Ubuntu16)

Lets try sending out "we are going down" message:

and what will **user1** receive:

options might not work is some old distributions.

## shutdown

shutdown - Halt, power-off or reboot the machine

shutdown does its job by signalling the init process, asking it to change the runlevel. According to previous title, runlevel 0 is used to halt the system, runlevel 6 is used to reboot the system, and runlevel 1 is used to put the system into a state where administrative tasks can be performed (single-user mode).

We may specify a time string (which is usually “now” or “hh:mm” for hour/minutes):

####

#### halt vs poweroff ! it's a bit historical

* halt was used before ACPI (Advanced Configuration and Power Interface)which today will turn off the power for us. It would halt the system and then print a message to the effect of "it's ok to power off now". Back then there were physical on/off switches, rather than the combo ACPI controlled power button of modern computers.
* poweroff, naturally will halt the system and then call ACPI power off.

These days halt is smart enough to automatically call poweroff if ACPI is enabled. In fact, they are functionally equivalent now.

### reboot

reboot command can be used to shutdown or reboot linux.

To reboot linux just call the reboot command directly without any options.

This will perform a graceful shutdown and restart of the machine. This is what happens when we click restart from your menu.

`-f` option will forcefully reboot the machine. This is similar to pressing the power button of the CPU. No shutdown takes place. The system will reset instantly.

### halt

The next command is the halt command. This can shutdown a system but has some other options:

the halt command also has force option but try not to use it, because it might put your system in an in consistant state.

### poweroff

There is another command exactly same as the halt command. It does the same things and takes the same options.

and we are done.

.

.

.

Sources:

<https://www.linuxjournal.com/article/1274>

<https://en.wikipedia.org/wiki/Runlevel>

<https://www.geeksforgeeks.org/run-levels-linux/>

<https://www.ostechnix.com/check-runlevel-linux/>

<https://geek-university.com/linux/etc-inittab/><https://developer.ibm.com/tutorials/l-lpic1-101-3/>

<https://www.liquidweb.com/kb/linux-runlevels-explained/>

<https://linux.die.net/man/8/telinit>

<https://unix.stackexchange.com/questions/434560/what-differences-it-will-make-if-i-use-telinit-6-instead-of-reboot-command>

<https://askubuntu.com/questions/5039/what-is-the-difference-between-etc-init-and-etc-init-d>

<https://www.systutorials.com/239880/change-systemd-boot-target-linux/>

<https://www.tecmint.com/change-runlevels-targets-in-systemd/>

<https://fedoramagazine.org/systemd-getting-a-grip-on-units/>

<https://www.linode.com/docs/quick-answers/linux-essentials/what-is-systemd/>

<https://www.howtoforge.com/linux-wall-command/>

[https://en.wikipedia.org/wiki/Wall\_(Unix)](https://en.wikipedia.org/wiki/Wall_%28Unix%29)

<http://man7.org/linux/man-pages/man1/wall.1.html>

[http://man7.org/linux/man-pages/man8/shutdown.8.html](https://legacy.gitbook.com/book/borosan/lpic1-exam-guide/edit#)

<https://www.computerhope.com/unix/ushutdow.htm>

<https://unix.stackexchange.com/questions/42572/is-halt-the-same-as-shutdown-h-and-poweroff-the-same-as-shutdown-p/42581>

<https://www.tecmint.com/shutdown-poweroff-halt-and-reboot-commands-in-linux/>

<https://www.binarytides.com/linux-command-shutdown-reboot-restart-system/>

Copy

# 102.1. Design hard disk layout

## **102.1 Design hard disk layout**

**Weight:** 2

**Description:** Candidates should be able to design a disk partitioning scheme for a Linux system.

**Key Knowledge Areas:**

* Allocate filesystems and swap space to separate partitions or disks
* Tailor the design to the intended use of the system
* Ensure the /boot partition conforms to the hardware architecture requirements for booting
* Knowledge of basic features of LVM

**Terms and Utilities:**

* / (root) filesystem
* /var filesystem
* /home filesystem
* /boot filesystem
* swap space
* mount points
* partitions

In this light weight lesson first we will have a quick review over Hard Disks structure and how data are stored on them, next we will take a look at linux disk layout.

### Disk tracks, cylinders, and sectors

A disk is divided into tracks, cylinders, and sectors.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbcctbMLMGFpTyf7%252Fdisklayout-diskstructure.jpg%3Fgeneration%3D1569999719247497%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=ce1729d&sv=2)

A **track** is that portion of a disk which passes under a single stationary head during a disk rotation, a ring 1 bit wide.

A **cylinder** is comprised of the set of tracks described by all the heads (on separate platters) at a single seek position. Each cylinder is equidistant from the center of the disk. A track is divided into segments of sectors, which is the basic unit of storage.

A **sector**, being the smallest physical storage unit on the disk, is almost always 512 bytes in size because 512 is a power of 2 (2 to the power of 9). The number 2 is used because there are two states in the most basic of computer languages — on and off.

### Partitions

Disk partitioning or disk slicing is the creation of one or more regions on a hard disk or other secondary storage, **so that an operating system can manage information in each region separately**. These regions are called partitions.

The disk stores the **information about the partitions' locations and sizes** in an area known as the **partition table** that the operating system reads before any other part of the disk. Each partition then appears in the operating system as a distinct "logical" disk that uses part of the actual disk.

When doing an installation there is normally a minimum disk configuration of two partitions that needs to be created:

* **/** (root): directory that contains the Linux distribution.
* **Swap space**

### **What is swap space?**

Swap space in Linux is used when the amount of physical memory (RAM) is full. If the system needs more memory resources and the RAM is full, inactive pages in memory are moved to the swap space. While swap space can help machines with a small amount of RAM, it should not be considered a replacement for more RAM. Swap space is located on hard drives, which have a slower access time than physical memory.

**Swap space can be** a **dedicated swap partition** (recommended), a **swap file**, or a **combination of swap partitions and swap files**.

Swap should equal 2x physical RAM for up to 2 GB of physical RAM, and about 1.5x physical RAM for more than 2 GB of physical RAM. How ever that an old recipe and it depends on what kind of system we are talking about.

### **mount points**

All **partitions are attached to the system via a mount point**. The mount point defines the place of a particular data set in the file system. Usually, all partitions are connected through the root partition. On this partition, which is indicated with the slash (/), directories are created. These empty directories will be the starting point of the partitions that are attached to them.

During system startup, all the partitions are thus mounted, (will be described in the file /etc/fstab). Some partitions are not mounted by default, for instance if they are **not constantly connected to the system, such like the usb storage**. If well configured, the device will be mounted as soon as the system notices that it is connected, or it can be user-mountable.

### File Systems

**A filesystem is the methods and data structures that an operating system uses to keep track of files on a disk or partition**; that is, the way the files are organized on the disk. Without a file system, information placed in a storage medium would be one large body of data with no way to tell where one piece of information stops and the next begins.

Different filesystems have different organizing structures to determine where the data and indexing information will be stored:

* **FAT32**: FAT32 is an older Windows file system, but it’s still used on removable media devices — just the smaller ones, though. Larger external hard drives of 1 TB or so will likely come formatted with NTFS
* **NTFS**: Modern versions of Windows — since Windows XP — use the NTFS file system for their system partition. External drives can be formatted with either FAT32 or NTFS.
* **HFS**+: Macs use HFS+ for their internal partitions, and they like to format external drives with HFS+ too.
* **Ext2/Ext3/Ext4**: You’ll often see the Ext2, Ext3, and Ext4 file systems on Linux.
* **Btrfs**: Btrfs — “better file system” — is a newer Linux file system that’s still in development. It isn’t the default on most Linux distributions at this point, but it will probably replace Ext4 one day. The goal is to provide additional features that allow Linux to scale to larger amounts of storage.
* **Swap**: On Linux, the “swap” file system isn’t really a file system. A partition formatted as “swap” can just be used as swap space by the operating system

#### Linux Directory Structure

Linux uses a hierarchical file system structure, much like an upside-down tree, with root (/) at the base of the file system and all other directories spreading from there. The linux directory consists of many file systems that can be on many devices even on many servers.

Lets explain what they are for:

* **/** (root): the root filesystem, mounted before the kernel loads the first process. The bootloader tells the kernel what to use as the root filesystem (it's usually a disk partition but could be something over the network).
* **/bin** : All the executable binary programs (file) required during booting, repairing, files required to run into single-user-mode, and other important, basic commands.
* **/boot** : Holds important files during boot-up process, including Linux Kernel.
* **/dev** : an in-memory filesystem where device files are automatically created by udev based on available hardware.Contains device files for all the hardware devices on the machine e.g., cdrom, cpu, etc
* **/etc** : Contains Application’s configuration files, startup, shutdown, start, stop script for every individual program.
* **/home** : Home directory of the users. Every time a new user is created, a directory in the name of user is created within home directory which contains other directories like Desktop, Downloads, Documents, etc.
* **/lib** : The Lib directory contains kernel modules and shared library images required to boot the system and run commands in root file system.
* **/media** : Temporary mount directory is created for removable devices .
* **/mnt** : Temporary mount directory for mounting file system.
* **/opt** : Optional is abbreviated as opt. Contains third party application software.
* **/proc** : A virtual and pseudo file-system which contains information about running process with a particular Process-id aka pid.
* **/root** : This is the home directory of root user and should never be confused with ‘/‘
* **/run** : This directory is the only clean solution for early-runtime-dir problem.
* **/sbin** : Contains binary executable programs, required by System Administrator, for Maintenance.
* **/srv** : Service is abbreviated as ‘srv‘. This directory contains server specific and service related files.
* **/sys** : Modern Linux distributions include a /sys directory as a virtual filesystem, which stores and allows modification of the devices connected to the system.
* **/tmp** :System’s Temporary Directory, Accessible by users and root. Stores temporary files for user and system, till next boot.
* **/usr** : Contains executable binaries, documentation, source code, libraries for second level program.
* **/var** : Stands for variable. The contents of this file is expected to grow. This directory contains log, lock, spool, mail and temp files.

Almost all of linux directories can be a separated partition, except /etc directory because it contains scripts which are required during boot process so it can be mounted with / partition and accessible at the very beginning boot process.

### Designing Hard Disk Layout

Of course just because we can partition a disk doesn't mean we should! The more partitions we create, the more there is to manage. So we shouldn't make extra partitions unless we consider the extra work they create to be worth the additional protections they provide.

If the root partition runs out of space the system will crash. If some non-root partition runs out of space, the system will remain up and the System Administrator can login and fix things. Thus the directories such as /home, /tmp, and /var that users can easily fill with downloads, email, etc., are prime candidates for extra partitions. So are any other directories that might grow (directories for FTP uploads, database files, etc.).

If the partition containing the log files runs out of space, the system won't be able to write any log messages that could help an System Administrator to determine what went wrong. On the other hand some rapidly recurring error (or attack) can cause log files to grow very large very quickly, filling the partition containing them. So the directory containing log files, (usually /var/log), is a good choice for a separate partition.

All in all try to follow vendor-recommended standard disk layout if not, be smart and do partitioning based on the server type and behaviour of your application(s).

#### Blocks vs. Sectors

**A sector is a physical spot on a formatted disk that holds information.** When a disk is formatted, tracks are defined (concentric rings from inside to the outside of the disk platter). Each track is divided into a slice, which is a sector. On hard drives and floppies, each sector can hold 512 bytes of data.

**A block, on the other hand, is a group of sectors that the operating system can address (point to).** A block might be one sector, or it might be several sectors (2,4,8, or even 16). The bigger the drive, the more sectors that a block will hold.

**So why are there blocks? Why doesn't the operating system just point straight to the sectors?** Because there are limits to the number of blocks, or drive addresses, that an operating system can address. By defining a block as several sectors, an OS can work with bigger hard drives without increasing the number of block addresses.

up to now we have talked about partitions, partitions are cool but partitions are fixed sized and that is not easy to resize in some cases. On a server we even need **more flexibility**. That is why **LVM** was invented.

### LVM

Logical volume management (LVM) is a **form of storage virtualization** that offers system administrators a more **flexible** approach to managing disk storage space than traditional partitioning.

There are 3 concepts that LVM manages:

* **Logical Volumes (LV)**: A Logical Volume is the conceptual equivalent of a disk partition in a non-LVM system. Logical volumes **are block devices which are created from the physical extents present in the same volume group**. File systems are built on top of logical volumes.
* **Volume Groups (VG)**: A Volume Group **gathers together a collection of Logical Volumes and Physical Volumes into one administrative unit**. Volume group is divided into fixed size physical extents.
* **Physical Volumes (PV)**: Each Physical Volume can be a disk partition or whole disk.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbctKYBg0BGpVb_c%252Fdisklayout-lvm.jpg%3Fgeneration%3D1569999719025130%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=7265bfb8&sv=2)

Logical Volume Management (LVM) makes it easier to manage disk space. If a file system needs more space, it can be added to its logical volumes from the free spaces in its volume group and the file system can be re-sized as we wish. If a disk **starts to fail**, replacement disk can be registered as a physical volume with the volume group and the logical volumes extents can be migrated to the new disk without data loss.

**How LVM works?**

It works by chunking the physical volumes (PVs) into physical extents (PEs). The PEs are mapped onto logical extents (LEs) which are then pooled into volume groups (VGs). These groups are linked together into logical volumes (LVs) that act as virtual disk partitions and that can be managed as such by using LVM.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbcviQ-ULB9WEEY6%252Fdisklayout-lvmdetails.jpg%3Fgeneration%3D1569999718778538%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=4c5802dd&sv=2)

There is one thing that we should know about LVM, we can not put intire server in LVM! Because there is a /boot directory and /boot directory must be available at the moment of booting, so it must be seen from master boot record (or GUID partition).

And in order to see /boot directory at the moment of booting it should always be on a traditional partition.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbcx5LB_NY1dtFKq%252Fdisklayout-lvmboot.jpg%3Fgeneration%3D1569999724519694%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=98239967&sv=2)

That is all.

.

.

.

.

Sources:

<https://www.studytonight.com/operating-system/secondary-storage>

<https://www2.cs.duke.edu/csl/docs/sysadmin_course/sysadm-30.html>

<http://www.ntfs.com/hard-disk-basics.htm>

[https://en.wikipedia.org/wiki/Disk\_partitioning](https://legacy.gitbook.com/book/borosan/lpic1-exam-guide/edit#)

<https://www.tldp.org/LDP/sag/html/filesystems.html>

[https://en.wikipedia.org/wiki/File\_system](https://legacy.gitbook.com/book/borosan/lpic1-exam-guide/edit#)

<https://searchstorage.techtarget.com/definition/file-system>

<https://www.howtogeek.com/196051/htg-explains-what-is-a-file-system-and-why-are-there-so-many-of-them/>

<https://www.centos.org/docs/5/html/5.2/Deployment_Guide/s1-swap-what-is.html>

<https://www.linuxtopia.org/online_books/introduction_to_linux/linux_Mount_points.html>

<https://unix.stackexchange.com/questions/12040/what-mount-points-exist-on-a-typical-linux-system>

<https://www.tutorialspoint.com/unix/unix-file-system.htm>

<https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/>

<https://wpollock.com/AUnix1/Partitioning.htm>

[http://www.alphaurax-computer.com/computer-tips/hard-drive-knowledge-blocks-vs-sectors](https://legacy.gitbook.com/book/borosan/lpic1-exam-guide/edit#)

<https://searchdatacenter.techtarget.com/definition/logical-volume-management-LVM>

<https://wiki.ubuntu.com/Lvm>

<https://www.thegeekdiary.com/redhat-centos-a-beginners-guide-to-lvm-logical-volume-manager/>

<https://www.tecmint.com/create-lvm-storage-in-linux/>

Copy

# 102.2. Install a boot manager

## **102.2 Install a boot manager**

**Weight:** 2

**Description:** Candidates should be able to select, install and configure a boot manager.

**Key Knowledge Areas:**

* Providing alternative boot locations and backup boot options
* Install and configure a boot loader such as GRUB Legacy
* Perform basic configuration changes for GRUB 2
* Interact with the boot loader

**The following is a partial list of the used files, terms and utilities:**

* menu.lst, grub.cfg and grub.conf
* grub-install
* grub-mkconfig
* MBR

We have talked about linux boot process and boot loaders. We got introduced to LILO as a very old boot loader which was replaced by GRUB in late 1990s. In this course we take a closer look at GRUB and GRUB2 boot loaders .

## GRUB

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbX8d1XQT8O1_OZV%252FGrub_logo.png%3Fgeneration%3D1569999728358512%26alt%3Dmedia&width=300&dpr=4&quality=100&sign=3537480f&sv=2)![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXCUydGtqtUvnS1%252FGrub_logo2.png%3Fgeneration%3D1569999728238656%26alt%3Dmedia&width=300&dpr=4&quality=100&sign=8dc289b7&sv=2)

GRUB (GRand Unified Bootloader) is a boot loader package developed to support multiple operating systems and allow the user to select among them during boot-up.

#### GRUB versions

GRUB was created by Erich Stefan Boleyn and has been further developed under the GNU project as GNU GRUB. The original package is still available for download but no longer being developed.

**GRUB2** has replaced what was formerly known as GRUB (i.e. version 0.9x), which has, in turn, become **GRUB Legacy.** Enhancements to GRUB2 are still being made, but the current released versions are quite usable for normal operation.

### How does GRUB work?

When a computer boots, the BIOS transfers control to the first boot device, which can be a hard disk, a floppy disk, a CD-ROM, or any other BIOS-recognized device.

#### MBR

The first sector on a hard is called the Master Boot Record (MBR). This sector is only 512 bytes long and contains a small piece of code (446 bytes) called the primary boot loader and the partition table (64 bytes) describing the primary and extended partitions.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXFUGnPdIROQR2n%252Fbootloader-mbr.jpg%3Fgeneration%3D1569999728181812%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=4996336a&sv=2)

GRUB replaces the default MBR with its own code:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lx_RwEKy0Gty4U6D_OF%252F-Lx_XE01ryK-tCbO1hqa%252Fmbr_color2.jpg%3Falt%3Dmedia%26token%3D5ee5d35e-1fbf-4901-9749-719375c4bef2&width=768&dpr=4&quality=100&sign=e7f36d&sv=2)

By default, MBR code looks for the partition marked as active and once such a partition is found, it loads its boot sector into memory and passes control to it.

Furthermore, GRUB works in stages.

* **Stage 1** is located in the MBR and mainly points to Stage 2, since the MBR is too small to contain all of the needed data.
* **Stage 2** points to its configuration file, which contains all of the complex user interface and options we are normally familiar with when talking about GRUB. Stage 2 can be located anywhere on the disk. If Stage 2 cannot find its configuration table, GRUB will cease the boot sequence and present the user with a command line for manual configuration.

The Stage architecture allows GRUB to be large (~20-30K) and therefore fairly complex and highly configurable, compared to most bootloaders, which are sparse and simple to fit within the limitations of the Partition Table.

### GRUB Legacy vs GRUB2

Lets draw a big picture:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXL4YxqaL1iTszC%252Fbootloader-grubvsgrub2.jpg%3Fgeneration%3D1569999728267623%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=901fa031&sv=2)

/boot/grub/menu.lst in GRUB Legacy has been replaced by /boot/grub/grub.cfg in GRUB2.

Which version of linux use which grub ?

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXNYlQhPfsueRFh%252Fbootloader-grubdistro.jpg%3Fgeneration%3D1569999728172743%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=ac991715&sv=2)

**Demonstration**

In order to show differences between GRUB Legacy and GRUB2, lets change `timeout` parameter in Two systems (CentsOS5 and Centos7) :

### menu.lst (GRUB Legacy)

just make a change in menu.lst and save it and that is all.

### grub.cfg (GRUB2)

**grub.cfg** is overwritten by certain Grub 2 package updates, whenever a kernel is added or removed, or when the user runs update-grub.**Do not edit grub.cfg directly!!**

In order to make any changes in grub.cfg two steps are required.

### 1-/etc/default/grub

first edit /etc/default/grub:

save chanages in /etc/default/grub. The configurations are written to /boot/grub2/grub.cfg using grub-mkconfig command

### 2- grub-mkconfig

grub-mkconfig Generate a GRUB configuration file.

It reads main grub script files from **/etc/grub.d** and setting from **/etc/default/grub** and print out generated configuration.

grub2-mkconfig options:

For saving generated configuration we use `-o` option (it is recommanded to take a backup from `/boot/grub2/grub.cfg` file, how ever this is not touching Master Boot Record and just re touches GRUB menu):

We where able to use `grub2-mkconfig > /boot/grub2/grub.cfg` command too,and GRUB2 configuration steps finish here.

#### grub-update

When you run the update-grub command, GRUB automatically combines the settings from the /etc/default/grub file, the scripts from the /etc/grub.d/ directory, and everything else, creating a /boot/grub/grub.cfg file that’s read at boot.

### GRUB Interfaces

There are three interfaces in GRUB which all provide different levels of functionality. The Linux kernel can be booted by the users with the help of these interfaces. Details about the interfaces are:

**1-Menu Interface**

The GRUB is configured by the installation program in the menu interface. It is the default interface available. It contains a list of the operating systems or kernels which is ordered by name. A specific operating system or kernel can be selected using the arrow keys and it can be booted using the enter key.

GRUB Legacy

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXvhTAGJLIPhiRz%252Fbootloader-grub1menu.jpg%3Fgeneration%3D1569999728194182%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=5de697dc&sv=2)

GRUB2

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXxkQzAs-L9JwQv%252Fbootloader-grub2menu.jpg%3Fgeneration%3D1569999728163500%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=2ee90fc1&sv=2)

Missing 'a' hah!

**2-Menu Entry Editor Interface**

The e key (a key GRUB Legacy) in the boot loader menu is used to access the menu entry editor. All the GRUB commands for the particular menu entry are displayed there and these commands may be altered before loading the operating system.

GRUB Legacy

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXzM3NwjDfsFgQF%252Fbootloader-grub1menuent.jpg%3Fgeneration%3D1569999728304680%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=36b27335&sv=2)

GRUB2

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbY0CcAkikm-7qbM%252Fbootloader-grub2menuent.jpg%3Fgeneration%3D1569999728277174%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=4bf6e0db&sv=2)

**3-Command Line Interface**

This interface is the most basic GRUB interface but it grants the most control to the user. Using the command line interface, any command can be executed by typing it and then pressing enter. This interface also features some advanced shell features.

GRUB Legacy

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbY2cV169AB-5jwm%252Fbootloader-grub1menucmd.jpg%3Fgeneration%3D1569999728318018%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=9d75c03d&sv=2)

It is possible to have GRUB Legacy command prompt after rebooting the system and gain information form there.

GRUB2

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbY4-wJ2kLaLajZa%252Fbootloader-grub2menucmd.jpg%3Fgeneration%3D1569999728168314%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=eb43c0b4&sv=2)

Note: Partition numbering has changed in GRUB2. The first partition is 1 in GRUB2 rather than 0 (GRUB Legacy). The first device/drive is still hd0 by default (no change).

### GRUB Installation

Normally when we setup a system GRUB is installed for us but there are some cases which we might need to install GRUB ourselves. There are different ways to install GRUB.

If we are on old system with GRUB legacy we can run grub-install command or using setup command in GRUB shell.

If we are on GRUB2 we can use one of GRUB2 utilities.

### grub2-install

grub-install installs GRUB onto a device. This includes copying GRUB images into the target directory (generally /boot/grub), and on some platforms may also include installing GRUB onto a boot sector.

as an example `grub2-install /dev/sdb` will install grub on sdb device, to the master boot record of my hard disk.

How ever instaling GRUB a from running system seems cool, but most of the time there is a problem during boot process and we can not get into our system any more, so we need to reinstall GRUB from GRUB shell. Unfortunately the setup command has been removed from GRUB2 shell and it would need more efforts. We need to bring up the system in rescue mode using a live cd and then install GRUB on our hard disk using current temporary root system file:

it is just an example and do not run it because you would mess up your current system!

`grub2-install --boot-directory=/tmp/root/boot /dev/sda`

.

.

.

Sources:

<https://en.wikipedia.org/wiki/GNU_GRUB>

<https://whatis.techtarget.com/definition/GRUB-GRand-Unified-Bootloader>

<https://www.gnu.org/software/grub/>

<https://www.dedoimedo.com/computers/grub.html>

<https://www.tutorialspoint.com/what-is-grub-in-linux>

<https://help.ubuntu.com/community/Grub2>

<https://www.mankier.com/8/grub2-install>

.

Copy

# 102.3. Manage shared libraries

## **102.3 Manage shared libraries**

**Weight:** 1

**Description:** Candidates should be able to determine the shared libraries that executable programs depend on and install them when necessary.

**Key Knowledge Areas:**

* Identify shared libraries
* Identify the typical locations of system libraries
* Load shared libraries

**Terms and Utilities:**

* ldd
* ldconfig
* /etc/ld.so.conf
* LD\_LIBRARY\_PATH

#### What is a library?

In programming, a library is an assortment of pre-compiled pieces of code that can be reused in a program. Libraries simplify life for programmers, in that they provide reusable functions, routines, classes, data structures and so on (written by a another programmer), which they can use in their programs.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_RZyGkYU7k69Ugw%252Fsharedlib-intro.jpg%3Fgeneration%3D1569999708885481%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=ae9e61c0&sv=2)

Linux supports two classes of libraries, namely:

* Static libraries – are bound to a program statically at compile time.
* Dynamic or shared libraries – are loaded when a program is launched and loaded into memory and binding occurs at run time.

**Static libraries vs Shared libraries**

* Each program using routines from a static library has a copy of them in the executable file. This wastes disk space and (if more than one such program is in use at the same time) RAM as well. Also, when a static library is updated, all the programs using it must be recompiled in order to take advantage of the new code.
* When a program uses a shared library instead, the program binary does not include a copy of the code, but only a reference to the library. The run time loader, finds the library and loads it into memory at the same time as the program.One advantage of using dynamic library is that when a library is updated ( security issues ) all other programs take advantage of new code without recompiling.

Dynamic or shared libraries can further be categorized into two groups ( beyond the scope of LPIC exam):

* **Dynamically linked libraries** – here a program is linked with the shared library and the kernel loads the library (in case it’s not in memory) upon execution.
* **Dynamically loaded libraries** – the program takes full control by calling functions with the library.

### Libraries locations in linux

Depending on library, Linux stores its libraries mainly in three locations:

* **/lib**
* **/usr/lib**
* **/usr/local/lib**

**/lib** : The /lib directory contains those **shared library images needed to boot** the system and run the commands in the root filesystem, ie. by binaries in /bin and /sbin.

The /lib folder sister folders are /lib32 and /lib64.

**/usr/lib** : **All software libraries** are installed here. This **does not contain system default or kernel libraries**.

**/usr/local/lib**: To place **extra system library files** here. These library files can be used by different applications.

Also **/var/lib** Directory, holds **dynamic data libraries/files** like the rpm/dpkg database and game scores.

In this article we will discuss specifically about Shared Libraries.

### Shared Library Naming Conventions

Shared libraries are named in three ways:

* library name (a.k.a "soname")
* filename (a.k.a "real name")(absolute path to file which stores library code)
* "linker name"

**1)**Every shared library has a special name called the **"soname''**. The soname has the prefix "**lib**'', the name of the library, the phrase "**.so**'', followed by a period and a **version number** that is incremented whenever the interface changes .

A fully-qualified soname includes as a prefix the directory it's in.

On a working system a fully-qualified soname is simply a symbolic link to the shared library's "real name''.

**2)**Every shared library also has a **"real name''**, which is the filename containing the actual library code. The real name adds to the soname a period, a minor number, another period, and the release number. The last period and release number are optional.

**3)**In addition, there's the name that the compiler uses when requesting a library, (I'll call it the **"linker name''**), which is simply the soname without any version number.

Okey lets explain all in an example:

Thus, `/usr/lib/libreadline.so.6` is a fully-qualified soname, which is set to be a symbolic link to some realname like `/usr/lib/libreadline.so.6.3`. There should also be a linker name, `/usr/lib/libreadline.so` which could be a symbolic link referring to `/usr/lib/libreadline.so.6`.

### ldd

To **get a list of all shared library dependencies for a binary file**, you can use the ldd utility**.** For example lets see what shared libraries are required by ls command:

Try `ltrace ls` to get surprised! But how poor ls can find its required shared libraries?

### Locating Shared Libraries in Linux

A program can call a library using its library name or filename, and a library path stores directories where libraries can be found in the filesystem. But How it can find them? Lets show the structure in a picture:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_RgmYD5ykptBozW%252Fsharedlib-filestructure.jpg%3Fgeneration%3D1569999708826636%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=4143470f&sv=2)

These three files helps programs to find their required shared libraries.

### ld.so.conf

ld.so.conf file tells the system where to look for library files, that is kind of an address book.

Traditionally in the past, it included all the paths which libraries existed. Today more abstraction has been implemented and it just points to ld.so.conf.d directory. Simply it says go to the ld.so.conf.d directory and load any configuration files.

### /etc/ld.so.conf.d

ld.so.conf.d directory contains several configuration files for the kernel or for other third party applications.

Lets see what is inside configuration files :

We can add a new configuration file or edit any of them in order to include a new path.

### ldconfig

Because shared libraries can exist in many different directories, searching through all of these directories when a program is launched would be greatly inefficient, which is one of the likely disadvantages of dynamic libraries. Therefore a mechanism of caching employed, performed by a the program ldconfig.

By default, ldconfig reads the content of /etc/ld.so.conf, creates the appropriate symbolic links in the dynamic link directories, and then writes a cache to /etc/ld.so.cache which is then easily used by other programs.

### ld.so.cache

This is a binary file, so that is not something we usually like to see :

use `string` command intead and it just shows human readable binary files, also `lconfig -p` prints cache.

This is very important especially when we have just installed new shared libraries or created our own, or created new library directories. We need to run ldconfig command to effect the changes.(The out put has been truncated):

ldconfig command has some options:

After creating our shared library, we need to install it.

### Installing a Dynamic Library:

There are several ways to install a dynamic library:

**1)**We can either move it into any of the standard directories mentioned above, and run the ldconfig command.

**2)**The method above sets the library path permanently. To set it temporarily, use the LD\_LIBRARY\_PATH environment variable on the command line.

## LD\_LIBRARY\_PATH

In Linux, the environment variable LD\_LIBRARY\_PATH is a colon-separated set of directories where libraries should be searched for first, before the standard set of directories; this is useful when debugging a new library or using a nonstandard library for special purposes.

The usual dynamic linker on Linux uses a cache to find its libraries, So there is no default value for LD\_LIBRARY\_PATH, default library lookup doesn’t need it at all. If LD\_LIBRARY\_PATH is defined, then it is used first, but doesn’t disable the other lookups (which also include a few default directories).

Whether it has a default value or not we can use blow command to add our new library path:

Do not forget that these changes are not permanent and If you want to keep the changes permanent, then add above line in the shell initialization file**/etc/profile**(global) or**~/.profile**(user specific), which will be discussed in next lessons.

That's all!

.

.

.

Sources:

<https://www.tecmint.com/understanding-shared-libraries-in-linux/>

<https://www.ibm.com/developerworks/linux/library/l-dynamic-libraries/>

<http://www.linuxforums.org/forum/newbie/151875-what-libraries.html>

<https://www.linuxnix.com/linux-directory-structure-lib-explained/>

<https://askubuntu.com/questions/17545/where-does-ubuntu-store-its-library-files>

<https://medium.com/@jhuang1012bn/static-library-and-shared-library-de6def6b1d3b>

<http://tldp.org/HOWTO/Program-Library-HOWTO/shared-libraries.html>

<https://unix.stackexchange.com/questions/354295/what-is-the-default-value-of-ld-library-path>

Copy

# 102.4. Use Debian package management

## **102.4 Use Debian package management**

**Weight:** 3

**Description:** Candidates should be able to perform package management using the Debian package tools.

**Key Knowledge Areas:**

* Install, upgrade and uninstall Debian binary packages
* Find packages containing specific files or libraries which may or may not be installed
* Obtain package information like version, content, dependencies, package integrity and installation status (whether or not the package is installed)

**Terms and Utilities:**

* /etc/apt/sources.list
* dpkg
* dpkg-reconfigure
* apt-get
* apt-cache
* aptitude

### What is a package?

A package is a piece of software that provides a piece of the system. Examples of packages:

* Linux Kernel
* The C compiler
* The Firefox web browser
* The USB library to interact with USB devices

A package contains the files and other instructions needed to make one Software component work on the system.

Packages have dependencies from other packages that must also be downloaded and installed before installing the package with dependencies.

In old days Linux administrators had to deal with dependency hell for installing a package which caused meta package handlers were born.

### What is a Package Manager?

The packet manager is the utility that handles the downloading, unpacking and putting the unpacked pieces in the right places.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGaev3LE1RLoEDFwI%252Fdebpack-packagemgmnt.png%3Fgeneration%3D1569999724776434%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=abb524db&sv=2)

The general workflow starts with the user requesting a package using the package manager available in the system. The Package manager then finds the requested package from a known location (called software repository) and downloads it. The Package Manager then installs the package and advises on any manual steps that it finds necessary.

Package management tools help System/Server Administrators in many ways such as:

* Downloading and installing software
* Compile software from source
* Keeping track of all software installed, their updates and upgrades
* Handling dependencies
* and also keeping other information about installed software and many more

#### What is a Software Repository?

A Linux repository **is a storage location from which our system retrieves and installs OS updates and applications.** Each repository is a collection of software hosted on a remote server and intended to be used for installing and updating software packages on Linux systems.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGaezNYZHP53EFr5B%252Fdebpack-swrepo.jpg%3Fgeneration%3D1569999724743038%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=413dc2d6&sv=2)

Package Manager consists of two entities:

* low-level tool
* high-level too

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LxR5V-xXapknlnpx3TO%252F-LxR71QzKHrbtAgwwNgL%252Fdebpack-all.jpg%3Falt%3Dmedia%26token%3D5242990d-4fa7-40dd-8911-6996fcf9eee1&width=768&dpr=4&quality=100&sign=5de8a75f&sv=2)

a **low-level** tool (such as **dpkg** or **rpm**), takes care of the details of unpacking individual packages, running scripts, getting the software installed correctly, while a **high-level** tool (such as **apt-get**, yum, or **zypper**) works with groups of packages, downloads packages from the vendor, and figures out dependencies

The core parts of a linux distro and most of its add-on Software are installed via a Package Management System.

In this course we will talk about package management in Debian based distributions.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGaf25yeoYcdHeFGW%252Fdebpack-deb.jpg%3Fgeneration%3D1569999724713734%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=3fe4c4ce&sv=2)

### dpkg

dpkg is a package manager for Debian-based systems. It can install, remove, and build packages, but unlike other package management systems, **it cannot automatically download and install packages or their dependencies.**

The dpkg has database and its is located under/var/lib/dpkg directory ;

the "status" file contains the list of installed software on the current system.

**Lets take a look at most useful switches:**

-l | --list list all packages installed on the system ( --get-selection does the same):

To view a specific package installed or not use the option “-l” along with package-name.

dpkg -i | --install ,install a local .deb file :

.deb is extension of the software package format for the Linux distribution Debian.

And if a package requires any dependencies you would get into trouble:

dpkg does not handle dependencies so and we try to install a package one of two thing will happend:

* whether It will completely fail !
* or it will install the package but leave it unconfigured until all dependencies are installed and the apt tool is used to finish the configuration(`apt-get install -f`we will see it).

We can also use `dpkg --force-depends`to omit dependencies or `--force-conflicts` to close its eyes to any possible conflicts or `--force-reinstall`for reinstalling, but do not forget that any `--force` command can cause a problem and make the system **inconsistent** state.

dpkg -L | --listfiles ,To list the files installed by a package:

dpkg -S | --serach ,If we are not sure which package installed a file, dpkg -S may be able to tell us :

note:We can also use `dpkg -S string` and it would do use regular expression search in the file system to find any matches with the string we have types.

dpkg -s | --status ,Check a Package is installed or not:

dpkg -c | --contents ,will display the contents of a “.deb” package in long-list format:

Do not mess `-c` with -C, -C checks for partially installed packages.

> **What is debconf?**
>
> When packages are being installed, debconf asks the user questions which determine the contents of the system-wide configuration files associated with that package and stores the user/admin preferences in a database.
>
> Later as the packages are installing, their scripts use the configuration preferences in the database to generate configuration files and otherwise do administrative tasks.This saves the hassle of editing configuration files by hand, and also of waiting for each individual package to install before responding to certain configuration questions.

### dpkg-reconfigure

After package installation, it is possible to go back and change the configuration of a package by using the dpkg-reconfigure program (or another program such as Synaptic). For example try:

dpkg -r | --remove , remove a package using its name :

dpkg cares about dependencies by and does not remove them by default,(which is why it doesn't get .deb file, instead it requires package name inorder to explore dependencies), how ever we can force it with`dpkg -r --force-depends` command but is NOT recommended. It is better to use a package manager that handles dependencies to ensure that the system is in a consistent state.

note:dpkg -P | --purge purge a package! We can also use ‘P‘ option in place of ‘r’ which will remove the package along with configuration file. The ‘r‘ option will only remove the package and not configuration files.

Do not get confused -P with -p , -p will print information about package.

dpkg has lots of options and switches try dpkg --help for more information :

When we work with dpkg we have to have .deb package in hand in order to work with. But how about Package Manager?How package manager like apt find software repositories in Debian based systems?

### /etc/apt/sources.list

This file contains information about what repositories [online / remote ] the system will use. This file contains lines in the following format:

`deb` lines are relative to binary packages, that we can install with apt.
`deb-src` lines are relative to source packages (as downloaded by apt-get source $package) and next compiled. Source packages are needed only if we want to compile some package ourselves, or inspect the source code for a bug. Ordinary users don't need to include such repositories.

The repository components are:

* Main - Officially supported software.
* Restricted - Supported software that is not available under a completely free license.
* Universe - Community maintained software, i.e. not officially supported software.
* Multiverse - Software that is not free.

Some distributions like Ubuntu also have `/etc/apt/sources.list.d` directory which provides a way to add sources.list entries in separate `.list` files.

All `.list` files are compiled and added to `/etc/apt/sources.list` file.

## APT (Advanced Packaging Tool)

It is a very popular, free, powerful and useful command line package management system that is a front end for dpkg package management system.Initially it was designed for Debian’s`.deb`packages

Apt is whole command line with no GUI. Whenever invoked from command line along with specifying the name of package to be installed, it finds that package in configured list of sources specified in ‘/etc/apt/sources.list’ along with the list of dependencies for that package and sorts them and automatically installs them along with the current package thus letting user not to worry of installing dependencies.

It is consist of two commands:

* **apt-get**
* **apt-cache**

### **What is apt-get?**

The apt-get is the command-line tool for working with APT software packages, that is used to work with Ubuntu’s APT (Advanced Packaging Tool) library to perform installation of new software packages, removing existing software packages, upgrading of existing software packages and even used to upgrading the entire operating system.

**apt-get update**

This will help us to download a **list of packages** from different repositories included on our system and updates them when there are new versions of packages and their dependencies. (After any modification in repositories we have to run apt-update manually other wise, system local cache from previous repositories will be used)

to see what packages can be upgraded:

**apt-get upgrade**

The ‘upgrade‘ command is used to upgrade all the currently installed software packages on the system. Under any circumstances currently installed packages are not removed or packages which are not already installed neither retrieved and installed to satisfy upgrade dependencies.

New versions of currently installed packages that cannot be upgraded without changing the install status of another package will be left at their current version.

An update must be performed first so that apt-get knows that new versions of packages are available.

**apt-get dist-upgrade**

dist-upgrade in addition to performing the function of upgrade, also intelligently handles changing dependencies with new versions of packages (including the kernel)

If we want to upgrade, unconcerned of whether software packages will be added or removed to fulfill dependencies, use the ‘dist-upgrade‘ sub command.

apt-get has a "smart" conflict resolution system, and it will attempt to upgrade the most important packages at the expense of less important ones if necessary.

**apt-get autoremove**

The ‘autoremove‘ sub command is used to auto remove packages that were certainly installed to satisfy dependencies for other packages and but they were now no longer required. For example:

**apt-get install**

Install a package as follows by specify a single package name or install many packages at once by listing all their names:

**apt-get remove**

Remove Packages without their Configuration Files:

**apt-get purge**

apt with remove, it only removes the package files but configuration files remain on the system. Therefore to remove a package and it’s configuration files, we will have to use purge.

#### apt-get clean

To delete downloaded packages (.deb) already installed (and no longer needed) and it would free up more space by cleaning the cache.

#### apt-get autoclean

To remove all stored archives in your cache for packages that can not be downloaded anymore (thus packages that are no longer in the repository or that have a newer version in the repository).

#### apt-get check

Will check the the currently installed packages for any broken installation.

### **What is apt-cache?**

The apt-cache command line tool is used for searching apt software package cache. In simple words, this tool is used to search software packages, collects information of packages and also used to search for what available packages are ready for installation on Debian or Ubuntu based systems. APTs cached files are located in`/var/cache/apt/archives/`

Before start using apt-cache it is good to do apt-get check first:

Because this command builds new cache by comparing the current state with the state of packages as listed in repositories. One the apt-cache has been built we can query it.

**apt-cache search**

Find Out Package Name and Description of Software (doesn't require root access because it is querying the cache)

**apt-cache show**

Check information of package along with it short description say (version number, check sums, size, installed size, category etc).

**apt-cache showpkg**

‘showpkg‘ sub command to check the dependencies for particular software packages. whether those dependencies packages are installed or not.

**apt-cache depends** and **apt-cache rdepends** allow us to query dependencies.

See telnet dependencies and see which other packages depends on telnet.

use **apt-cache stat** to show statistics of installed packages on your computer.

> dselect
>
> dselect is a front-end to dpkg that is used to manage software packages in Debian and Debian-based Linux distributions. You can use dselect to install packages on your system from the APT archives defined in /etc/apt/sources.list, review the already installed packages, uninstall and upgrade packages.
>
> ![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGafRaYpBqkwvB0KM%252Fdebpack-dselect.png%3Fgeneration%3D1569999732036480%26alt%3Dmedia&width=300&dpr=4&quality=100&sign=23fbc8f8&sv=2)

## aptitude

aptitude is another high-level package manager for Debian-based systems, and can be used to perform management tasks (installing, upgrading, and removing packages, also handling dependency resolution automatically) in a fast and easy way. It provides the same functionality as apt-get and additional ones, such as offering access to several versions of a package.

You might need to install aptitude first ( `apt-get install aptitude` )

As an example lets search and get info about netcat using aptitude:

**Differences Between APT and Aptitude**

Apart from main difference being that Aptitude is a high-level package manager while APT is lower-level package manager which can be used by other higher-level package managers, other main highlights that separate these two package managers are:

* Aptitude is vaster in functionality than apt-get and integrates functionalities of apt-get and its other variants including apt-cache and apt-mark.
* While apt-get lacks UI, Aptitude has a text-only and interactive UI

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGafZL4LtkOAUVHab%252Fdebpack-aptitude.jpg%3Fgeneration%3D1569999724628668%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=c60071b2&sv=2)

* Aptitude has a better package management than apt-get:

1.While removing any installed package, Aptitude will automatically remove unused packages, while apt-get would need user to explicitly specify this by either adding additional option of ‘—auto-remove’ or specifying ‘apt-get autoremove’.

2.To investigate further as to why certain action is getting blocked or why or why-not a certain action should be taken, Aptitude offers 'why' and ‘why-not’ commands.

3.While apt-get would probably die-out in case of conflicting action regarding installation or removal of package with a message, Aptitude can suggest possible measures to remove that conflict.

### Summary

Debian Family System

**dpkg:**

* low-level or underlying packet manager
* Unpacks, installs, removes and build packages
* It can't download or resolve dependencies

**Advance Package Tool (apt) :**

* Build on top of dpkg (depends on it)
* works with groups of packages
* It can automatically download and install packages to figure out and resolve dependencies.
* Tts native user interface is through the apt-get and apt-cache commands
* Usually a user interface is created on top of it for an specific distro (SW update GUIs are an example of this)

.

.

.

sources:

<http://www.pepedocs.com/notes?tid=linux&nid=lfs101x>

<https://www.dennyzhang.com/linux_package_mgmt>

<https://www.networkworld.com/article/3305810/linux/how-to-list-repositories-on-linux.html>

<https://help.ubuntu.com/lts/serverguide/dpkg.html.en>

<https://www.tecmint.com/dpkg-command-examples/>

<https://geek-university.com/linux/dselect/>( like dpkg but has UI)

<https://unix.stackexchange.com/questions/20504/the-difference-between-deb-versus-deb-src-in-sources-list>

<https://askubuntu.com/questions/58364/whats-the-difference-between-multiverse-universe-restricted-and-main>

<https://www.tecmint.com/apt-advanced-package-command-examples-in-ubuntu/>

<https://wiki.debian.org/debconf>

<https://www.tecmint.com/useful-basic-commands-of-apt-get-and-apt-cache-for-package-management/>

<https://www.tecmint.com/apt-advanced-package-command-examples-in-ubuntu/>

<https://askubuntu.com/questions/32191/how-do-i-remove-cached-deb-files>

<https://askubuntu.com/questions/81585/what-is-dist-upgrade-and-why-does-it-upgrade-more-than-upgrade>

<https://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do>

<https://www.tecmint.com/linux-package-management/>

<https://www.tecmint.com/difference-between-apt-and-aptitude/>

Copy

# 102.5. Use RPM and YUM package management

## **102.5 Use RPM and YUM package management**

**Weight:** 3

**Description:** Candidates should be able to perform package management using RPM and YUM tools.

**Key Knowledge Areas:**

* Install, re-install, upgrade and remove packages using RPM and YUM
* Obtain information on RPM packages such as version, status, dependencies, integrity and signatures
* Determine what files a package provides, as well as find which package a specific file comes from

**Terms and Utilities:**

* rpm
* rpm2cpio
* /etc/yum.conf
* /etc/yum.repos.d/
* yum
* yumdownloader

In this lesson we learn how to work with packages in RedHat Distributions. If you are not familiar with Package and package Manager concepts in linux please study first part of previous lesson.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_XYZ2nRzxHIkUCM%252Fredpack-red.jpg%3Fgeneration%3D1569999731651356%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=6f8487cc&sv=2)

## rpm

RPM (Red Hat Package Manager) is a powerful Package Manager, which can be used to build, install, query, verify, update, and erase individual software packages.

A package consists of an archive of files and meta-data used to install and erase the archive files. The meta-data includes helper scripts, file attributes, and descriptive information about the package.

Packages come in two varieties: **binary packages**, used to encapsulate software to be installed, and **source packages**, containing the source code and recipe necessary to produce binary packages. RPM is the only way to install packages under Linux systems, if you’ve installed packages using source code, then rpm won’t manage it.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_XaoL_zDO0b05J-%252Fredpack-rpmbox.jpg%3Fgeneration%3D1569999731593028%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=5f5df4ce&sv=2)

RPM deals with .rpm files, which contains the actual information about the packages such as: what it is, from where it comes, dependencies info, version info etc.

### Where to find RPM packages

list of rpm sites, where we can find and download all RPM packages:

* <http://rpmfind.net>
* <http://www.redhat.com>
* <http://freshrpms.net/>
* <http://rpm.pbone.net/>

RPM keeps the information of all the installed packages under /var/lib/rpm database.

They are all binary files, try `cat Basenames` to see.

There are five basic modes for RPM command:

* Install : It is used to install any RPM package.
* Remove : It is used to erase, remove or un-install any RPM package.
* Upgrade : It is used to update the existing RPM package.
* Verify : It is used to verify an RPM packages.
* Query : It is used query any RPM package.

#### Install an RPM Package

-i is used for installing an rpm software package

`-v` verbose for a nicer display
,`-h` print hash marks as the package archive is unpacked.

#### Check an Installed RPM Package

`-q` option query a package:

#### List all files of an installed RPM package

Use `-ql` **(query list)** with rpm command:

#### Query a file that belongs which RPM Package

`-qf` **(query file)** option help us to find out which package belongs to a file.

#### Query a Information of Installed RPM Package

`-qi` **(query info)** option will print the available information of the installed package.

#### Get the Information of RPM Package Before Installing

`-qip` **(query info package)** will print the information of a package , as the package has not been installed there is nothing to read by rpm in its data base, so we need to give full name of the package and it would provide required information directly from rpm package:

`-p` is used to query information from rpm package. We can omit -p and use Package name instead `rpm -qi htop` .

#### check dependencies of RPM Package before Installing

Use `-qpR` options to do a dependency check before installing or upgrading a package

`-R` List capabilities on which this package depends. we can easily use `rpm -qR PackageName` to query an installed package.

**Query configuration file of Installed RPM Packae**

`-qc` **(query configuration file)** will query an installed package for its configuration files, if it has any:

If the package is not installed use `-qpc` instead to query a rpm package.

#### Query documentation of Installed RPM Package

`-qdf`**(query document file)** gives a list of available documentation of an installed package:

#### Verify a installed Package

`-V`**(verify)** verifies a package:

No news is good news.When verifying a package, RPM produces output only if there is a verification failure. When a file fails verification, the format of the output is a bit cryptic, but it packs all the information you need into one line per file. Here is the format: `SM5DLUGT c`  `. As an example:`

Where:

* **S** is the file size.
* **M** is the file's mode.
* **5** is the MD5 checksum of the file.
* **D** is the file's major and minor numbers.
* **L** is the file's symbolic link contents.
* **U** is owner of the file.
* **G** is the file's group.
* **T** is the modification time of the file.
* **c** appears only if the file is a configuration file. This is handy for quickly identifying config files, as they are very likely to change, and therefore, very unlikely to verify successfully.
* is the file that failed verification. The complete path is listed to make it easy to find.

#### Verify all RPM Packages

Use `-Va`**(Verify all)** to verify all the installed rpm packages.

use `rpm -Vac` to just verify configuration files.There would be some common system script which are routinely changed.

#### Verify a RPM Package

Verifying a package compares information of installed files of the package against the rpm database.

The`-Vp` **(verify package)** is used to verify a package.

#### List all Installed RPM Packages

`-qa` **(query all)** option, will list all the installed rpm packages.

use `--last` option to list recently installed RPM Packages.

#### Upgrade a RPM Package

`-U` upgrades or installs the package currently installed to a newer version. This is the same as install, except all other version(s) of the package are removed after the new package is installed.

One of the major advantages of using this option is that it will not only upgrade the latest version of any package, but it will also maintain the backup of the older package so that in case if the newer upgraded package does not run the previously installed package can be used again.(via rpm --oldpackage switch or using yum downgrade )

> **rpm -ivh vs rpm -Uvh**
>
> rpm -ivh just installs a package and if the package is already installed it won't do any things, but rpm -Uvh installs it, even if it exists.
>
> Also rpm -ivh might cause having multiple version of a package at the same time but by using rpm -Uvh we are sure that we just have the latest version.

-F will upgrade packages, but only ones for which an earlier version is installed.( means upgrade if installed other wise do noting)

#### Remove a RPM Package

`-e` **(erase)** option is used to remove package (add `v` or `vv` for more verbosity):

rpm take care of dependencies while removing a package and does not remove package dependencies. on the other hand if a package is required by other pacakage(d) rpm avoid removing that.The `–nodeps` **(Do not check dependencies)** option **forcefully** remove the rpm package from the system. But keep in mind removing particular package may break other working applications.

note:If you've made changes to a configuration file that was originally installed by RPM, your changes won't be lost if you erase the package.

What you can do is just run "rpm -qc packageName" which will show you which configuration files were installed on your system by an rpm. When you have uninstalled the rpm, you can search on your system if any of the files or their backups remain on your system and remove them manually.

### rpm2cpio

From time to time, we might find it necessary to extract one or more files from a package file. One way to do this would be to:

1. Install the package
2. Make a copy of the file(s) you need
3. Erase the package

An easier way would be to use **rpm2cpio**.

**What Files Are In a RPM Package?**

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_XpRjjjLE_pnIu0%252Fredpack-rpm.jpg%3Fgeneration%3D1569999731572786%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=bb51005b&sv=2)

A rpm package is consist of some of files and directories which has been archived in cpio format, in addition some descriptions and dependencies have been added to that.

**What does rpm2cpio do?**

As the name implies, rpm2cpio takes an RPM package file and converts it to a cpio archive. next we need to open cpio archive in order to have orginal file structure.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAG_XrpHqIbCqNUG0J%252Fredpack-rpm2cpio.jpg%3Fgeneration%3D1569999731585061%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=d71db376&sv=2)

In this case, the cpio options`-i` Extract one or more files from an archive, `-v`verboe, list the files processed, and `-d`Create leading directories where needed.(We will talk about cpio in next courses)

rpm2cpio takes only only one argument, and even that's optional! The optional argument is the name of the package file to be converted. (If there is no filename specified on the command line, rpm2cpio will simply read from standard input and convert that to a cpio archive.)

While there's nothing wrong with using rpm2cpio to actually create a cpio archive file, it's takes a few more steps and uses a bit more disk space than is strictly necessary. A somewhat cleaner approach would be to pipe rpm2cpio's output directly into cpio:

we used the`-t` option to direct cpio to produce a "table of contents" of the archive created by rpm2cpio. This can make it much easier to get the right filename and path when you want to extract a file. An easier way to exctract would be `rpm2cpio package.rpm | cpio id .`

Warning! Becarefull when removing extracted package (usr vs /usr)

## YUM

The YUM (Yellowdog Updater Modified) is an open-source command-line package-management utility for Linux operating systems using the RPM Package Manager. Yum allows automatic updates, package and dependency management, on RPM-based distributions.

As a high-level tool,like the Advanced Packaging Tool (APT) from Debian, yum works with software repositories (collections of packages), which can be accessed locally or over a network connection.

Yum is implemented as libraries in the Python programming language, with a small set of programs that provide a command-line interface. GUI-based wrappers such as **yumex** also exist.

### /etc/yum.conf

The configuration file for yum and related utilities is located at /etc/yum.conf.

This file contains one mandatory [main] section, which allows us to set Yum options that have global effect, and can also contain one or more [repository] sections, which allow us to set repository-specific options. However, it is recommended to define individual repositories in new or existing .repo files in the /etc/yum.repos.d/ directory.

### /etc/yum.repos.d

YUM Repository configuration files are stored in /etc/yum.repos.d directory. It contains several .repo files.

Lets take a look at CentOS-Base.repo file:

Repository configuration files tell yum information about the actual repository (where package files are physically located). While there are a number of optional elements, each .repo file is required to have:

* **Repository ID** - A one word unique repository ID e.g. [localrepo].
* **Name** - A human readable name for the repository e.g. name=Awesome Local Repo
* M**irrorList** : A mirror list is a list of URLs where Package repositories are stored/present.
* **Baseurl** - A URL to the repodata directory (where the actual files are kept). file://path, ftp://link, <http://link>, and <https://link> addresses are all valid options.
* **Enabled** - Whether or not to enable the repository for use when performing updates and installs e.g. enabled=1 (1 means "use this repository", 0 defines "do not use this repository").
* **Gpgcheck** - Enable/disable GPG signature checking (example: gpgcheck=1)
* **Gpgkey** - URL to the GPG key (example: gpgkey=[http://mirror.cisp.com/CentOS/6/os/i386/RPM-GPG-KEY-CentOS-6\](http://mirror.cisp.com/CentOS/6/os/i386/RPM-GPG-KEY-CentOS-6%29\)

GPG is a digital signature check , which is used to verify the package is modified in between your downloads or after making the package, It help to verify the that you are installing the correct package with out any modification from 3 party or a hacker.

YUM can use numerous third party repositories to install packages automatically by resolving their dependencies issues.

### List Enabled Yum Repositories

`yum repolist` list all enabled Yum repositories in your system:

To list all Enabled and Disabled Yum Repositories use `yum repolist all` command.

### Install a Package with YUM

We can install new software on Red Hat/CentOS Linux with `yum install packagename` command from console.

Running this command first checks for existing YUM Repository configuration files in /etc/yum.repos.d/ directory. It reads each YUM Repository configuration file to get the information required to download and install new software, resolves software dependencies and installs the required RPM package files.

use `-y` option if you do not like to be asked for confimation. If you have a rpm package use `yum localinstall abc.rpm` .

### Removing a Package with YUM

`yum remove packagename` remove a package completely with their all dependencies.

Same way the remove command will ask confirmation before removing a package. To disable it just add option `-y` .

### Search for a Package using YUM

Use `yum search` function to search all the available packages to match the name of the package you specified.

### Get Information of a Package using YUM

With`yum info packagename` we can get information of a package before installing or an installed package:

### Get information about dependencies of a package

Use yum deplist command to know about dependencies of a package which would be installed on our system:

`yum install`automatically installs all of them.

### Yum Provides Function

`yum provide` finds packages that provide the queried file:

also we can use`yum whatprovide /*filename` instead.

### List all Available Packages

`yum list` list all the available packages in the Yum database.

### List all Installed Packages using YUM

### Working with yum **Cache**

By default, yum deletes downloaded data files when they are no longer needed after a successful operation. This minimizes the amount of storage space that yum uses. However, we can enable caching, so that the package files downloaded by yum stay in cache directories. By using cached data, you can carry out certain operations without a network connection, we can also copy packages stored in the caches and reuse them elsewhere.

Yum stores temporary files in the`/var/cache/yum/$basearch/$releasever/`directory,

Each configured repository has one subdirectory.T o change the default cache location, modify the **cachedir** option in the **[main]** section of the `/etc/yum.conf`configuration file.

**Enabling the cache**

To retain the cache of packages after a successful installation, we can enable the cacheediting **keppcache = 1** in the [main] section of`/etc/yum.conf`.

To download and make usable all the metadata for the currently enabled yum repositories, use `yum makecache` command.It makes sure that the cache is fully up to date with all metadata.This make sure that the cache is fully up to date with all metadata. To set the time after which the metadata will expire, use the **metadata-expire** setting in`/etc/yum.conf`.

**Using yum in Cache-only Mode**

To carry out a yum command without a network connection, add the `-C` (not `-c` )or `--cacheonly` command-line option. With this option, yum proceeds without checking any network repositories, and uses only cached files. In this mode, yum may only install packages that have been downloaded and cached by a previous operation.

**clearing the yum caches**

It is often useful to remove entries accumulated in the `/var/cache/yum/` directory. If we remove a package from the cache, we do not affect the copy of the software installed on our system. To remove all entries for currently enabled repositories from the cache, run `yum clean all` as a root.

### Check for Available Updates using Yum

use `yum check-update` To find how many of installed packages on our system have updates available:

### Update System using Yum

yum update keep our system up-to-date with all security and binary package updates

### Updating a Package using YUM

`yum update packagename`will update a package and automatically resolves all dependencies issues and install them.

If you have a rpm package you can use `yum localupdate abc.rpm` .

> ### YUM update vs YUM upgrade
>
> `yum upgrade` and `yum update` will perform the same function that update to the latest current version of package.
>
> `yum upgrade` **forces** the removal of obsolete packages, while `yum update` may or may not also do this. The removal of obsolete packages can be risky, as it may remove packages that you use.
> This makes `yum update` the safer option.
>
> note: The behaviour might be different based on your distribution and version.

### Working with Group Packages

In Linux, number of packages are bundled to particular group , called **Group Packages**. Instead of working with individual packages with yum, we can work particular group that will install/remove/update all the related packages that belongs to the group.

## YUM Shell

Yum utility provides a custom shell where you can execute multiple commands.

## yumdownloader

How do I use yum to download a package without installing it? There are multiple ways in which you can download a yum package without installing it. The 2 most commonly used methods are described here in the post.

1. using the “downloadonly” plugin for yum
2. using “yumdownloader” utility.

**Method 1** : using the “**downloadonly**” plugin for yum:

First install the package including “downloadonly” plugin:

syntax:

If you do not use `--downloaddir` option, it would be saved in `/var/cache/yum/ in rhel-{arch}-channel/packages directory`.

example:

**Method 2** : using the “**yumdownloader**” utility

First install the yum-utils package:

syntax:

example:

try`yumdownloader --help` to see some of usefull switches such as :

the `--resolve` switch is usefull inorder to download a package ant its dependencies and lets us to use them in other system.

### to view history of Yum commands (update, install, remove)

We can either use `yum history` command :

or see yum log file in `/var/log/yum` directory:

### Summary

Fedora Family System:

* **Red Hat Package Manager (rpm)**:

  + low-level or underlying packet manager
* **Yellowdog Updater (yum)**:

  + The high-level package manager differs between distribution but yum is commonly used
* **Dandified Yum (dnf)**:

  + It is the next-generation version of yum

.

.

.

sources:

<http://www.pepedocs.com/notes?tid=linux&nid=lfs101x#ch6>

<https://linux.die.net/man/8/rpm>

<https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/>

<http://ftp.rpm.org/max-rpm/s1-rpm-verify-output.html>(rpm -V)

<https://serverfault.com/questions/747089/whats-the-diff-between-rpm-u-and-rpm-f?rq=1>

<http://ftp.rpm.org/max-rpm/s1-rpm-erase-and-config-files.html>

<https://www.linuxquestions.org/questions/linux-software-2/can-rpm-remove-config-files-during-uninstall-537423/>

<http://ftp.rpm.org/max-rpm/s1-rpm-miscellania-rpm2cpio.html>

<https://blog.packagecloud.io/eng/2015/10/13/inspect-extract-contents-rpm-packages/>(what is inside rmp)

<https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/>

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-configuring_yum_and_yum_repositories>(yum.conf)

<https://www.quora.com/What-is-gpgcheck-in-a-yum-configuration-file-in-Rhel>

<https://www.digitalocean.com/community/tutorials/how-to-set-up-and-use-yum-repositories-on-a-centos-6-vps>

<https://superuser.com/questions/1252958/explanation-of-the-contents-inside-folder-etc-yum-repos-d>

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sec-working_with_yum_cache>( working with yum cache)

<https://www.hivelocity.net/kb/how-to-clear-the-yum-cache/> (clear cache)

<https://access.redhat.com/solutions/10154>

<https://www.thegeekdiary.com/how-to-use-yum-downloadonly-to-download-a-package-without-installing-it/>

.

Copy

# 103.1. Work on the command line

### **103.1 Work on the command line**

**Weight**: 4

**Description:**Candidates should be able to interact with shells and commands using the command line. The objective assumes the Bash shell.

**Key Knowledge Areas:**

* Use single shell commands and one line command sequences to perform basic tasks on the command line
* Use and modify the shell environment including defining, referencing and exporting environment variables
* Use and edit command history
* Invoke commands inside and outside the defined path

**Terms and Utilities:**

* bash
* echo
* env
* export
* pwd
* set
* unset
* man
* uname
* history
* .bash\_history

**What's A "Terminal?"**

It's a program called a terminal emulator. This is a program that opens a window and lets you interact with the **shell**. There are a bunch of different terminal emulators we can use. Most Linux distributions supply several, such as: gnome-terminal, konsole, xterm, **... ,** It is also called Console.

**What is "The Shell"?**

Simply put, the shell is a program that takes commands from the keyboard and gives them to the operating system to perform. In the old days, it was the only user interface available on a Unix-like system such as Linux. Nowadays, we have graphical user interfaces (GUIs) in addition to command line interfaces (CLIs) such as the shell.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbWkyCRYcuNGU6VA%252Fcommandintro-shell.jpg%3Fgeneration%3D1569999770421965%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=e939fb5d&sv=2)

**What is The "bash"?**

On most Linux systems a program called **bash acts as the shell** program. bash stands for **Bourne Again SHell**, an enhanced version of the original Unix shell program, sh, written by Steve Bourne

Besides, There are other shell programs that can be installed in a Linux system. These include: ksh, tcsh and zsh.

note: Historically the original /bin/sh Bourne shell would use **$** as the normal prompt and **#** for the root user prompt This made it pretty easy to tell if you were running as superuser or not.

**Standard Input, Standard Output and Standard Error**

In general, a command (a program):

* Gets data to process from standard input or **stdin** (default: keyboard).
* Returns processed data to standard output or **stdout** (default: screen).
* If program execution causes errors, error messages are sent to standard error or **stderr** (default: screen).

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbWvUfOCFqTekssK%252Fcommandintro-InputOutput.jpg%3Fgeneration%3D1569999770256219%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=4c0ce014&sv=2)

### echo

echo is one of the most commonly and widely used built-in command for Linux bash and C shells, that typically used in scripting language and batch files to display a line of text/string on standard output or a file.

The syntax for echo is: `echo [option(s)] [string(s)]`

example : Input a line of text and display on standard output:

The echo command has a couple of options. Normally, echo will append a trailing new line character to the output. Use the`-n`option to suppress this:

#### Special Characters or Meta Characters

What makes a character special? If it has a meaning beyond its literal meaning, a meta-meaning, then we refer to it as a special character or metacharacters like : `` | & ; ( ) < > [ ] { } * ! ? ` ' " $ \ / # ``

**pound sign (#)**

Everything written after a pound sign (#) is ignored by the shell. This is useful to write a shell comment, but has no influence on the command execution or shell expansion.

**end of line backslash \**

Lines ending in a backslash are continued on the next line. The shell does not interpret the newline character and will wait on shell expansion and execution of the command line until a newline without backslash is encountered.

**escaping special characters**

The backslash character enables the use of control characters, but without the shell interpreting it, this is called **escaping characters**.

**Double quotes " "**

Enclosing characters in double quotes (`"`) preserves the literal value of all characters within the quotes, [*with the exception of* `$`*,* `` ` ``*,* `\`*, and, when history expansion is enabled,* `!`  .*The characters* `$` *and* `` ` `` *retain their special meaning within double quotes*`].`

Lets take a look at other options of echo command:

Use the`-e`option to enable certain backslash **escaped characters** to have special meaning.

Escape sequence

Function

\a

Alert (bell)

\b

Backspace

\c

Suppress trailing newline (same function as -n option)

\f

Form feed (clear the screen on a video display)

\n

New line

\r

Carriage return

\t

Horizontal tab

\v

vertical tab

Some examples:

One of echo command usage is getting variable values with `echo $VARIABLENAME` command. We will see that.

### **Control Operators**

Certain metacharacters or pairs of metacharacters also serve as control operators:`|| && & ; ;; | ()`

Some of these control operators allow you to create sequences or lists of commands.

#### Linux command chaining

Sometimes we would want to run multiple commands in succession or simultaneously. This allows us to automate a process that include several commands that may or may not depend on the result of the previous command.

**Linux command chaining** is the method of combining several different commands such that each of them can execute in succession based on the operator that separate them. The important part of chaining is the operators that we use to combine them. These operators determine how the commands execute.

Lets take a look at some of operators that are used mostly to combine different commands :

**Semi-Colon** (**;**) : The succeeding commands will execute regardless of the exit status of the command that precedes it.

**Logical AND** (**&&**) : This command that follows this operator will execute only if the preceding command executes successfully.

**Logical OR** (**||**) : The command that follows will execute only if the preceding command fails.

## Environment Variables

Environment Variables are some special variables that are defined in shell and are needed by programs while execution. They can be system defined or user defined.

System defined variables are those which are set by system and are used by system level programs.

The whole concept of setting and un-setting environment variables revolves around some set of files and few commands and different shells.

an environment variable can be in three types:

**1. Local Environment Variable** :One defined for the current session. These environment variables last only till the current session, be it remote login session, or local terminal session. These variables are not specified in any configuration files and are created, and removed by using a special set of commands.

**2. User Environment Variable** : These are the variables which are defined for a particular user and are loaded every time a user logs in using a local terminal session or that user is logged in using remote login session. These variables are typically set in and loaded from some configuration files which are present in user’s home directory.

**3. System wide Environment Variables** :These are the environment variables which are available system-wide, i.e. for all the users present on that system. These variables are present in system-wide configuration files present in /etc directories and files.These variables are loaded every time system is powered on and logged in either locally or remotely by any user.

### env

By default, "env" command lists all the current environment variables.

These varibales make working with shell easier. Some of most important ones are:

* **HOSTNAME**:The name of the your computer.
* **SHELL**: This describes the shell that will be interpreting any commands you type in. In most cases, this will be bash by default, but other values can be set if you prefer other options.
* **TERM**: This specifies the type of terminal to emulate when running the shell. Different hardware terminals can be emulated for different operating requirements. We usually won't need to worry about this though.
* **USER**: The current logged in user.
* **LS\_COLORS**: This defines color codes that are used to optionally add colored output to the ls command. This is used to distinguish different file types and provide more info to the user at a glance.
* **MAIL**: The path to the current user's mailbox.
* **PATH**: A list of directories that the system will check when looking for commands. When a user types in a command, the system will check directories in this order for the executable.

> For running other scripts or commands we can add them to path, or use full path or relative path (. and ..)
>
> PATH=$PATH:/tmp/mybin

* **PWD**: The current working directory.

> We use pwd command to see that:

* **LANG**: The current language and localization settings, including character encoding.
* **HOME**: The current user's home directory.
* **\_**: The most recent previously executed command.
* **OLDPWD**: The previous working directory. This is kept by the shell in order to switch back to your previous directory by running cd -.

The exit code of the previous command is stored in the shell variable $?. Actually $? is a shell parameter and not a variable, since you cannot assign a value to $?.

`[root@centos7-1 ~]# touch my.txt`

`[root@centos7-1 ~]# echo $?`

`0`

To see the value of a variable use `echo $VARIABLENAME` :

To set a Local Variable we create a local variable VAR1 and set it to any value( Historically it is recommended to use upper case for variables but you are free to use what ever case you want):

By default variables are local, so What will happen to our Variable if we start a new sub shell ?

It shows nothing. Why?

**Child vs Parent process**

Any process can be a parent and child process at the same time. The only exception is the init process, which is always marked with PID ( process ID ) 1. Therefore, init is a parent of all processes running on your Linux system.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbX5JIK655nKuHdo%252Fcommandintro-parentchild.jpg%3Fgeneration%3D1569999770261843%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=3063ea34&sv=2)

Any process created will normally have a parent process from which it was created and will be considered as a child of this parent process.
`echo $$` print a PID for a current shell

When creating a new child process (a sub shell in our example) an export command simply ensures that any exported variables in the parent process are available in the child process.

We can terminate a shell using the exit command or simply press ctrl+d keys.

**( )** : parentheses really put the command in a subshell. try(exit)

### export

export command is one of the bash shell builtin commands, marks an environment variable to be exported to child-processes, so that the child inherits them.

Syntax:`export [-fn] [name[=value] ...] or export -p`

The export command is fairly simple to use as it has straightforward syntax with only three available command options.

Following our example:

### set

`set`is a shell built-in that (If no options or arguments are supplied) displays all shell variables, not only the environment ones, and also shell functions, which is what you are seeing at the end of the list.

> **set vs env**
>
> Long story short: set can see shell-local variables, env cannot.
>
> As we have mentioned, shells can have variables of 2 types: locals, which are only accessible from the current shell, and (exported) environment variables, which are passed on to every executed program.
>
> Since set is a built-in shell command, it also sees sees shell-local variables (including shell functions). env on the other hand is an independent executable; it only sees the variables that the shell passes to it, or environment variables

In bash like in any Bourne-like shell, set is the command to set options (shell configuration settings like -f, -C, -o noclobber...) and positional parameters ($1, $2...).

Use - and + signs for enabling and disbaling options.Try`help set | less` .

To see the current shell options use `echo $-` :

For example -u treat unset variables as an error when substituting:

We can use `set -o` without any option to get the current state of shell options :

set +o turns off specified option and set -o turns it on .For example lets disable and enable History Storing with -o option:

One of important options you might be asked for in the exam is noclobber, The noclobber option prevents you from overwriting existing files with the > operator (Discussed in next courses).

set is not for setting variables. Do not make mistake!

Set has lots of options which are used to change bash behaviour.

### unset

unset command is used to unset any local environment variable temporarily:

So `set` is not set, but `unset` is unset.

We can also use `env VARNAME=VALUE` and `env -u VARNAME` to set and unset a variable.

## Understanding Bash History

History of all commands which are executed by all users are stored.History is maintained both in ram and in a file*.bash\_history.* History which is maintained in ram, manipulated with the command`history`and environment variables. It is important to note that the history contained in ram is only written after a user logs out of his or her session.

### history

history shows the current content of Bash's history list in memory for the current session.

How many lines are stored in RAM version of History list? It is defined by HISTSIZE variable.

* **HISTSIZE** : This variable contains the maximum number of lines that be contained in the in-ram version of history.

and that would be 1000 lines! to see just 5 lines for example use`history 5` .

**Repeat previous command quickly(3 methods)**

1. Use the **up arrow** to view the previous command and press enter to execute it.
2. **Type !! and press enter** from the command line.(or **!!number** )
3. **Press Control+P** will display the previous command, press enter to execute it

**Search the history(3 methods)**

1. **Control+R:** Press Control+R and type the keyword.
2. **!string** Refers to the most recent command starting with string.
3. **!?string?** Refers to the most recent command containing string (the ending ? is optional).

**Clear all the previous history :** Use history -c option.

### **~/.bash\_history**

When user closes shell , Bash will save its history list to the disk by appending the contained entries to his/her **~/.bash\_history** hidden file. **~/.bash\_history** is controlled by some variables:

* **HISTFILE** This variable contains the location of the history file. When bash is logged out of, the contents of the history command will be written to this file.
* **HISTFILESIZE** The variable contains the maximum number of lines that may be in the history file. When bash writes to the history file, the oldest commands that go over this maximum number will be deleted.

  it acts the same as HISTSIZE.
* **HISTCONTROL** This variable contains instructions for what should be ignored when added to the history file. has four settings:

To see the **.bash\_history** hidden file we should use ls with `-a` switch:

What about other users?

As an instance lets find out what user1 has done:

He/she has done nothing:). **.bash\_history** by default keeps 500 or 1000 of command which has been used.So we can go back to some thing we have done long time ago. history -c does not clear that and it remains after user log off, so if you don't like it you should remove it.

### uname

uname command without any switch will print system information :

Its syntax is like `uname [OPTION] ...` .For example`-a, --all`Prints all information:

If -a (--all) is specified, the information is printed in the following order of individual options:

Processor information (-p) and Hardware-Platform(-i) are omitted if they are unknown.

### man

In Unix-like operating systems, a man page (in full manual page) is a documentation for a terminal-based program/tool/utility (commonly known as a command). It contains:

* **the name of the command**
* **syntax for using it**
* **a description**
* **options available**
* **author**
* **copyright**
* **related commands and ... .**

To read a manual page for a Unix command, a user can type:

For example try `man man` :

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXRj2sEV-XoS0LU%252Fcommandintro-manman.jpg%3Fgeneration%3D1569999770424556%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=654971ec&sv=2)

By default, man typically uses a terminal pager program such as **more** or **less** to display its output.

The manual is generally split into eight or nine numbered sections, organized as follows :

1. **Executable programs or shell commands**
2. **System calls** (functions provided by the kernel)
3. **Library calls** (functions within program libraries)
4. **Special files** (usually found in /dev)
5. **File formats and conventions** eg /etc/passwd
6. **Games**
7. **Miscellaneous** (including macro packages and conventions), e.g. man(7), groff(7)
8. **System administration commands** (usually only for root)
9. **Kernel routines** [Non standard]

To make man display manual page from specific sections use `man [section-num] [command/tool name]` :

man will search for the desired manual pages within the index database caches. So there is no need to remember section numbers for manual entries .

#### mandb

mandb is used to initialise or manually update index database caches
that are usually maintained by man. The caches contain information
relevant to the current state of the manual page system and the
information stored within them is used by the man-db utilities to
enhance their speed and functionality.

the cache consistency check can be slow on systems with many manual pages installed, so mandb is not performed by default, and system administrators may wish to run mandb every week or so to keep the database caches fresh.

**Most useful man command options:**

`-f, --whatis`Display a short description from the manual page

`-w, --where, --location` Don't actually display the manual pages, but do print of the source off files

`-k, --apropos` Equivalent to apropos. Search the short manual page descriptions for keywords and display any matches.

### apropos

apropos command is used to search and display a short man page description of a command/program as follows.

That is all!

.

.

.

sources:

<http://linuxcommand.org/lc3_lts0010.php>

<https://stackoverflow.com/questions/6697753/difference-between-single-and-double-quotes-in-bash>

<https://www.w3resource.com/linux-system-administration/control-operators.php>

<https://www.tecmint.com/set-unset-environment-variables-in-linux/>

<https://unix.stackexchange.com/questions/291729/why-is-the-default-symbol-for-a-user-shell-and-the-default-symbol-for-a-root>

<http://labor-liber.org/en/gnu-linux/introduction/index.php?diapo=input_output>

<http://www.lostsaloon.com/technology/how-to-chain-commands-in-linux-command-line-with-examples/>

<https://www.tecmint.com/chaining-operators-in-linux-with-practical-examples/>

<https://www.tecmint.com/echo-command-in-linux/>

[https://developer.ibm.com/tutorials/l-lpic1-103-1/](https://legacy.gitbook.com/book/borosan/lpic1-exam-guide/edit#)

<https://ss64.com/bash/syntax-quoting.html>

<https://linuxconfig.org/learning-linux-commands-export>

<https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps>

<http://www.symkat.com/understanding-bash-history>

<https://www.tecmint.com/history-command-examples/>

<https://www.thegeekstuff.com/2008/08/15-examples-to-master-linux-command-line-history>

<https://www.computerhope.com/unix/uuname.htm>

<https://en.wikipedia.org/wiki/Man_page>

<https://www.tecmint.com/view-colored-man-pages-in-linux/>

<https://www.techonthenet.com/linux/commands/man.php>

<http://man7.org/linux/man-pages/man8/mandb.8.html>

<https://bash.cyberciti.biz/guide/Shopt>

.

Copy

# 103.2. Process text streams using filters

## **103.2 Process text streams using filters**

**Weight:**3

**Description:** Candidates should be able to apply filters to text streams.

**Key Knowledge Areas:**

Send text files and output streams through text utility filters to modify the output using standard UNIX commands found in the GNU textutils package

**Terms and Utilities:**

* cat
* cut
* expand
* fmt
* head
* join
* less
* nl
* od
* paste
* pr
* sed
* sort
* split
* tail
* tr
* unexpand
* uniq
* wc

Everything in Linux revolves around streams of data—particularly text streams.

### streams

A stream is nothing more than a sequence of bytes that is passed from one file, device, or program to another.

Input and output in the Linux environment is distributed across three streams (which are in fact special files).

These streams are:

* **standard input stream (stdin)**, which provides input to commands.
* **standard output stream (stdout)**, which displays output from commands.
* **standard error stream (stderr)**, which displays error output from commands.

The streams are also numbered: **stdin (0)** ,**stdout (1)**, **stderr (2)**.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbWq0Q-rmaY9Lfzl%252Fprocesstxt-streams.jpg%3Fgeneration%3D1569999734698450%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=c40b995f&sv=2)

### piping with |

Piping is a mechanism for sending data from one program to another. The operator we use is ( | ) (found above the backslash `\` key on most keyboards). What this operator does is feed the output from the program on the left as input to the program on the right.

Either command can have options or arguments. We can also use | to redirect the output of the second command in the pipeline to a third command, and so on.

Constructing long pipelines of commands that each have limited capability is a common Linux and UNIX way of accomplishing tasks.

### Redirection

Linux includes redirection commands for each stream.We can use `>` in order to redirect output stream (mostly to a file).

> "|" vs ">"
>
> The difference between > (redirection operator) and | (pipeline operator) is that while the > connects a command with a file, the | connects the output of a command with another command.

### Text filtering

Text filtering is the process of taking an input stream of text and performing some conversion on the text before sending it to an output stream.

## cat

The **cat** (short for “**concatenate**“) command is one of the most frequently used command in Linux/Unix like operating systems. cat command allows us to create single or multiple files, view contain of file, concatenate files and redirect output in terminal or files.

Simplest usage of cat is displaying the content of a file:

is can show contents of Multiple Files :

The cat command also used to concatenate number of files together:

create a new file with cat:

> "-" A hyphen (used alone) generally signifies that input will be taken from stdin as opposed to a named file:

List of cat command options:

Now what’s the opposite of cat? Yeah it’s ‘tac‘. `tac` is a command under Linux, try it for yourself.

## od

od (Octal dump) command in Linux is used to output the contents of a file in different formats with the octal format being the default.
This command is especially useful when debugging Linux scripts for unwanted changes or characters.

as and example:

With `-t` option we can select output format and display it. (Traditional format specifications may be intermixed):

example:

`-A` Option displays the contents of input in different format by concatenation some special character (offsets).

* **Hexadecimal (using -x along with -A)**
* **Octal (using -o along with -A)**
* **Decimal (using -d along with -A)**

`-An` Option displays the contents of input in character format but with no offset information:

## expand and unexpand

The **expand** command is used to convert tabs in files to spaces.

lets try it :

By default, expand converts tabs into the corresponding number of spaces. But it is possible to tweak the number of spaces using the -t (– – tabs=N) command line option. This option requires us to enter the new number of spaces(N) we want the tabs to get converted.

expand command options:

The **unexpand** command is used to convert space characters (blanks) into tabs in each file(unexpand needs at least two spaces).

Lets do reverse:

unexpand with no options just initial blanks!!! `-a` option convert all blanks, instead of just initial blanks:

> unexpand only convert double spaces and more to tab, it doesn't convert single spaces!

the unexpand command options:

## tr command

tr stands for **translate**. The tr utility copies the standard input to the standard output with substitution or deletion of selected characters. The syntax of tr command is:

Lets convert lower case to upper case:

The following command will also convert lower case to upper case:

Translate white-space to tabs:

if there are two are more spaces present continuously, then the previous command will translate each spaces to a tab. We can use `-s` option to squeeze repetition of characters :

`-d` option can be used to delete specified characters :

We complement the sets using `-c` option For example, to remove all characters except digits, you can use the following.:

tr has many options and sets try tr --help for more information.

## pr

The pr command is used to format files for printing. The default header includes the filename and file creation date and time, along with a page number and two lines of blank footer.

**Note:** When output is created from multiple files or the standard input stream, the current date and time are used instead of the filename and creation date.

We can print files side-by-side in columns and control many aspects of formatting through options.

`--column` defines number of columns created in the output.`-l`specifies page length (default is 66 lines).As usual, refer to the **man** page for details.

## nl

nl is a linux command to number lines of the files, it copies its files to standard output, prepending line numbers.

`-n Format`Uses the value of the Format variable as the line numbering format. Recognized formats are:

* ln :Left-justified, leading zeros suppressed
* rn :Right-justified, leading zeros suppressed (default)
* rz: Right-justified, leading zeros kept

> By default nl skip over blank lines and does not give a number to them, use -ba switch to assign them numbers.

other ln options:

`cat -n filename` does the same thing that `nl` command do.

## fmt

fmt simple optimal text formatter, it reformats paragraphs in specified file and prints results to the standard output.

By default fmt sets the column width at 75. This can be changed with the -w , --width=WIDTHoption.

fmt command options:

## sort and uniq

**Sort** is a Linux program used for printing lines of input text files and concatenation of all files in sorted order. Sort command takes blank space as field separator and entire Input file as sort key. It is important to notice that sort command don’t actually sort the files but only print the sorted output, until your redirect the output.

If a file has words/lines beginning with both upper case and lower case characters, then sort displays those with upper case at top. However, we can change this behavior using the -f command line option:

The `-n` option sort the contents numerically. Also we can sort a file base on "`n"`**th** column with `-k`n option:

user `-r` to reverse the result of comparisons. Other options of sort command:

Sort can sort the contents of two files on standard output in one go! `sort 1.txt 2.txt`

**uniq** command is used to report or omit repeated lines, it filters lines from standard input and writes the outcome to standard output.

use -c to display number of repetitions for each line:

-d displays only the repeated lines and visa versa -u just shows uniq ones:

try `-D` to see all duplicated lines. other options from uniq --help :

## split

split command is used to split or break a file into the pieces.

* Replace filename with the name of the large file you wish to split.
* Replace prefix with the name you wish to give the small output files.
* We can exclude [options], or replace it with either of the following:
* `-l linenumber`
* `-b bytes`

If we use the -l (a lowercase L) option, replace line number with the number of lines we'd like in each of the smaller files (the default is 1,000).

The split command will give each output file it creates the name prefix with an extension tacked to the end that indicates its order. By default, the split command adds aa to the first output file, proceeding through the alphabet to zz for subsequent files. If you do not specify a prefix, most systems use x.

If we use the -b option, replace bytes with the number of bytes you'd like in each of the smaller files.

Some other options are:

For joining the splitted files use `cat x* > orginalfile` .

## wc

The wc (word count) command is used to find out number of newline count, word count, byte and characters count in a file.

A Basic Example of WC Command

Three numbers shown below are **17** (number of **lines**), **80** (number of **words***[by default space delimited]*) and **511**(number of **bytes**) of the file.

options:

## head and tail commands:

##

## head

The head command reads the first ten lines of a any given file name.

For example lets take a look at /var/log/yum.log file:

For retrieving desired number of lines use -n or simple - options:

Options from`head --help` :

## tail

tail command displays last ten lines of any text file.

Similar to the head command above, tail command also support options -n number of lines and n number of characters.

-f option will cause tail will loop forever, checking for new data at the end of the file(s). When new data appears, it will be printed. It works great with log files and lets us see what is going on:

options:

## less

less command allows you to view the contents of a file and navigate through file.

By default the only way to exit less command is to hit q key. To change this behavior and automatically exit file when reaching the end of file use the `-e` or `-E` option. `less -e /var/log/auth.log` or `less -E /var/log/auth.log`

* To open a file at the first occurrence of a pattern use the following syntax:

`less +/sshd /var/log/auth.log`

* In order to automatically append the content of a file opened in less command use the Shift+f keys combination or run less with the following syntax:

`less +F /var/log/messages`

This makes less to run in interactive mode (live) and display new content on-fly while waiting for new data to be written to file. This behavior is similar to tail -f command. To exit live mode just press`Ctrl+c`keys.

**Tip**: In combination with a pattern you can watch the log file interactively with`Shift+f`key stroke while matching a keyword.

> **less vs more**
>
> less command is similar to more, he main difference between more and less is that less command is faster because it does not load the entire file at once and allows navigation though file using page up/down keys.
>
> Whether you decide to use more or less, which is a personal choice, remember that less is more with more features.

## cut

The cut command in UNIX is a command line utility for cutting sections from each line of files and writing the result to standard output. It can be used to cut parts of a line by byte **position**, **character** and **delimiter**.

**cut by byte position:**

**cut by character:**

**cut based on a delimiter:**

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbY-e_UpA-Zc2U-6%252Fprocesstxt-cut.jpg%3Fgeneration%3D1569999734513434%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=c4990fc0&sv=2)

To cut using a delimiter use the -d option. This is normally used in conjunction with the -f option to specify the field that should be cut. examples:

cut has lots of options:

## paste

The paste command displays the corresponding lines of multiple files side-by-side.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbY1NEEkD3QsopQW%252Fprocesstxt-paste.jpg%3Fgeneration%3D1569999734241297%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=75dc5c33&sv=2)

paste writes lines consisting of the sequentially corresponding lines from each FILE, separated by tabs.To apply a colon (:) as a delimiting character instead of tabs, use -d option:

paste command options:

## join

Joins the lines of two files which share a common field of data.

> When **using** `join`, the **input files must be sorted** ***by the join field ONLY***, otherwise you may see the warning

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M_kPH5Ueg0aN0Tnjgh0%252F-M_kQAC_9tSPjzPlv6i2%252Fprocesstxt-join.jpg%3Falt%3Dmedia%26token%3D76663212-aa79-44aa-9951-86d281c8ee2c&width=768&dpr=4&quality=100&sign=43b93137&sv=2)

By default, the join command only prints pairable lines. unpairable lines are left out in the output. However, if we want, we can still have them in the output using the -a command line option. This option requires you to pass a file number so that the tool knows which file you are talking about.

Inorder to print unpaired lines (meaning, suppress the paired lines in output),use the -v command line option. This options works exactly the way -a works.

join combines lines of files on a common field, which is the first field by default. However, if we want, we can specify a different field for each file using -1 and -2 command line options. for example `join -1 2 -2 2 file1 file2` uses second field of each line. join command options:

## sed

The name **Sed** is short for **\_s\_tream \_ed\_itor**.
**S** stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline). sed uses regular expressions and the most basic (and popular) usage of sed is the substitution of characters.

As an example lets replace 'l' with "L" in a sample text file:

By default sed just perform the substitution just once for first instance of term, use -g flag to perform the substitution for all instances of term on every line of file.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbY6baV30RLtlg9D%252Fprocesstxt-seds.jpg%3Fgeneration%3D1569999734120679%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=652ea8b1&sv=2)

Additionally, we can gi instead of g in order to ignore character case:

Another example is replacing blank spaces with tab :

sed is extremely powerful, and the tasks it can accomplish are limited only by your imagination.

.

.

.

sources:

<https://developer.ibm.com/tutorials/l-lpic1-103-2/>

<https://ryanstutorials.net/linuxtutorial/piping.php#piping>

<https://www.tecmint.com/linux-io-input-output-redirection-operators/>

<https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection>

<https://www.tecmint.com/13-basic-cat-command-examples-in-linux/>

<https://kb.iu.edu/d/afar>

<https://www.tecmint.com/wc-command-examples/>

<https://www.tecmint.com/view-contents-of-file-in-linux/>

<http://landoflinux.com/linux_expand_unexpand_command.html>

<https://www.geeksforgeeks.org/expand-command-in-linux-with-examples/>

<https://www.thegeekstuff.com/2012/12/linux-tr-command>

<https://www.howtoforge.com/linux-uniq-command/>

<https://www.tecmint.com/linux-file-operations-commands/>

<https://www.tecmint.com/20-advanced-commands-for-linux-experts/>

<https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/com.ibm.aix.cmds4/nl.htm>

<https://shapeshed.com/unix-fmt/>

<https://www.tecmint.com/linux-more-command-and-less-command-examples/>

<https://www.tecmint.com/linux-file-operations-commands/>

<https://shapeshed.com/unix-cut/>

<https://www.computerhope.com/unix/upaste.htm>

<https://www.howtoforge.com/tutorial/linux-join-command/>

<https://www.tecmint.com/sed-command-to-create-edit-and-manipulate-files-in-linux/>

<https://www.tecmint.com/linux-sed-command-tips-tricks/>

.

Copy

# 103.3. Perform basic file management

### **103.3 Perform basic file management**

**Weight:** 4

**Description:** Candidates should be able to use the basic Linux commands to manage files and directories.

**Key Knowledge Areas:**

* Copy, move and remove files and directories individually
* Copy multiple files and directories recursively
* Remove files and directories recursively
* Use simple and advanced wildcard specifications in commands
* Using find to locate and act on files based on type, size, or time
* Usage of tar, cpio and dd

**Terms and Utilities:**

* cp
* find
* mkdir
* mv
* ls
* rm
* rmdir
* touch
* tar
* cpio
* dd
* file
* gzip
* gunzip
* bzip2
* xz
* file globbing

As we said Linux is the world of processes and files, in this section we start talking about file management in linux and we will talk about both files and directories (folders). Tools are pretty basic and their names are abstraction of what they really do.

### ls

ls **lists files and directories**, and their associated metadata, such as file size, ownership, and modification time.

We can use **absolute paths** (ex:`user1@ubuntu16-1:~$ ls /home/user1/Music`) or **relative paths** (ex: `user1@ubuntu16-1:~$ ls Music/`) with ls.

With no options, ls lists the files contained in the current directory, sorting them alphabetically.

`-1` prints outs each result in 1 line:

The default output of the ls command shows only the names of the files, which is not very informative. So lets use ls with `-l` for long listing format :

The first character represents the file type: "-" for a regular file, "d" for a directory, "l" for a symbolic link(we will see them).

When the long listing format is used the ls command will display the following file information:

1. The file type
2. The file permissions
3. Number of hard links to the file
4. File owner
5. File group
6. File size
7. Date and Time
8. File name

**Show Hidden Files**

By default, the ls command will not show hidden files. *In Linux, a hidden file is any file that begins with a dot (.)*.To display all files including the hidden files use the `-a` option:

Some other usefull options:

ls command options

description

-l

list with long format - show permissions

-r

list in reverse order

-t

sort by time & date

-lh

List Files with Human Readable Format

-F

List Files and Directories with ‘/’ Character at the end

-R

Recursively list Sub-Directories

-a

list all files including hidden file starting with '.'

## Copying, Moving & Deleting

To make it easier lets classfied them in some groups:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbk4D5K7QkDqydfs%252Fbasicfilemgmnt-table.jpg%3Fgeneration%3D1569999766137336%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=ac4d705d&sv=2)

Before going into how to use the touch command, let’s start by reviewing the file timestamps in Linux.

#### Linux Files Timestamps

In Linux every single file is associated with timestamps, and every file stores the information of **last access time**, **last modification time** and **last change time**. So, whenever we create new file, access or modify an existing file, the timestamps of that file automatically updated.

A file in Linux has three timestamps:

* **atime** (access time) - The last time the file was accessed/opened by some command or application such as cat, vim or grep.
* **mtime** (modify time) - The last time the file’s content was modified.
* **ctime** (change time) - The last time the file’s attribute or content was changed. The attribute includes file permissions, file ownership or file location.

To display the file status including the timestamps you can use the `stat` command.(we use ubuntu 16.04 here)

### touch

The touch command is a standard command used in UNIX/Linux operating system which is used to create, change and modify timestamps of a file.

* touch command (with no option) create an empty file if file does not exist.
* if file exists touch command would change its time stamps .

**creating an empty file:**

touch command is used to create a file without any content. The file created using touch command is empty. This command can be used when the user doesn’t have data to store at the time of file creation.

example:

**creating multiple empty files:**

for example:

**avoids creating new files:**

`-c`option tells that if the file does not exist, do not create it:

#### touch command timestamp options:

* `-a`: change the **access time** only
* `-d`: update the **access and modification times**
* `-m`: change the **modification time only**
* `-r`: **use the access and modification times of other file as reference.**
* `-t`: **creates a file using a specified time**

Lets do some timestamp modifications.

Create a file using a specified time:`touch -t YYMMDDHHMM fileName`

Change the access time:`touch -a fileName`

It only updates last access time.

Change the modification time:`touch -m fileName`

It only updates last modification time.

Explicitly Set the Access and Modification times: `touch -c -t YYDDHHMM filename`

Update access and modification time:`touch -c -d fileName`

We use the timestamp of another file with -r option: `touch -r refrence_file_name file_name`

and many more examples.

### mkdir

mkdir command in Linux allows the user to create directories (also referred to as folders in some operating systems )

This command can create multiple directories at once as well as set the permissions for the directories. It is important to note that the user executing this command must have enough permissions to create a directory in the parent directory, or he/she may recieve a ‘permission denied’ error.

Lets try some of the most useful switches, `-p`enables the command to create parent directories as necessary. If the directories exist, no error is specified:

We can create a directory and set the permissions(will be discussed later) for that directory at the same time using -m option:

The syntax of the mode is the same as the chmod command (will be discussed later).

with `-v`option, it prints a message for each created directory.

### cp

The `cp` command is a command-line utility for copying files and directories. [Copies of files are independent of the original file( unlike the `mv` command) ].The basic syntax of the cp command is:

> cp can take 1 or more sources(s) but just one destination.

It supports copying one or more files or directories with options for taking backups and preserving attributes.

Do not forget to consider source and destination types (files or directory) when using cp command.

* If the target is an existing directory, then all sources are copied into the target.
* If the target is a directory that does not exist, then the (single) source must also be a directory and a copy of the source directory and its contents is made with the target name as the new name.
* If the target is a file, then the (single) source must also be a file and a copy of the source file is made with the target name as the new name, replacing any existing file of the same name.

lets do some examples:

**copy a file:**

**take a backup when copying a file**

If a copy operation will overwrite a file the `-b` flag may be used to create a back up of the file. This copies the file into place and writes a backup file.

specify the name of the backup file use the `-S` option. try `cp -S .file2bak file1 file2`

**copy multiple files (into a directory)**

**Copying files recursively**

We can use cp to copy entire directory structures from one place to another using the `-R` option to perform a recursive copy.

Let's say you are the user root and you have a directory, /home/test-space, which contains many files and subdirectories. You want to copy all those files, and all the subdirectories (and the files and subdirectories they contain), to a new location, /root/files-backup. You can copy all of them using the command:

`cp -R ~/test-space ~/files-backup`

* If the directory files-backup already exists, the directory files will be placed inside.
* If files-backup does not already exist, it will be created and the contents of the files directory will be placed inside it.

**copy a directory**

By default the cp command will not copy directories. Attempting to copy a directory results in an error.

To copy a directory pass the `-R` flag. This will recursively copy a folder and create a copy.

**copy multiple directories**

To copy multiple directories pass the path of the directories to be copied followed by the destination directory.

Now lets take a look at some cp command options:

cp command useful options:

Description

-v,--verbose

Verbose mode; explain what is being done.

--preserve

preserve file attributes (permissions, group and user owernship).By default mode, ownership and timestamps will be preserved.

-i , --interactive

Prompt before overwrite (overrides a previous -n option).

-n , --no-clobber

Do not overwrite an existing file. If -i/--interactive was previously specified, this option overrides it. This option cannot be specified with -b/--backup, because backups are only created when a file would have been overwritten.

-f,--force

If an existing destination file cannot be opened, remove it and try again. This option has no effect if the -n/--no-clobber option is used. However, it applies independently of -i/--interactive; neither option cancels the effect of the other.

cp command has lots of options.Try `man cp` command for more information.

### mv

`mv` is used to **move or rename one or more files or directories**. In general, the names we can use follow the same rules as for copying with cp; [If you are moving a file on the same file system, the inode wont change].

* Rename a file( or directory) name source to destination:

* Move source file(s) or directory(s) to a directory named destination:

Same as the previous syntax, but specifying the directory first, and the source file(s)(or directory(s)) last

Lets try mv command:

**Renaming a File or a directory:**

**Moving Files into a directory:**

**Moving a directory into another :**

we could use`mv -t dirA dir3` command as well. `-t, --target-directory`Move all sources into the directory destination.

usefull mv command options:

mv command options

description

-v

verbose - print source and destination files

-i

interactive prompt before overwrite

-u

update - move when source is newer than destination

-f

force move by overwriting destination file without prompt

> #### cp vs mv :
>
> Normally, the cp command will copy a file over an existing copy, if the existing file is writable. On the other hand, the mv will not move or rename a file if the target exists. We can overcome this using the`-f`switch.

### rm

`rm` stands for **remove** here. `rm` removes files or directories.

Lets try:

**Removing Files**

**File names starting with a dash, How to remove it?**

To remove a file whose name begins with a dash ("-"), you can specify a double dash ("--") separately before the file name. This extra dash is necessary so that rm does not misinterpret the file name as an option: `rm -- -file.txt`Or, we can delete it by referring to it with a pathname : `rm /home/hope/-file.txt`

some other options of rm command:

mv options

description

-v

Verbose mode; explain at all times what is being done.

-i

prompt before every removal

-f,--force

Ignore none existant files,and never prompt before removing.

-d,--dir

Remove empty directories.

#### Removing directories

By default, `rm` does not remove directories.

If the specified directory is empty, it may be removed with the -d/--dir option, instead.

What if desired directory contains some files? If the **-r/-R/--recursive** option is specified, we can remove that directory however rm will remove any matching directories and their contents!

`rm -d`lets us to remove a directory without specifying **-r/-R/--recursive**, provided that the directory is **empty**. In other words, **rm -d** is equivalent to using **rmdir**.

### rmdir

Removing directories using the rmdir command is the opposite of creating them. We can remove a directory with `rmdir` only if it is **empty** as there is **no option to force removal**.

Again, there is a`-p` option to remove parents as well. Let try it:

Normally, when`rmdir` is instructed to remove a non-empty directory, it reports an error. With `--ignore-fail-on-non-empty`option suppresses those error messages.

## Handling multiple files and directories

Some time we need to work on more than one files, Now we try to have review over some recursive commands

### Recursive manipulation

**Recursive listing**

The ls command has a -R (note uppercase “R”) option for listing a directory and all its subdirectories. The recursive option applies only to directory names, for example, in a directory tree.

**Recursive copy**

We can use the -r (or -R or --recursive) option to cause the cp command to descend into source directories and copy the contents recursively. To prevent an infinite recursion, we cannot copy the source directory itself!

**Recursive deletion**

I mentioned earlier that *rmdir only removes* ***empty*** *directories*. We can use the `-r` (or -R or --recursive) option to cause the rm command to remove both files and directories:

## Wildcards and Globbing

**File globbing is a feature provided by the UNIX/Linux shell to represent multiple filenames by using special characters called wildcards with a single file name.** A wildcard is essentially a symbol which may be used to substitute for one or more characters. Therefore, we can use wildcards for generating the appropriate combination of file names as per our requirement.

* `?` **is used to match any single character.** We can use ‘?’ for multiple times for matching multiple characters.

* `*` **is used to match zero or more characters.** If we have less information to search any file or information then we can use ‘\*’ in globbing pattern.

* `[ ]`**is used to match the character from the range. Some of the mostly used range declarations are mentioned below:**

`[A-Z]` : All uppercase alphabets

`[a-z]` : All lowercase alphabets

`[a-zA-Z0-9]` : All uppercase alphabets, lowercase alphabet and digits

> The`-`character between two others represents a range that includes the two other characters and all characters between them in the collating sequence.

* **The**`!` **character means NOT so it matches any character except the remaining characters**.

* `{ }`**can be used to match filenames with more than one globbing patterns. Each pattern is separated by ‘,’ in curly bracket without any space.**

`rm {*.doc,*.docx}` : delete all files whose extensions are ‘doc’ or ‘docx’.

* **and finally** `\` **is used as an "escape" character**, we have used it to protect a subsequent special character. example: "\\” searches for a backslash

> We can disable globbing using `set -f` command.

**Wildcard patterns vs Regular Expressions**

Wildcard patterns and regular expression patterns share some characteristics, but they are not the same. Pay careful attention.

Now that we’ve covered the file and directory topic with the big recursive hammer that hits everything, and the globbing hammer that hits more selectively, let’s look at the find command, which can be more like a surgeon’s knife.

### Finding Files

The find command is used to find files in one or more directory trees, based on criteria such as name, time stamp, or size.

### find

The find command searches for files or directories using all or part of the name, or by other search criteria, such as size, type, file owner, creation date, or last access date.

1. The `starting/path` attribute will define the top level directory where find begins filtering.
2. The `options`attribute will control the behavior and optimization method of the find process.
3. The `expression` attribute controls the tests that search the directory hierarchy to produce output.

   The most basic find is a search by name or part of a name:

`-name` option used for searching for files based on their name. `-i`makes it case insensitive. In the first example above, we found both files and a directory (/etc).

**finding hidden files :** If you want to find a file or directory whose name begins with a dot, such as .bashrc or the current directory (.), then you must specify a leading dot as part of the pattern. Otherwise, name searches ignore these files or directories. `find . -name ".*"`

note: If you want to chain different results together, you can use the “-and” or “-or” commands. The “-and” is assumed if omitted. `find . -name file1 -or -name file9`

**Finding files by type**

We can specify the type of files you want to find with the “-type” parameter. It works like this:

* `-type f`will search for a regular file
* `-type d` will search for a directory
* `-type l` will search for a symbolic link

**Finding files by size**

We can also search by file size, either for a specific size (n) or for files that are either larger (+n) or smaller than a given value (-n). By using both upper and lower size bounds, we can find files whose size is within a given range. By default, the -size option of find assumes a unit of ‘b’ for 512-byte blocks.

* `-size +/- [b] [c] [w] [k] [M} [G]`

as an example lets find files smaller than 1 kilobytes:

We can find all empty files using `find . -size 0b` or `find . -empty` .

**Finding files based on their time:**

Linux stores time data about access times, modification times, and change times.

* **Access Time**: Last time a file was read or written to.
* **Modification Time**: Last time the contents of the file were modified.
* **Change Time**: Last time the file’s inode meta-data was changed.

We can use the time stamps described with the touch command to locate files having particular time stamps.

again (+/-) signs can be used to give it a range.

Find Changed Files in Last 2 Hours:

note : Adding the `-daystart` option to `-mtime` or `-atime` means that we want to consider days as calendar days, starting at midnight. So to list the regular files in your home directory that were modified yesterday we can use `find ~/ -daystart -type f -mtime 1` .

> We can also find files by owner and permissions and use filter result by depth (will be discussed in later sections"104-7")

Acting on files with two other switches:

find command switch

meaning

-ls

list current file in ls -dils format on standard output

-print

print the full file name on the standard output

As you can see find command has tons of options, get into more details using man page files.

#### Executing and Combining Find Commands (-exec)

We can execute an arbitrary helper command on everything that find matches by using the “-exec” parameter. This is called like this:

The `{}` is used as a placeholder for the files that find matches. The “\;” is used so that find knows where the command ends.

As an instance this will remove all empty files:

We could remove all empty files in this directory and its subdirectories:

We could then change the directory permissions like this:

## Identifying files

File names often have a suffix such as gif, jpeg, or html that gives a hint of what the file might contain. Linux does not require such suffixes and generally does not use them to identify a file type. Knowing what type of file you are dealing with helps you know what program to use to display or manipulate it.

### file

The file command tells us something about the type of data in one or more files.

`-b, –brief` **:** This is used to display just file type in brief mode.

`-z`**:** Try to look inside compressed files.

and `-i`option To view mime type of file.

A MIME type is a label used to identify a type of data. It is used so software can know how to handle the data. It serves the same purpose on the Internet that file extensions do on Microsoft Windows.

### Archiving and Compressing files

Archiving and compressing are two different things

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGblHWc3u54BhTcqV%252Fperformbasicfile-archcompress.jpg%3Fgeneration%3D1569999771744991%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=5f0ffbc&sv=2)

* tar just archive files and does not do any compression by default.
* zip does both archiving and compresion.
* gzip and bzip2 are used just for compression.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGblJIvLd8XmznUjj%252Fperformbasicfile-compratio.jpg%3Fgeneration%3D1569999761042017%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=3a631d35&sv=2)

### zip

`Zip` is one of the most popular archive file format out there. With zip, you can compress multiple files into one file. This not only saves disk space, it also saves network bandwidth. This is why you’ll encounter zip files almost all the time.

Lets take a look a look:

use the `-r` option with the zip command and it will recursively zips the files in a directory. This option helps you to zip all the files present in the specified directory:

### uzip

A separate companion program, unzip, unpacks and uncompresses zip archives.

zip command example

Description

zip –v filename.zip file1.txt

Verbose mode or print diagnostic version info.

zip –d filename.zip file.txt

Removes the file from the zip archive.

zip –u filename.zip file.txt

Updates the file in the zip archive.

zip –m filename.zip file.txt

Deletes the original files after zipping.

zip –x filename.zip file\_to\_be\_excluded

Exclude the files in creating the zip.

### Compressing files

### gzip

Gzip (GNU zip) is a compressing tool, which is used to truncate the file size.

**By default** original file will be replaced by the compressed file ending with extension (.gz) and gzip removes the original files after creating the compressed file. gzip keeps the original file mode, ownership, and timestamp.

### gunzip

To decompress a file we can use gunzip command and your original file will be back.

also we can use -d option to decompress a file using the “gzip” command.ex : `gzip -d mydoc.gz`

gzip command example

Description

gzip -r testfolder

compress every file in a folder and its subfolders

gzip -k mydoc.txt

compress the file and keep the original file

gzip -f myfile1.txt

fore to compress already compressed file

gzip -v mydoc.txt

displays the name and percentage reduction for each file compressed or decompressed. we can use -l with compressed files.

gzip -L filename.gz

displays the gzip license

gzip -9 mydoc.txt

-[1-9] option : It allows to change the compression level.

1 : fastest compression speed but lower ratio

9 : highest compression ratio but at a lower speed

### bzip2

Like gzip, bzip2 command in Linux is used to compress and decompress the files. It uses different compression algorithm so it compress files better than gzip, but It has a slower decompression time and higher memory use.

### bunzip2

bunzip2 is used for decompression bzip2 files:

also **-d**  option is used for decompression of compressed files.

bzip2 command example

Description

bzip2 -k input.txt

does compression but does not deletes the original file

bzip2 -z input.txt

forces compression. It is an opposite command of decompression

bzip2 -v input.txt

show the compression ratio for each file processed

bzip2 -L filename.gz

-V , -L used to display the software version, license terms

bzip2 -q input.txt

It will suppress non-essential warning messages.

bzip2 doesn't any options for compressing a directory, so use tar with that. How? read tar section.

### xz

xz is a new general-purpose, command line data compression utility, similar to gzip and bzip2. It can be used to compress or decompress a file according to the selected operation mode. It supports various formats to compress or decompress files.

Selecting a compression utility to use will depend mainly on two factors, the compression speed and rate of a given tool. Unlike its counterparts, xz is not commonly used but offers the best compression.

or we could use xz `-x` file to compress that. `-d` is used for decompression:

xz command example

Description

xz -k file.txt

prevent deleting of the input file(s)

xz -f file.txt.xz

use the -f option to force the process(ex: compressed file already exist)

xz -9 file.txt

different compression preset levels (0 to 9, with default being 6) --fast equals -0 and --best is the same as -9

xz -q file.txt

run it in quiet mode or enable verbose mode with the -v

### Archiving files

What is an Archive file?

An Archive file is a file that is composed of one or more files along with metadata. Archive files are used to collect multiple data files together into a single file for easier portability and storage, or simply to compress files to use less storage space.

### tar

The Linux ‘tar’ stands for tape archive, is used to create Archive and extract the Archive files. tar command in Linux is one of the important command which provides archiving functionality in Linux.

Here a few common use cases of the tar command:

* Backup of Servers and Desktops.
* Document archiving.
* Software Distribution.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGblLLI6RYKe_1q5J%252Fperformbasicfile-tar.jpg%3Fgeneration%3D1569999761015350%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=94fd4d33&sv=2)

lets start:

**Create tar Archive File**

We can include more than one directory, also it is possible to exclude with `--exclude` option.

note: by default tar uncompress file in your current directory and it can make some problems(overwriting ,...), for avoiding that use `tar -xvf backupfile -C /restoreDir` command. `-C` means change the directory before extracting the backup.

**Untar tar Archive File**

We can use Linux tar command to create compressed or uncompressed Archive files and also maintain and modify them.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqVYH3vJVpW7aU77uH5%252F-LqVlvBDN4ENXQxkRx7k%252Fperformbasicfile-targzipbzip2.jpg%3Falt%3Dmedia%26token%3D87fc9dbf-5d30-4412-ac79-d26f94316ec2&width=768&dpr=4&quality=100&sign=dc22fdbe&sv=2)

for decompressing tar.gzip use  `tar -xzvf file.tar.gz` and `tar -xjvf file.tar.bz2` for bzip2 files.

note: `-r` option can not append any files to a **compressed file**.

we usually use mixture of tar options to gain what we want:

tar command example

Description

tar tf file.tar

list the contents and specify the tarfile

tar tvf file.tar

Viewing the Archive

tar tvf file.tar filename

We can pass a file name as an argument to search a tarfile

tar tvf file.tar --wildcards '\*.png'

Using wildcards with tar

tar -tvfW file.tar

Verify tar Archive File

tar -rvf file.tar newfile.txt

Add a file to .tar File

tar -uvf file.tar newdir

Add a directory to an existing .tar file

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGblN4FLNwqdcWPxs%252Fperformbasicfile-over.jpg%3Fgeneration%3D1569999765651887%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=bcd1fbd2&sv=2)

use `tar -cJf file.tar.xz` to create xz compressed file and `tar -xJf file.tar.xz` for extracting.

### dd

dd stands for Convert & Copy but why it is not cc? because the name cc is already used by c compiler. Many people call it Disk Destroyer because dd doesn't care at all about file system and strickly works with Block Devices!

The command line syntax of dd differs from many other Unix programs, in that it uses the syntax *option=value* for its command line options, rather than the more-standard *-option value* or *–option=value* formats. By default, dd reads from stdin and writes to stdout, but these can be changed by using the if (input file) and of (output file) options.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGblP5EV4K97FubSP%252Fperformbasicfile-dd.jpg%3Fgeneration%3D1569999760962346%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=25facc94&sv=2)

dd takes an input file line (ex:/dev/sda) and it writes it to the out put file (ex:/dev/sdb) we specify, bs is block size, how big we want to write blocks and it is not neseccary and can be omitted.

Backup the entire harddisk:

We can even use dd to copy any kind of block devices and as dd works on block devices itself it doesn't matter if partion ups.

* If there are any errors, the above command will fail. If you give the parameter *“conv=noerror”* then it will continue to copy if there are read errors.`dd if = /dev/sda of = /dev/sdb conv=noerror`
* Input and output should be mentioned very carefully. Just in case, you mention source device in the target and vice versa, you might loss all your data.
* To copy, hard drive to hard drive using dd command given below, sync option allows you to copy everything using synchronized I/O.`dd if = /dev/sda of = /dev/sdb conv=noerror, sync`

dd comand examples

Description

dd if = /dev/sda of = /dev/sdb

backup entire Disk

dd if=/dev/hda1 of=~/partition.img

backup a partition

dd if = /dev/hda of = ~/hdadisk.img

create an image of a Hard Disk

dd if = hdadisk.img of = /dev/hdb

restore using Hard Disk image

dd if = /dev/cdrom of = tgsservice.iso bs = 2048

create CD-Rom backup

dd if=/path/to/ubuntu.iso of=/dev/sdb bs=1M

create bootable usb drive from image

dd if=textfile.ebcdic of=textfile.ascii conv=ascii

Convert the data format of a file from EBCDIC to ASCII

conv can do many thing such as Converting a file to uppercase or visa versa.

### cpio

`cpio` stands for “**C**o**p**y **i**n, copy **o**ut“. It is used for processing the archive files like *.cpio or* .tar. This command can copy files to and from archives.

* **Copy-out Mode:** Copy files named in name-list to the archive `command | cpio -o > archive`
* **Copy-in Mode:** Extract files from the archive `cpio -i < archive`
* **Copy-pass Mode:** Copy files named in name-list to destination-directory `cpio -p destination-directory < name-list`

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqeUL6O1-THSia2AZHJ%252F-LqeUa8zCH0Sq8p-9euM%252Fperformbasicfile-cpio.jpg%3Falt%3Dmedia%26token%3D611b6626-7f6f-414b-97ed-481f392b8f2a&width=768&dpr=4&quality=100&sign=ea078a66&sv=2)

cpio command example

Description

ls /etc | cpio -ov file.cpio

create a cpio file

cpio -iv < file.cpio

extract a cpio file

ls | cpio -ov -H tar file.tar

create a tar file using cpio

cpio -iv -F file.tar

extract a tar file using cpio

cpio -it -F < file.tar

only view tar archive file using cpio

.

.

.

.

#### Linux Devices (beyond the scop of LPIC1 exam)

In Linux various special files can be found under the directory `/dev`. These files are called device files and behave unlike ordinary files.

The columns are as follows from left to right:

* Permissions
* Owner
* Group
* Major Device Number
* Minor Device Number
* Timestamp
* Device Name

Remember in the ls command you can see the type of file with the first bit on each line. Device files are denoted as the following:

The most common types of device files are for block devices and character devices. These files are an interface to the actual driver (part of the Linux kernel) which in turn accesses the hardware. Another, less common, type of device file is the named *pipe:*

**Character Device:**These devices transfer data, but one a character at a time. You'll see a lot of pseudo devices (/dev/null) as character devices, these devices aren't really physically connected to the machine, but they allow the operating system greater functionality.

**Block Device:**These devices transfer data, but in large fixed-sized blocks. We'll most commonly see devices that utilize data blocks as block devices, such as harddrives, filesystems, etc.

**Pipe Device:**Named pipes allow two or more processes to communicate with each other, these are similar to character devices, but instead of having output sent to a device, it's sent to another process.

**Socket Device:**Socket devices facilitate communication between processes, similar to pipe devices but they can communicate with many processes at once.

**Device Characterization (Major Device Number & Minor Device Number)**

Devices are characterized using two numbers, major device number and minor device number. **We** can see these numbers in the above ls example, they are separated by a comma. For example, let's say a device had the device numbers: 8, 0:

The major device number represents the device driver that is used, in this case 8, which is often the major number for sd block devices. The minor number tells the kernel which unique device it is in this driver class, in this case 0 is used to represent the first device (a).

.

.

<https://www.computerhope.com/unix/uls.htm>

<https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/>

<https://www.rapidtables.com/code/linux/ls.html>

<https://www.tecmint.com/8-pratical-examples-of-linux-touch-command/>

<https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/>

<https://linuxize.com/post/linux-touch-command/>

<https://www.geeksforgeeks.org/mkdir-command-in-linux-with-examples/>

<https://www.lifewire.com/create-directories-linux-mkdir-command-3991847>

<https://developer.ibm.com/tutorials/l-lpic1-103-3/>

<https://shapeshed.com/unix-cp/>

<https://www.rapidtables.com/code/linux/cp.html>

<https://www.computerhope.com/unix/ucp.htm>

<https://www.rapidtables.com/code/linux/mv.html>

<https://www.computerhope.com/unix/umv.htm>

<https://jadi.gitbooks.io/lpic1/content/1033_perform_basic_file_management.html>

<https://www.computerhope.com/unix/urm.htm>

<https://www.computerhope.com/unix/urmdir.htm>

<https://www.linuxnix.com/10-file-globbing-examples-linux-unix/>

<https://linuxhint.com/bash_globbing_tutorial/>

<https://www.linode.com/docs/tools-reference/tools/find-files-in-linux-using-the-command-line/>

<https://www.lifewire.com/uses-of-linux-command-find-2201100>

<https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-a-linux-vps>

<https://www.geeksforgeeks.org/tar-command-linux-examples/>

<https://itsfoss.com/linux-zip-folder/>

<https://www.geeksforgeeks.org/zip-command-in-linux-with-examples/>

<https://www.geeksforgeeks.org/gzip-command-linux/>

<https://www.geeksforgeeks.org/bzip2-command-in-linux-with-examples/>

<https://www.tecmint.com/xz-command-examples-in-linux/>

<https://www.debian.org/releases/wheezy/amd64/apds01.html.en>

<https://linuxjourney.com/lesson/device-types>

<https://www.geeksforgeeks.org/dd-command-linux/>

<https://linoxide.com/linux-command/linux-dd-command-create-1gb-file/>

[`https://www.geeksforgeeks.org/cpio-command-in-linux-with-examples/`](https://www.geeksforgeeks.org/cpio-command-in-linux-with-examples/)

and whith the special thanks from shawn powers.

Copy

# 103.4. Use streams, pipes and redirects

**Weight:** 4

**Description:** Candidates should be able to redirect streams and connect them in order to efficiently process textual data. Tasks include redirecting standard input, standard output and standard error, piping the output of one command to the input of another command, using the output of one command as arguments to another command and sending output to both stdout and a file.

**Key Knowledge Areas:**

* Redirecting standard input, standard output and standard error
* Pipe the output of one command to the input of another command
* Use the output of one command as arguments to another command
* Send output to both stdout and a file

**Terms and Utilities:**

* tee
* xargs

We have talked about basics of piping and redirecting in previous sections and in this tutorial we take a closer look at Linux techniques for redirecting standard IO streams.

### Input, output, and streams

In computing, a stream is something that can transfer data. Data streams, like water streams, have two ends. They have a source and an outflow.

A Linux shell, such as Bash, receives input and sends output as sequences or streams of characters. Stream of characters comes from or goes to a file, a keyboard, a window on a display, or some other IO device.

stdin, stdout, and stederr are three standard streams that are established when a Linux command is executed.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lqel1gGCatOnRA78g37%252F-LqeqjhaX8p9xw3nfOXR%252Fusestreams-streams.jpg%3Falt%3Dmedia%26token%3D24a6e1af-0b5c-46f3-94a9-f1bc60c96a9c&width=768&dpr=4&quality=100&sign=5deed1d2&sv=2)

Linux shells use these three standard I/O **streams ,** each of which is associated with **file descriptor**:**:**

* **stdout** is the standard output stream, which displays output from commands(**file descriptor** **1**)
* **stderr** is the standard error stream, which displays error output from commands(**file descriptor** **2**)
* **stdin** is the standard input stream, which provides input to commands(**file** **descriptor** **0**)

So we can see that there are two output streams, `stdout` and `stderr`, and one input stream, `stdin`

**What are file descriptors?**

Streams Are Handled Like Files. We can read text from a file, and we can write text into a file. Both of these actions involve a stream of data. So the concept of handling a stream of data as a file isn’t that much of a stretch.

Each file associated with a process is allocated a unique number to identify it.

This is known as the **file descriptor**. Whenever an action is required to be performed on a file, the file descriptor is used to identify the file. These values are always used for `stdin`, `stdout,` and `stderr`:

* 0: stdin
* 1: stdout
* 2: stderr

To make life more convenient the system creates some shortcuts for us:

### Redirecting standard IO

Although the model for standard input and output is a serial stream of characters to and from a terminal, we might want to prepare input data in a file, or save output or error information in a file. That’s where **.**comes in.

#### Redirecting output

There are two ways to redirect output to a file:

***n*****>**  redirects output from file descriptor n to a file. You must have write authority to the file. If the file does not exist, it is created. If it does exist, the existing contents are usually lost without any warning.

***n*****>>**  also redirects output from file descriptor n to a file. Again, we must have write authority to the file. If the file does not exist, it is created. If it does exist, the output is appended to the existing file.

> The *n* in n> or n>> refers to the *file descriptor*. If it omitted, then standard output (file descriptor 1) is assumed.

The `>` and `>>` redirection symbols works with **stdout** by default. We can use one of the numeric file descriptors to indicate which standard output stream you wish to redirect.

* **>** - standard output
* **2>** - standard error

">" redirects stdout

"2>" redirects stderr

**Append**

Commands with a double bracket *do not* overwrite the destination’s existing contents, they append.

* **>>** - standard output
* **2>>** - standard error

**To clobber or to noclobber?**

We said that output redirection using n> usually overwrites existing files. You can control this with the `noclobber` option of the `set` builtin. use set -C for enabling noclobber:

If it has been set, we can override it using n>|

use `set +C` for turning globbing off.

**redirect both standard output and standard error**

Sometimes, we might want to redirect both standard output and standard error into a file. This is often done for automated processes or background jobs so that we can review the output later.

* Use **&>** or **&>>** to redirect both standard output and standard error to the same place**.**

We can do it in another way, redirect file descriptor *n* and then redirect file descriptor *m* to the same place using the construct m>&n or m>>&n.

* **&1** and **&2** and **&0** reffer to current place of **stdout** , **stderror** and **stdin**.

The order in which outputs are redirected is important. For example,
`command 2>&1 >output.txt`
is not the same as
`command >output.txt 2>&1`

In the first case, stderr is redirected to the current location of stdout and then stdout is redirected to output.txt, but this second redirection affects only stdout, not stderr. In the second case, stderr is redirected to the current location of stdout and that is output.txt.

**redirecting to /dev/null**

At other times, wemight want to ignore either standard output or standard error entirely. To do this, redirect the appropriate stream to the empty file, /dev/null.

/dev/null is a special file called the null device. it is also called the bit-bucket or the black-hole because it immediately discards anything written to it and only returns an end-of-file EOF when read.

### redirecting input

"<" redirects stdin

or simply wc 0< list do the same thing.

### here documents

A here document (or heredoc) is a way of getting text input into a script or command without having to feed it in from a separate file.

**<<** redirects standard input and the command will take input until "HeredocDelimiter" string .

**Note:** There should not be any space between the << symbol and the limit string. If there are any characters between the limit string and the << symbol then the here document is unlikely to work.

> Reminder: "-" A hyphen (used alone) generally signifies that input will be taken from `stdin` as opposed to a named file. try: cat - << EOF > interesting.txt

### here string

**<<<** Redirect a single line of text to the stdin of cmd. This is called a here-string.

### **Pipes**

We use the `|` (pipe) operator between two commands to direct the stdout of the first to the stdin of the second. `command | command`

Some commands like grep can accept input as parameters, but some commands accepts arguments

> Parameter vs Argument:
>
> * **Parameter** is variable in the declaration of function.
> * **Argument** is the actual value of this variable that gets passed to function.

### Using output as arguments

In the privious of pipelines, we learned how to take the output of one command and use it as input to another command. Instead , what if we want to use the output of a command or the contents of a file as arguments to a command rather than as input. Pipelines don’t work for that.

Three common methods are:

1. The `xargs` command
2. The `find` command with the `-exec` option (previous section)
3. Command substitution ( will be discussed later)

### xargs

**xargs** is a Unix command which can be used to build and execute commands from standard input.

> If no command is specified, xargs executes echo by default.

There are several ways in which **xargs** is useful in daily usage of the command line.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lr3ctIjZ2f1bcj2eRMH%252F-Lr3py8D8lHfSwX4dDCZ%252Fusestreams-xarg.jpg%3Falt%3Dmedia%26token%3Df0b86d2c-3c7a-4267-9125-89e38c81bbd5&width=768&dpr=4&quality=100&sign=a52a89d0&sv=2)

We can replace occurrences of arguments via `-I` switch:

`it is also possible to run multiple commands with xargs`

cat a.txt | xargs -I % sh -c {command1; command2; ... }

With `-L` option, the input will break by line and not by blanks. Other options:

xarg command example

Description

xargs --version

Prints the version number of xargs command

xargs -a test.txt

It will show contents of file

xargs -p -a test.txt

-p option prompts for confirmation before running each command line.

xargs -r -a test.txt

-r option ensures if standard input is empty, then command is not executed

### tee

Sometimes we might want to see output on the screen while saving a copy for later. While we **could** do this by redirecting the command output to a file in one window and then using `tail -f` to follow the output in another screen, using the `tee` command is easier.

**tee** reads the standard input and writes it to both the standard output and one or more files.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lr3raitb3HOoQjTVftX%252F-Lr3z1LNRWzqG8PQSCC1%252Fupstreams-tee.jpg%3Falt%3Dmedia%26token%3D793a2aed-b3af-4732-8dc5-77bac3efc0ff&width=768&dpr=4&quality=100&sign=aa3064e1&sv=2)

tee always work after the '|' and it does both the tasks simultaneously.example:

with `-a` option It basically do not overwrite the file but append to the given file.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-103-4/>

<https://www.gnu.org/software/libc/manual/html_node/Streams-and-File-Descriptors.html>

<https://geek-university.com/linux/streams/>

<https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php>

<https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/>

<https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection>

<https://www.serverwatch.com/columns/article.php/3860446/Shell-Scripts-and-Here-Documents.htm>

<https://linuxhint.com/bash-heredoc-tutorial/>

<https://stackoverflow.com/questions/40230008/whats-the-usages-of-hyphen-in-linux-shell>

<https://www.geeksforgeeks.org/xargs-command-unix/>

<https://www.tecmint.com/xargs-command-examples/>

.

Copy

# 103.5. Create, monitor and kill processes

**Weight:** 4

**Description:** Candidates should be able to perform basic process management.

**Key Knowledge Areas:**

* Run jobs in the foreground and background
* Signal a program to continue running after logout
* Monitor active processes
* Select and sort processes for display
* Send signals to processes

**Terms and Utilities:**

* &
* bg
* fg
* jobs
* kill
* nohup
* ps
* top
* free
* uptime
* pgrep
* pkill
* killall
* screen

In this section we are talking about jobs and processes. What you should know is that, what exactly is a job?

If you run a command from the shell, that is job.

A job might be executed and exit immediately and runs for a short time only but some jobs run for a long time.

that goes to sleep for 3600 seconds, that is an hour! So you can wait for an hour (considering that you can not use your terminal) or you can run a job in background.

### Foreground and Background jobs (&)

A **job is a process that the shell manages**. Each job is assigned a sequential job ID. Because a job is a process, each job has an associated PID. There are two types of job statuses:

1. **Foreground**: When we enter a command in a terminal window, the command occupies that terminal window until it completes. This is a foreground job.
2. **Background**: When we enter an ampersand (**&**) symbol at the end of a command line, the command runs without occupying the terminal window. The shell prompt is displayed immediately after you press Return. This is an example of a background job.

> By default you get notified about terminated jobs when you hit enter ,Try set -b to get notified immediately.

**Job Control Commands**

Job control commands enable **us** to place jobs in the foreground or background, and to start or stop jobs. The table describes the job control commands.

Command

Description

jobs

Lists all jobs

bg %n

Places the current or specified job in the background, where n is the job ID

fg %n

Brings the current or specified job into the foreground, where n is the job ID

Control-Z

Stops the foreground job and places it in the background as a stopped job

Control-C

Ctrl+C kills the process

> if no job id is mentioned bg and fg consider the most recent job

### jobs

### bg

we cloud use `fg %3` command and it would have the same result.

### fg

We brought a job to foreground and use Ctrl + C to kill that job.

> we can disable and enable shell job control feature with`set +m and set -m` commands.

jobs normally stick to the shell running it, so they are killed when we close the terminal or log out. Some times we need to make sure that the running job is not attached to the running shell.This is where nohup and disown come to play.

**huponexit**

jobs are killed **only if** the `huponexit` option is set!

run`shopt huponexit` to see if this is true.

* If `huponexit` is false, *which* ***is the default*** *on at least some linuxes these days*, then backgrounded jobs will **not** be killed on normal logout!
* If `huponexit` is true, then we can use `nohup` or `disown` to dissociate the process from the shell so it does not get killed when you exit. Or, run things with `screen`.

use `shopt -s huponexit` and `shopt -u huponexit` in order to set and unset it.

### Signal a program to continue running after logout

### nohup

`Nohup` stands for **no hangup**, and that means even if the parent shell is diconnected the job just will continue, The output of the **nohup** command will write in **nohup.out** the file if any redirecting filename is not mentioned in **nohup** command.

Using nohup with commands:

Now even if we close the terminal and open it again ping is still running.

> Please notice that we can not use `fg`, `bg` commands on that particular job anymore.

When we run nohup command without ‘**&’** then it returns to shell command prompt immediately after running that particular command in the background.

> We useually use nohup with output redirection `nohup bash script.sh > myresult.txt 2>&1`

**disown**

We can also use disown command, it is used after the a process has been launched and put in the background, it’s work is to remove a shell job from the shell’s active list jobs, therefore we can not use fg, bg commands on that particular job anymore but that process keeps running even after closing current shell.

disown -h %1 lets us to have normal job control mechanisms to continue controlling the process until closing the terminal.

Option

Description

**-a**

Delete all jobs if jobID is not supplied.

**-r**

Delete only running jobs.

There is a problem with nohup and disown commands. There is no way to bring back that job to forground and work interactivly with that. So we need a different solution, screen.

### screen

**screen** command in Linux provides the ability to launch and use multiple shell sessions from a single *ssh* session.

When a process is started with ‘screen’, the process can be detached from session and then can reattach the session at a later time. When the session is detached, the process that was originally started from the screen is still running and managed by the screen itself. The process can then re-attach the session at a later time, and the terminals are still there, the way it was left. (you might need to install it)

#### Start screen for the first time

simple use screen command  **:**

use `screen -s Session_Name` to start a named session.now lets run a command inside screen:

> Inorder to create a new screen inside the current screen (nested screen) use just press **Ctrl-a** +**c**

#### Detach the screen

One of the advantages of screen that is you can detach it. Then, you can restore it without losing anything you have done on the screen. use **Ctrl-a + d** to detach**:**

**-d** is **also** used to detach a screen session so that it can be reattached in future.

**List screens**

**screen -ls** is used to display the currently opened screens including those running in the background:

**Reattach to a screen**

**-r**  It is used to reattach a screen session which was detached in past:

> We usually use `screen -dr`  command.This means detach the specified screen first and then reattach it.

#### Switching between screens

When we do nested screen, you can switch between screen using command **Ctrl-a +n**. It will be move to the next screen. When need to go to the previous screen, just press **Ctrl-a** +**p**.

#### Terminate screen session

Use “**Ctrl-A**” and “**K**” to kill the screen.

### Monitor active processes

#### What is process?

A program is a series of instructions that tell the computer what to do. When we run a program, those instructions are copied into memory and space is allocated for variables and other stuff required to manage its execution. This running instance of a program is called a process and it's processes which we manage

Each process got a **PID**. PID stands for **process identifier** and it is is a unique number that identifies each of the running processes in an operating system

processes can further be categorized into:

* **Parent processes** – these are processes that create other processes during run-time.
* **Child processes** – these processes are created by other processes during run-time.

therefore **PPID** stands for **Parent Process ID**. notes:

* note1:Used up pid’s can be used in again for a newer process since all the possible combinations are used.
* note2:At any point of time, no two processes with the same pid exist in the system because it is the pid that Unix uses to track each process.

> If we use the `jobs` command with the `-l` option, it will also show process ID.

### ps

ps (Process status) can be used to see/list all the running processes and their PIDs along with some other information depends on different options.

ps reads the process information from the virtual files in **/proc** file-system. In it's simplest form, when used without any option, `ps` will print four columns of information for minimum two processes running in the current shell, the shell itself, and the processes that run in the shell when the command was invoked.

Where,
**PID –** the unique process ID
**TTY –** terminal type that the user is logged into
**TIME –** amount of CPU in minutes and seconds that the process has been running
**CMD –** name of the command that launched the process.

> **Note –** Sometimes when we execute **ps** command, it shows TIME as 00:00:00. It is nothing but the total accumulated CPU utilization time for any process and 00:00:00 indicates no CPU time has been given by the kernel till now. In above example we found that, for bash no CPU time has been given. This is because bash is just a parent process for different processes which needs bash for their execution and bash itself is not utilizing any CPU time till now.

Usually when we use the command ps we add parameters like `-a`, `-u` and `-x`. While

* `a` = show processes for all users
* `u` = display the process’s user/owner
* `x` = also show processes not attached to a terminal

where column are :

* **USER –** Specifies the user who executed the program.

  **PID:** Process ID, shows the process identification number.

  **CPU%**: The processor % used by the process.

  **MEME%**: The memory % used by the process.

  **VSZ:** The virtual size in kbytes.

  **RSS:** In contrast with the virtual size, this shows the real memory used by the process.

  **TTY:** Identifies the terminal from which the process was executed.

  **STATE:** Shows information on the process’ state just as it’s priority, by running “man ps” you can see codes meaning.

  **START:** Show when the process has started.

  **TIME:** Shows the processor’s time occupied by the program.

  **C0MMAND:** Shows the command used to launch the process.

> We can also use ps -ef instead of ps aux . There are no **differences** in the output because the meanings are the same. The **difference between ps** -**ef and ps aux** is due to historical divergences **between** POSIX and BSD systems. At the beginning, POSIX accepted the -**ef** while the BSD accepted only the **aux** form. Both list all processes of all users. In that aspect `-e` and `ax` are completely equivalent.

Options for ps command

Description

ps -T

View Processes associated with a terminal

ps -x

View all processes owned by you

ps -o column\_name

view process according to user-defined format

It is also possible to use --sort option to sort output based on different fields (+ for ascending & - for descending). `ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -10` . With`-o` or `–format` options, ps allows us to build user-defined output formats.

**Process selection commands**

Description

ps -C command\_name

Select the process by the command name.

ps p process\_id

View process by process ID.

ps -u user\_name/ID

Select by user name or ID

ps -g group\_name , ps -G group\_id

Select by group name or ID

ps -t pst/0

Display Processes by TTY

We already know about the grep command in Linux, which searches for a pattern, and then prints the matching text in the output. What if the requirement is to apply this kind of processing to fetch select information about processes currently running in the system?

### pgrep

the `pgrep` command searches for processes currently running on the system, **based on a complete** or **partial process name**, or other specified attributes.

> Always use ps -ef command to make sure about process\_name. There is different between process\_name and the running program(like bash). compare pgrep -a and pgrep -af.

pgrep options:

> **Real Time process monitoring ?**
>
> Be creative and use combination of other commands like 'watch'. We can use 'watch' in conjunction with ps command to perform Real-time Process Monitoring :
>
> `watch -n 1 'ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head'`

But there is another tool for that, top.

### top

**top** command is used to show the Linux processes. It provides a dynamic real-time view of the running system. Usually, this command shows the summary information of the system and the list of processes or threads which are currently managed by the Linux Kernel.

Top output keep refreshing until you press ‘q‘.

Where,

* **PID:** Shows task’s unique process id
* **USER:** User name of owner of task.
* **PR:** Stands for priority of the task.
* **NI:** Represents a Nice Value of task. A Negative nice value implies higher priority, and positive Nice value means lower priority.
* **VIRT:** Total virtual memory used by the task.
* **RES:**It is the Resident size, the non-swapped physical memory a task has used.
* **SHR:** Represents the amount of shared memory used by a task.
* **%CPU:** Represents the CPU usage.
* **%MEM:** Shows the Memory usage of task.
* **TIME+:** CPU Time, the same as ‘TIME’, but reflecting more granularity through hundredths of a second.
* **COMMAND:**Shows the command used to launch the process.

top command option

description

top -n 10

Exit Top Command After Specific repetition

top -u user1

Display Specific User Process

Top -d seconds.tenths

It tells delay time between screen updates

top -h

Shows top command syntax

Running top command hot keys

Description

pressing ‘d‘

change screen refresh interval (default 3.0 sec)

Pressing ‘z‘

display running process in color

Pressing ‘c‘

display absolute path of running program

pressing ‘k‘

kill a process after finding PID of process(without exiting)

Pressing 'M'

sort based on memory usage

Shift+P

Sort by CPU Utilisation

Press ‘h‘

Getting top command help

### Manage processes

To manage processes in a linux machine we can send signals signals to the process.Many Signals are defined in the linux kernels. (try `man 7 signal`)

Signal Name

Signal Number

Description

SIGHUP

1

Hang up detected on controlling terminal or death of controlling process

SIGINT

2

Issued if the user sends an interrupt signal (Ctrl + C)

SIGQUIT

3

Issued if the user sends a quit signal (Ctrl + D)

SIGKILL

9

If a process gets this signal it must quit immediately and will not perform any clean-up operations

SIGTERM

15

Software termination signal (sent by kill by default)

SIGCOUNT

18

Continue the process stopped with STOP

STOP

19

Stop process

to send signals to processes there are some commands:

### kill

`kill` command in Linux (located in /bin/kill), is a built-in command which is used to terminate processes manually . *kill* command sends a signal to a process which terminates the process.

please notice that:

* A user can kill all his process.
* A user can not kill another user’s process.
* A user can not kill processes System is using.
* A root user can kill System-level-process and the process of any user.

note: If the user doesn’t specify any signal which is to be sent along with kill command then **default TERM signal** is sent that terminates the process.

use `kill -l` to see all signals you can send using kill.

There are two commands used to kill a process:

* kill – Kill a process by ID
* killall,pkill – Kill a process by name

killing a proccess by name could be realy dangerous, Before sending signal, verify which process is matching the criteria using “pgrep -l”.

### killall

`killall` is a tool for terminating running processes on your system **based on name**. *In contrast,* `kill` *terminates processes based on Process ID number (PID)*. Like `kill` , `killall` can also send specific system signals to processes.

note1:the whole process\_name should be defined ( ex : sleep not sle or slee).

note2: If no signal name is specified, SIGTERM is sent.

killall command example

Description

killall -l

all signals the killall command can send

killall -q process\_name

prevent killall from complaining if specified process doesn't exist

killall -u [user-name]

kill all processes owned by a user

killall -o 5h

kill all processes that have now been running for more than *5* hour

killall -y 4h

kill all precesses that less than 4 hours old

killall -w [process-name]

causes `killall` to wait until the process terminates before exiting.

### pkill

The PKill command allows you to kill a program simply **by specifying the name.**

note: We don't have to define whole process\_name. So it could be really dangerous!

example:

pkill command example

Description

pkill -c [process\_name]

return a count of the number of processes killed

pkill -U [real\_user\_ID]

kill all the processes for a particular user

pkill -G [real\_group\_ID]

kill all the programs in a particular group

### free

`free` command displays the total amount of **free space** available along with the amount of **memory used** and **swap** memory in the system, and also the **buffers** used by the kernel.

As free displays the details of the memory related to the system , its syntax doesn’t need any arguments to be passed but it has some options!

free command with no options produces the columnar output as shown above where column:

1. **total** : displays the total installed memory *(MemTotal and SwapTotal i.e present in /proc/meminfo).*
2. **used :** displays the used memory.
3. **free :** displays the unused memory.
4. **shared :** displays the memory used by tmpfs*(Shmen i.epresent in /proc/meminfo and displays zero in case not available).*
5. **buffers :** displays the memory used by kernel buffers.
6. **cached :** displays the memory used by the page cache and slabs*(Cached and Slab available in /proc/meminfo).*
7. **buffers/cache :** displays the sum of buffers and cache.

By default the display is in kilobytes, but you can override this using `-b` for bytes, `-k` for kilobytes, `-m` for megabytes, or `-g` for gigabytes.

`-t` displays an additional line containing the total of the total, used and free columns:

Other free command options:

### uptime

The `uptime` command shows you a one-line display that includes the current time, how long the system has been running, how many users are currently logged on, and the **system load averages** for the past 1, 5, and 15 minutes.

Lets try `uptime -h` to see all of `uptime` availbale options:

examples:

.

.

.

Processes deep dive ( Beyond the scope of LPIC1)

**Types of Processes**

1. **Parent and Child process :** The 2nd and 3rd column of the ps –f command shows process id and parent’s process id number. For each user process there’s a parent process in the system, with most of the commands having shell as their parent.
2. **Zombie and Orphan process :** After completing its execution a child process is terminated or killed and SIGCHLD updates the parent process about the termination and thus can continue the task assigned to it. But at times when the parent process is killed before the termination of the child process, the child processes becomes orphan processes, with the parent of all processes “init” process, becomes their new ppid.
   A process which is killed but still shows its entry in the process status or the process table is called a zombie process, they are dead and are not used.
3. **Daemon process :** They are system-related background processes that often run with the permissions of root and services requests from other processes, they most of the time run in the background and wait for processes it can work along with for ex print daemon.
   When ps –ef is executed, the process with ? in the tty field are daemon processes

**States of a Process in Linux**

* **Running** – here it’s either running (it is the current process in the system) or it’s ready to run (it’s waiting to be assigned to one of the CPUs). use ps -r command.
* **Waiting** – in this state, a process is waiting for an event to occur or for a system resource. Additionally, the kernel also differentiates between two types of waiting processes; interruptible waiting processes – can be interrupted by signals and uninterruptible waiting processes – are waiting directly on hardware conditions and cannot be interrupted by any event/signal.
* **Stopped** – in this state, a process has been stopped, usually by receiving a signal. For instance, a process that is being debugged.
* **Zombie** – here, a process is dead, it has been halted but it’s still has an entry in the process table.

**Processes state codes in ps aux or ps -ef command:**

* `R` running or runnable (on run queue)
* `D` uninterruptible sleep (usually IO)
* `S` interruptible sleep (waiting for an event to complete)
* `Z` defunct/zombie, terminated but not reaped by its parent
* `T` stopped, either by a job control signal or because it is being traced

Some extra modifiers:

* `<` high-priority (not nice to other users)
* `N` low-priority (nice to other users)
* `L` has pages locked into memory (for real-time and custom IO)
* `s` is a session leader
* `l` is multi-threaded (using CLONE\_THREAD, like NPTL pthreads do)
* `+` is in the foreground process group

.

<https://www.thegeekdiary.com/understanding-the-job-control-commands-in-linux-bg-fg-and-ctrlz/>

<https://superuser.com/questions/662431/what-exactly-determines-if-a-backgrounded-job-is-killed-when-the-shell-is-exited>

<https://linuxhint.com/nohup_command_linux/>

<https://www.tecmint.com/run-linux-command-process-in-background-detach-process/>

<https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/>

<https://www.tecmint.com/screen-command-examples-to-manage-linux-terminals/>

<https://linoxide.com/linux-command/15-examples-screen-command-linux-terminal/>

<https://ryanstutorials.net/linuxtutorial/processes.php>

<https://www.cyberciti.biz/faq/unix-linux-disown-command-examples-usage-syntax/>

<https://linuxize.com/post/ps-command-in-linux/>

<https://www.computerhope.com/jargon/p/pid.htm>

<https://www.tecmint.com/linux-process-management/>

<https://www.geeksforgeeks.org/processes-in-linuxunix/>

<https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/>

<https://linuxhint.com/ps_command_linux-2/>

<https://www.quora.com/What-is-the-difference-between-ps-elf-and-ps-aux-in-Linux>

<https://www.geeksforgeeks.org/top-command-in-linux-with-examples/>

<https://www.tecmint.com/12-top-command-examples-in-linux/>

<https://www.tutorialspoint.com/unix/unix-signals-traps.htm>

<https://www.geeksforgeeks.org/kill-command-in-linux-with-examples/>

<https://www.linux.com/tutorials/how-kill-process-command-line/>

<https://www.linode.com/docs/tools-reference/tools/use-killall-and-kill-to-stop-processes-on-linux/>

<https://www.geeksforgeeks.org/free-command-linux-examples/>

<https://www.geeksforgeeks.org/linux-uptime-command-with-examples/>

<https://linuxhint.com/load_average_linux/>

.

Copy

# 103.6. Modify process execution priorities

**Weight:** 2

**Description:** Candidates should should be able to manage process execution priorities.

**Key Knowledge Areas:**

* Know the default priority of a job that is created
* Run a program with higher or lower priority than the default
* Change the priority of a running process

**Terms and Utilities:**

* nice
* ps
* renice
* top

Linux, like most modern operating systems, can run multiple processes. It does this by sharing the CPU and other resources among the processes. If one process can use 100 percent of the CPU, then other processes may become unresponsive. We’ll introduce you to the way Linux assigns priorities for tasks.(We have already talked about ps and top commands in previous section)

### nice

In Linux we can set guidelines for the CPU to follow when it is looking at all the tasks it has to do. These guidelines are called ***niceness*** or ***nice value.*****(**weuse ubuntu 16 here)

Copy

```
top - 03:15:57 up 3 days, 20:17,  1 user,  load average: 0.03, 0.01, 0.00
Tasks: 235 total,   1 running, 171 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.1 us,  1.4 sy,  0.0 ni, 96.2 id,  0.3 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :   985080 total,   116124 free,   436040 used,   432916 buff/cache
KiB Swap:  1045500 total,   374404 free,   671096 used.   335984 avail Mem

   PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
   949 root      20   0  496000  30668  15864 S  2.0  3.1  11:17.57 Xorg
 55222 user1     20   0  667544  18964  12132 S  1.3  1.9   0:22.76 gnome-term+
  2112 user1     20   0 2346400  53212  24204 S  0.7  5.4  36:38.03 compiz
  1916 user1     20   0  477868   5304   3464 S  0.3  0.5   0:07.53 ibus-ui-gt+
  1948 user1     20   0  188388   1384   1108 S  0.3  0.1   0:18.18 ibus-engin+
 55210 root      20   0    6536    600    572 S  0.3  0.1   0:19.60 ping
 64405 root      20   0   41920   3760   3040 R  0.3  0.4   0:00.13 top
     1 root      20   0  185244   3996   2500 S  0.0  0.4   0:08.10 systemd
```

**NI column**  Represents a Nice Value of task. The Linux niceness scale goes from -20 to 19. The lower the number the more priority that task gets. If the niceness value is high number like 19 the task will be set to the lowest priority and the CPU will process it whenever it gets a chance. The default nice value is **zero**.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LrmyUtqvnx57s7ZxPl2%252F-Lrn6OAk9p7NuxEAe7io%252Fmodifyprocess-nice.jpg%3Falt%3Dmedia%26token%3Dbdfc4ccd-3deb-46ec-8d92-5743b93c1679&width=768&dpr=4&quality=100&sign=a06b7cdc&sv=2)

Different OS distributions can have different default values for new processes. The simplest method to determine the default value is to simply run the nice command with no arguments. By default nice will simply return the current niceness value

#### Determining the niceness value of a current process

The niceness value of current processes are also pretty simple to find as they are visible in the ps command’s full long format :

> `-f` do full-format listing and `-l` is for Long format.

#### Changing the nice value of a new process

Changing the niceness value of a new process is fairly simple. The nice command itself will run the supplied command with the desired niceness value.(Please note we are logged in as a user here)

note: root user is the only person who can start an application with the high priority (lower than zero), but, any body can start an application with low priority (higher than zero).

if we try to run an application with high priority without root permissions, it would trough an error and starts application with priority zero.

Now lets try the last command using root :

it good to know that nice command has there different syntax:

nice command example

Description

nice --20 application

highest priority

nice --15 application

very high

nice -10 application

medium low

nice -19 application

lowest

#### Changing the nice value of a running process

### renice

To change the niceness of a running process to a negative value we will use the `renice` command again.

It is important to note that changing a processes niceness value to a negative value requires root privileges. As the effects of giving a process a higher priority could have detrimental effects on a system.

> user can only raise nice level.

we can also use -p option before giving PID, but that is not necessary.

renice command example

renice -20 -p PID

highest priority

renice -15 -p PID

very high

renice 10 -p PID

medium low

renice 19 -p PID

lowest

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-103-6/>

<https://www.nixtutor.com/linux/changing-priority-on-linux-processes/>

<https://bencane.com/2013/09/09/setting-process-cpu-priority-with-nice-and-renice/>

<https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/>

.

Copy

# 103.7. Search text files using regular expressions

**Weight:** 2

**Description:** Candidates should be able to manipulate files and text data using regular expressions. This objective includes creating simple regular expressions containing several notational elements. It also includes using regular expression tools to perform searches through a filesystem or file content.

**Key Knowledge Areas:**

* Create simple regular expressions containing several notational elements
* Use regular expression tools to perform searches through a filesystem or file content

**Terms and Utilities:**

* grep
* egrep
* fgrep
* sed
* regex(7)

While we are working with text files, often it will happen that we are looking for a text in text file.We might be looking for something that is not that specific. For example we are looking for "linux" or "Linux" or what ever, that is where regular expression come in handy.(the most important light weight section!)

### Regular Expression

Regular expressions are used when we want to search for specify lines of text containing a particular pattern.Regex can be used in a variety of programs like grep, sed, vi, bash, rename and many more. Here we will use regex with grep command.

A regex pattern uses a **regular expression engine** which translates those patterns.

Linux has two regular expression engines:

* The **Basic Regular Expression (BRE)** engine.
* The **Extended Regular Expression (ERE)** engine.

> There's a difference between basic and extended regular expressions.Some utilities is written to support only basic regular expressions (BRE)and other utilities are written to support extended regular expressions(ERE) as well.Most Linux programs work well with BRE engine specifications, With GNU grep, there is no difference in functionality.

## What makes up regular expressions

There are two types of characters to be found in regular expressions:

* literal characters
* metacharacters

**Literal characters** are standard characters that make up our strings. Every character in this sentence is a literal character. You could use a regular expression to search for each literal character in that string.

**Meta characters** are a different beast altogether; they are what give regular expressions their power. With meta characters, we can do much more than searching for a single character. Meta characters allow us to search for combinations of strings and much more.

## grep

grep stands for **g**eneral **r**egular **e**xpression **p**arser**.** The grep filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern.grep is a utility that can benefit a lot from regular expressions.

Lets see some examples:

command

description

echo "linux is my os" | grep l

**l**inux is my os

echo "linux is my os" | grep i

l**i**nux **i**s my os

**Concatenation**

Concatenating two regular expressions creates a longer expression.

regex

match

echo "aa ab ba aaa bbb AB BA" | grep a

**aa a**b b**a** **aaa** bbb AB BA

echo "aa ab ba aaa bbb AB BA" | grep ab

aa **ab** ba aaa bbb AB BA

### Extended Regular Expressions

**Repetition**

* The **\***  means preceding item will be matched **0** **or more** times.
* The **+** means preceding item will be matched **1 or more** times.
* The **?** means preceding item will be matched, **0 or 1** time.

#### Globbing and Regex: So Similar, So Different

Beginners sometimes tend to confuse **wildcards**(globbing) with **regular expressions** when using grep but they are not the same.
**Wildcards** are a feature provided by the shell to expand file names whereas **regular expressions** are a text filtering mechanism intended for use with utilities like grep, sed and awk.

Special Character

Meaning in Globs

Meaning in Regex

**\***

zero or more characters

zero or more of the character it follows

**?**

single occurrence of any character

zero or one of the character it follows but not more than 1

**.**

literal "." character

any single character

In order to avoid any mistake while using extended regular expressions, use `grep` with `-E` option, `-E` treats pattern as an extended regular expression(ERE).

**double quotes " " :** Also we need to put our extended regex between double quotes, other wise it might be interpreted by shell and gives us different results.

regex

match

echo "aa ab ba aaa bbb AB BA" | grep -E "a\*b"

aa **ab** **b**a aaa **bbb** AB BA

echo "aa ab ba aaa bbb AB BA" | grep -E "a+b"

aa **ab** ba aaa bbb AB BA

echo "aa ab ba aaa bbb AB BA" | grep -E "a?b"

aa **ab** **b**a aaa **bbb** AB BA

This is a point where egrep comes to play:

## egrep

**egrep** is a pattern searching command which belongs to the family of grep functions. It works the same way as `grep -E` does. It treats the pattern as an extended regular expression and prints out the lines that match the pattern. If there are several files with the matching pattern, it also displays the file names for each line.

**Options:** Most of the options for this command are same as grep.

So instead of using grep -E command in above we can use egrep easily.

#### Curly Braces

Curly braces enable us to specify the number of existence for a pattern, it has three formats:

* **{N}** meanspreceding item is matched *exactly* **N times**.
* **{N,}** means preceding item is matched **N or more times**.
* The **{N,M}** means preceding item is matched *at least* **N** *times, but not more than* **M** *times*.

regex

match

echo "ab aab aaab aaaab ba Ab" | egrep "a{1}b"

**ab** a**ab** aa**ab** aaa**ab** ba Ab

echo "ab aab aaab aaaab ba Ab" | egrep "a{2,}b"

ab **aab** **aaab** **aaaab** ba Abb

echo "ab aab aaab aaaab ba Ab" | egrep "a{1,3}b"

**ab aab aaab** a**aaab** ba Ab

**Any Characters**

The .(dot) is a meta character that stands for any character(except newline `\n` )

* The **.**  Matches **any single character**.

> One of the most commonly used patterns is .**‘\*’**, which matches an arbitrary length string containing any characters (or no characters at all)

regex

match

echo "ac abc aaabbbccc abcz" | egrep "a.\*c"

**ac abc aaabbbccc abc**z

**Anchor Characters**

Anchor Characters or easily Line positioning Characters are used To locate the beginning or ending of a line in a text:

* **^** matches the beginning of the line.
* **$** matches the end of the line.

**Alternation (multiple strings)**

The alternation operator (|) matches either the preceding or following expression. for example :

* **cat|dog** it will match **cat or dog**.

regex

match

echo "cat dog was a cartoon" | egrep "cat|dog"

**cat dog** was a cartoon

### Character Classes

We can match any character with the dot special character, but what if you match a set of characters only? We can use a character class.The character class matches a set of characters if any of them found, the pattern matches.The character class is defined using square brackets [ ]

**Bracket expression**

By placing a group of characters within brackets ("[" and "]"), we can specify that the character at that position can be any one character found within the bracket group.

* **[set\_of\_characters]** Matches any single character in ***set\_of\_characters***. By default, the match is case-sensitive.

regex

match

echo "cat dog was a cartoon" | egrep "cart[o]\*"

cat dog was a **cartoo**n

### Negating Character Classes

What about searching for a character that is not in the character class? To achieve that, precede the character class range with a caret **^.**

* **[^set\_of\_characters]**  *Negation:* Matches any single character that is **not in** ***set\_of\_characters***. By default, the match is case sensitive.

regex

match

echo "cat dog was a cartoon" | grep ".\*[^cartoon]"

**cat dog was a** cartoon

**Range expression**

To specify a range of characters, wecan use the **(-)** **hyphen** symbol, such as 0-9 for digits. Note that ranges are locale dependent.

regex

match

echo "a12345a a54321a 123" | egrep "[a-z]"

**a**12345**a** **a**54321**a** 123

### Special Character Classes (**Named classes)**

Several named classes provide a convenient shorthand for commonly used classes. Named classes open with [: and close with :] and may be used within bracket expressions. Some examples:

* **[[:alnum:]]**  Alphanumeric characters.
* **[[:alpha:]]** Alphabetic characters.
* **[[:blank:]]**  Space and tab characters.
* **[[:digit:]]**  The digits 0 through 9 (equivalent to 0-9).
* **[[:upper:]]** and **[:lower:]**  Upper and lower case letters, respectively.

**regex**

match

echo "a12345a a54321a 123 678 9" | egrep "[[:alpha:]]"

**a**12345**a** **a**54321**a** 123

**Group expressions**

By placing part of a regular expression inside parentheses, we can group that part of the regular expression together.

* **() Groups regular expressions**

regex

match

echo "a12345a a54321a 123 678 9" | egrep "(1a.\*)|(9)"

a12345a a5432**1a 123 678 9**

### **Special Characters**

regex patterns use some special characters. And we can’t include them in your patterns and if we do so, we won’t get the expected result.These special characters are recognized by regex:

**.\*[]^${}\+?|()**

So how we can search for some of them inside a text? That's where fgrep comes to play.

### fgrep

If you don't want the power of regex, it can be very frustrating. This is especially true if you're actually looking for some of the special characters in a bunch of text. You can use the `fgrep` command (or `grep -F`, which is the same thing) in order to skip any regex substitutions. Using `fgrep`, you'll search for exactly what you type, even if they are special characters.

as an example:

### sed

Sed command or **S**tream **Ed**itor is very powerful utility offered by Linux/Unix systems. It is mainly used for **text substitution** , **find & replace** but it can also perform other text manipulations like **insertion**, **deletion**, **search ,** etc.

With **sed**, we can edit complete files without actually having to open it. Sed also supports the use of regular expressions, which makes sed an even more powerful **text manipulation tool**.

We have previously used sed for text substitution, here we want to use regex with that.

`-r, --regexp-extended`  tells sed that we are using **regular expressions** in the script.

By default, sed prints every line. If it makes a substitution, the new text is printed instead of the old one. If you use an optional argument to sed, "sed -n," it will not:

When the "-n" option is used, the "p" flag will cause just the modified line to be printed:

sed is very powerfull tools and that is complicated, we have just take a quick lookat it!

.

.

.

<http://www.grymoire.com/Unix/Regular.html>

<https://www.linux.com/tutorials/introduction-regular-expressions-new-linux-users/>

<https://linux.die.net/Bash-Beginners-Guide/sect_04_01.html>

<https://dzone.com/articles/35-examples-of-regex-patterns-using-sed-and-awk-in>

<https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux#regular-expressions>

<https://www.linuxnix.com/10-file-globbing-examples-linux-unix/>

<https://www.linuxjournal.com/content/globbing-and-regex-so-similar-so-different>

<https://www.zyxware.com/articles/4627/difference-between-grep-and-egrep>

<https://www.geeksforgeeks.org/fgrep-command-in-linux-with-examples/>

<https://www.linuxtechi.com/20-sed-command-examples-linux-users/>

<http://www.grymoire.com/Unix/Sed.html>

<https://www.linuxtechi.com/20-sed-command-examples-linux-users/>

.

Copy

# 103.8. Perform basic file editing operations using vi

**Weight:** 3

**Description:** Candidates should be able to edit text files using vi. This objective includes vi navigation, basic vi modes, inserting, editing, deleting, copying and finding text.

**Key Knowledge Areas:**

* Navigate a document using vi
* Use basic vi modes
* Insert, edit, delete, copy and find text

**Terms and Utilities:**

* vi
* /, ?
* h,j,k,l
* i, o, a
* c, d, p, y, dd, yy
* ZZ, :w!, :q!, :e!

The need to learn how to use text editors in Linux is indisputable. Every system administrator and engineer deal with configuration (plain text) files on a daily basis, and most times this is done purely using one or more tools from a command-line interface (such as **nano**, **vi**, or **emacs**).

### vi

The vi editor (visual editor) is almost certainly on every Linux and UNIX system. In fact, if a system has just one editor, it’s probably vi, so it’s worth knowing your way around in vi.

Using vi editor, we can edit an existing file or create a new file from scratch. we can also use this editor to just read a text file.

> vi editor is great even trough ssh sessions!

#### vi or vim ?

Most Linux distributions now ship with the vim (for **V**i **IM**proved) editor rather than classic vi. Vim is upward compatible with vi and has a graphical mode available (gvim) as well as the standard vi text mode interface. The `vi` command is usually an alias or symbolic link to the vim program.

There are several versions of vim: tiny, small, normal, big, and huge. We can find out what version of vim we are running and what features are included by using the command(ubuntu 16.04 here ):

Inorder to read, create or modify a file with vi, give the file name to it:

**if you just type vi(m) and hit enter, the vi(m) version will be displayed:**

Okey lets start learning vi(m):

### vi modes

Vim actually has three modes: **insert mode**, **command mode**, and **escape**  **(last-line) mode**. Let’s start with the default mode you’ll see when you start up Vim–command mode.

* **command mode** : When you run vim filename to edit a file, Vim starts out in command mode. This means that all the alphanumeric keys are bound to commands, rather than inserting those characters.(save, quit, search/replace, navigate around, execute macros,...)
* **insert mode** : *To enter the insert mode, type i (for “insert”)* and now the keys will behave as you’d expect. You can type normally until you want to make a correction, save the file, or perform another operation that’s reserved for command mode or escape (last-line) mode. *To get out of insert mode, hit the Escape key.*
* **escape (last-line) mode** : Once you press Escape, you’re in command mode again. What if you’d like to save your file or search through your document? No problem, *press : and Vim will switch to escape (last-line) mode*. Vim is now waiting for you to enter a command like :w to write the file or :q to exit the editor.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lsv9B3A_1GFWOJW4TM9%252F-LsvFsL2vsccLOMbdqJd%252Fperformbasicfileop-vimodes.jpg%3Falt%3Dmedia%26token%3D218e57e3-4f5b-4802-ba85-6759e1a293f8&width=768&dpr=4&quality=100&sign=8d5891dd&sv=2)

If that all sounds complicated, it’s really not. It does take a few days to start training your brain to move between the modes and memorizing the most important keys for movement, commands, and so on.

#### Moving the cursor

The first thing you’ll want to learn is how to move around a file. When you’re in command mode, you’ll want to remember the following keys and what they do:

Key

function

h

Move left one character on the current line

j

Move down to the next line

k

Move up to the previous line

l

Move right one character on the current line

w

Move to the next word on the current line

e

Move to the next end of word on the current line

b

Move to the previous beginning of the word on the current line

Crtl-f

Scroll forward one page

Ctrl-b

Scroll backward one page

> If you type a number before any of these commands, then the command will be executed that many times. This number is called a *repetition count* or simply *count*. For example, 5h will move left five characters. You can use repetition counts with many vi commands.

#### Jumping

key

function

H

move to top of screen

M

move to middle of screen

L

move to bottom of screen

key

function

W

jump forwards to the start of a word (words can contain punctuation)

E

jump forwards to the end of a word (words can contain punctuation)

B

jump backwards to the start of a word (words can contain punctuation)

key

function

0

jump backwards to the start of line

^

jump to the first non-blank character of the line

$

jump to the end of the line

g\_

jump to the last non-blank character of the line

gg

go to the first line of the document

G

go to the last line of the document

### Editing text

Now that you can open a file in vi, move around it and get out, it’s time to learn how to edit the text in the file

key( for inserting)

function

i

insert text before cursor, until hit

I

insert text at beginning of current line, until hit

a

append text after cursor, until hit

A

append text to end of current line, until hit

o

open and put text in a new line below current line, until hit

O

open and put text in a new line above current line, until hit

key(for changing)

function

r

replace single character under cursor (no needed)

R

replace characters, starting with current cursor position, until hit

cw

change the current word with new text, starting with the character under cursor, until hit

cNw

change N words beginning with character under cursor, until hit; e.g., c5w changes 5 words

C

change (replace) the characters in the current line, until hit

cc

change (replace) the entire current line, stopping when is hit

Ncc or cNc

change (replace) the next N lines, starting with the current line, stopping when is hit

key (for deleting)

function

x

delete single character under cursor

Nx

delete N characters, starting with character under cursor

dw

delete the single word beginning with character under cursor

dNw

delete N words beginning with character under cursor; e.g., d5w deletes 5 words

d^

delete start of line till the cursor

d$ and D

delete the remainder of the line, starting with current cursor position

dd

delete entire current line

Ndd or dNd

delete N lines, beginning with the current line; e.g., 5dd deletes 5 lines

key(for cutting and pasting)

function

yy

copy (yank, cut) the current line into the buffer

Nyy or yNy

copy (yank, cut) the next N lines, including the current line, into the buffer

p

put (paste) the line(s) in the buffer into the text after the current line

P

put (paste) the line(s) in the buffer into the text before the current line

### searching

key

function

/string

search forward for occurrence of string in text

? string

search backward for occurrence of string in text

n

move to next occurrence of search string

N

move to next occurrence of search string in opposite direction

### replacing

key

function

:s/old/new/

replace first old with new in just that line

:s/old/new/g

replace all old with new in just that line

:%s/old/new/g

replace all old with new throughout file

:%s/old/new/gc

replace all old with new throughout file with confirmations

:%s/old/new/gic

same as above but case insensitive

:noh

remove highlighting of search matches

### Exiting

If you’re in insert mode, hit Escape. Then enter : and you’ll see a line at the bottom of the screen with a cursor ready to take input.

key

function

:w

That will write the file to the existing filename,but don't exit.

:w *file*

If you don’t have a filename or want to write out to a different *file name*

:q

quit (fails if there are unsaved changes)

:q!

Quit editing without saving.

:wq

write (save) and quit (throw and error if file is not writable)

:wq!

try to write and quit (if it is not writable, quit without saving! )

ZZ and :x

Exit and save the file if modified

q! or ZQ

quit and throw away unsaved changes

Press ESC to return back to the normal command mode!

> When you want to write and exit from a file consider you permissions, the bellow command write out the current file using sudo:
>
> :w !sudo tee %
>
> * :w – Write a file (actually buffer).
> * !sudo – Call shell with sudo command.
> * tee – The output of write (vim :w) command redirected using tee.
> * % – The % is nothing but current file name.

### reloading

key

function

:e

(short for `:edit`) reload the file from the disk

:e!

it will discard local changes and reload.

### VIM Tip : running external commands in a shell

It usuaslly happens that we need to run a command in shell to see the result of file which we are edditing. It could be happened in two ways:

1.We could suspend your session (ctrl-Z), and then run the command in your shell.That’s a lot of keystrokes, though !

2.So, instead, you could use vim’s built-in “run a shell command”:

> :!cmd Run a shell command, shows you the output and prompts you before returning to your current buffer.

### help

Need help? you can use `:help` or `:help keyword` and vim will open help for keyword.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-103-8/>

<https://www.tecmint.com/learn-vi-and-vim-editor-tips-and-tricks-in-linux/>

<https://www.geeksforgeeks.org/vi-editor-unix/>

<https://www.linux.com/tutorials/vim-101-beginners-guide-vim/>

<https://vim.rtorr.com/>

<https://www.cs.colostate.edu/helpdocs/vi.html>

<https://www.endpoint.com/blog/2009/03/10/vim-tip-of-day-running-external>

.

Copy

# 104.1. Create partitions and filesystems

## **104.1 Create partitions and filesystems**

**Weight:** 2

**Description:** Candidates should be able to configure disk partitions and then create filesystems on media such as hard disks. This includes the handling of swap partitions.

**Key Knowledge Areas:**

* Manage MBR partition tables
* Use various mkfs commands to create various filesystems such as:
* ext2/ext3/ext4
* XFS
* VFAT
* Awareness of ReiserFS and Btrfs
* Basic knowledge of gdisk and parted with GPT

**Terms and Utilities:**

* fdisk
* gdisk
* parted
* mkfs
* mkswap

### BIOS

The Basic Input/Output System (BIOS), (also known as System BIOS, ROM BIOS ) is a standard for defining a firmware interface. The BIOS software is built into the PC, and is the first software run by a PC when powered on.

The fundamental purposes of the BIOS are to initialize and test the system hardware components, and to load a bootloader or an operating system from a mass memory device.

### UEFI

The Unified Extensible Firmware Interface (UEFI) is a specification that defines a software interface between an operating system and platform firmware. UEFI is meant to replace the Basic Input/Output System (BIOS) firmware interface. In practice, most UEFI images provide legacy support for BIOS services. UEFI can support remote diagnostics and repair of computers, even without another operating system!

> The original EFI (Extensible Firmware Interface) specification was developed by Intel. UEFI is still not widespread and major hardware companies have switched over almost exclusively to UEFI use. Many older and less expensive motherboards also still use the BIOS system.

### MBR

A master boot record (MBR) is a special type of boot sector at the very beginning of partitioned computer mass storage devices like fixed disks or removable drives.

The MBR holds the information on how the logical partitions, containing file systems, are organized on that medium. Besides that, the MBR also contains executable code to function as a loader for the installed operating system—usually by passing control over to the loader's second stage. This MBR code is usually referred to as a boot loader.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LqAGZBTzViD1dkOj2A0%252F-LqAGbXFUGnPdIROQR2n%252Fbootloader-mbr.jpg%3Fgeneration%3D1569999728181812%26alt%3Dmedia&width=768&dpr=4&quality=100&sign=4996336a&sv=2)

**Master Boot records has some short comings:**

* MBR puts all information in first sector of hard disk so if any problem ocures for that sectore, system won't be able to boot up.
* MBR contains only four entries (slots) for four Primary partitions, one of which can be an Extended partition. This partition will contain unallocated space within it where we can create unlimited number of Logical partitions.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LxXp8KPLaqG3N8egRdZ%252F-LxXq3KoSH2RwxmR2cOY%252Fcreatepartition-mbrpart.jpg%3Falt%3Dmedia%26token%3D77188eb6-4fbc-44ce-a3d2-fd488fb8d0b7&width=768&dpr=4&quality=100&sign=aa7f31c&sv=2)

* The organization of the partition table in the MBR limits the maximum addressable storage space of a disk to 2 TB.

Therefore, the MBR-based partitioning scheme is in the process of being superseded by the GUID Partition Table (GPT) scheme in new computers. A GPT can coexist with an MBR in order to provide some limited form of a backwards compatibility for older systems.

### GPT

GUID Partition Table (GPT) is a standard for the layout of the partition table on a physical hard disk, using globally unique identifiers (GUID).

Although it forms a part of the Unified Extensible Firmware Interface (UEFI) standard, it is also used on some BIOS systems because of the limitations of master boot record (MBR) partition tables.

### MBR vs GBT

MBR(Master Boot Record)

GPT(GUID Partition Table)

Since 1983

New 2005-...

lives on first sector

Stored in multiple locations on Drive

Limited to 4 partitions per disk

Limited to 2 TB partitions

Supports 128 partitions per disk

Supports 18EX partition

> Both GPT disk and MBR disk can be basic or dynamic.

### BIOS vs UEFI

BIOS(Basic Input/Output System)

UEFI(Unified Extensible Frimware Interface)

Only Supports MBR( So GPT itself acts like MBR!)

Native GPT support

Sees GPT as a drive with a single MBR partition

Usually need to run in legacy mode ti support MBR

Usually, MBR and BIOS **(MBR + BIOS)**, and GPT and UEFI **(GPT + UEFI)** go hand in hand. This is required for some systems (Windows), while optional for others (Linux).

### Block devices

A block device is an abstraction layer for any storage device that can be formatted in fixed-size blocks and blocks should be able to be access randomly.

Examples of block devices include the first IDE or SATA hard drive on our system (/dev/sda or /dev/hda) or the second SCSI, IDE, or USB drive (/dev/sdb). Use the `ls -l` command to display /dev entries.

The first character on each output line is **b** for a **block** device, such as floppy, CD drive, IDE hard drive, or SCSI hard drive; and **c** for a **character** device, such as a or terminal (tty) or the null device.

#### Disk Partitioning

Now that we are introduced you to hard drive layouts (MBR & GPT) , lets learn how to create MBR partitions using fdisk and GPT partitions using gdisk.

### fdisk

**fdisk** also known as format disk is a dialog-driven command in Linux used for creating and manipulating disk partition table. It is used for the view, create, delete, change, resize, copy and move partitions on a hard drive using the dialog-driven interface.
fdisk allows us to create a maximum of four primary partitions and the number of logical partition depends on the size of the hard disk you are using. It allows the user:

* To Create space for new partitions.
* Organizing space for new drives.
* Re-organizing old drives.
* Copying or Moving data to new disks(partitions)

The first thing to do before doing any thing with the disks and partition is to view basic details about all available partition in the system using `-l` option(ubuntu 16.04):

as you can see we have two disk drives (sda,sdb) sda has some partitions on it but sdb is row.

* **Boot** : The Boot column shows that the first partition, /dev/sda1, has an asterisk **(\*)** indicating that this partition contains the files required by the boot loader to boot the system.
* **Start and End** : The start and end columns list the starting and ending sectors of each partition.
* **Blocks** : The blocks column lists the number of blocks allocated to the partition.
* **Id and System** : These columns identify the partition type.

Viewing Partition(s) on a Specific Disk (sda) :

Lets start interactive mode and see all available commands (sdb):

okey creating partion:

next we need to specify partition type based on the future use we have considered for:

**Partition Types**

The partition types can be displayed and changed by using the fdisk utility. A partial list (most commonly used) of partition types are:
**83: Linux
82: Linux swap
5: Extended
8e: Linux LVM**

and use -p option inorder to print partition table:

fdisk does not write any changes on hard disk until we ask it using `w` switch, if you are not sure use `q` to quit and hard disk stays untouched!

use -d for delete a partition bu be care full!

> To see the help message and listing of all options, use fdisk -h command.

### gdisk

We can Manage GPT Partitions with gdisk. like fdisk, gdisk is a text-mode menu-driven program for creation and manipulation of partition tables. It will automatically convert an old-style Master Boot Record (MBR) partition table to the newer Globally Unique Identifier (GUID) Partition Table (GPT) format, or will load a GUID partition table.

### parted

The `parted` command is a partition editor that will work with both MBR and GPT formatted disks.

### File System

Linux File System or any file system generally is a layer which is under the operating system that handles the positioning of your data on the storage, without it; the system cannot knows which file starts from where and ends where.

### **File system types**

Linux supports several different file systems. Each has strengths and weaknesses and its own set of performance characteristics.

**Ext, Ext2, Ext3, Ext4, JFS, XFS, btrfs and swap**

One important attribute of a filesystem is journaling

**What is journaling?**

Journaling is designed to prevent data corruption from crashes and sudden power loss. Let’s say your system is partway through writing a file to the disk and it suddenly loses power. Without a journal, your computer would have no idea if the file was completely written to disk. The file would remain there on disk, corrupt.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LxR7luULR8_XmJ7NnPH%252F-LxRDcMVNK4jB3zXLUCQ%252Fcreatepartition-journaling.jpg%3Falt%3Dmedia%26token%3Dbf5b6b55-ca03-459c-a45a-d3a50e46dfaf&width=768&dpr=4&quality=100&sign=dc88699a&sv=2)

With a journal, your computer would note that it was going to write a certain file to disk in the journal, write that file to disk, and then remove that job from the journal. If the power went out partway through writing the file, Linux would check the file system’s journal when it boots up and resume any partially completed jobs. This prevents data loss and file corruption.

Journaling does slow disk write performance down a tiny bit, but it’s well-worth it on a desktop or laptop.

Which File System is perfect for you?

Generally, a journaling filesystem is preferred over a non-journaling one when you have a choice. You may also want to consider whether your chosen filesystem supports *Security Enhanced Linux* (or SELinux).

Following is a brief summary of the types you need to know about for the LPI exam**:**

Format

Description

**ext2**

(1993)

The ext2 filesystem (also known as the *second extended filesystem*) was developed to address shortcomings in the Minix filesystem used in early versions of Linux. It has been used extensively on Linux for many years. There is no journaling in ext2, and it has largely been replaced by ext3 and more recently ext4.

1. Maximum file size is **16GB – 2TB**.

\*It’s being used for normally Flash based storage media like **USB Flash drive**, **SD Card** etc.

**ext3**

(2001)

The ext3 filesystem adds journaling capability to a standard ext2 filesystem and is therefore an evolutionary growth of a very stable filesystem. It offers reasonable performance under most conditions and is still being improved. Because it adds journaling on top of the proven ext2 filesystem, it is possible to convert an existing ext2 filesystem to ext3 and even convert back again if required.

1. Max file size **16GB – 2TB**.
2. was integrated in **Kernel 2.4.15** with journaling feature

**ext4**

(2008)

The ext4 filesystem started as extensions to ext3 to address the demands of ever larger file systems by increasing storage limits and improving performance. Some of the changes from ext3 are:

1. Max file size **16GB to 16TB**.
2. was included in the **2.6.28 kernel**.
3. Ext4 file system have option to **Turn Off** journaling feature.
4. Other features like **Fast FSCK** etc.

**ReiserFS**

ReiserFS is a B-tree-based filesystem that has very good overall performance, particularly for large numbers of small files. has journaling. no longer in active development, does not support SELinux and has largely been superseded by Reiser4 whose future is unclear.

**XFS**

XFS is a filesystem with journaling. It comes with robust features and is optimized for scalability. XFS aggressively caches in-transit data in RAM, great if you have an uninterruptible power supply.

**btrfs**

btrfs (B-Tree file system) was initially developed by Oracle(GPL).It is a new copy-on-write filesystem for Linux aimed at implementing advanced features(snapshots,compression,...) while focusing on fault tolerance, repair, and easy administration.Designed to handle large files efficiently and handle filesystems spread across multiple devices.

**vfat**

(also known as *FAT32*) no journaling, lacks many features required for a full Linux filesystem implementation. useful for exchanging data between Windows and Linux systems . Do **not** use this filesystem , except for sharing data .

\*If you unzip or untar a Linux archive on a vfat disk, you will lose permissions, such as execute permission, and you will lose any symbolic links that may have been stored in the archive.

**swap**

Swap space must be formatted for use as swap space, but it is not generally considered a filesystem.

We must create a file system before you can use any data storage device connected to a Linux computer.

### partitioning

Linux uses the `mkfs` command to create filesystems and `mkswap`command to make swap space.

Before you start modifying partitions, there are some important things to remember. You risk losing your existing data if you do not follow these guidelines:

1. Back up important data before you start
2. Do not change partitions that are in use
3. Know your tool
4. Stop if you do make a mistake

Linux uses the `mkfs` command to create filesystems and `mkswap`command to make swap space

### mkfs

The mkfs (make filesystem) command is used to create a filesystem.

The `mkfs` command is actually a front end to several filesystem-specific commands such as `mkfs.ext3` for ext3, `mkfs.ext4` for ext4 and `mkfs.btrfs` for btrfs.

various forms of some commands. mke2fs, mkfs.ext2, and mkfs.ext3 are all the same file, while mkfs.msdos and mkfs.vfat are usually symbolic links to mkdosfs.

In order to build the filesystem using mkfs command, the required arguments are filesystem-type and device-filename:

We can either use mkfs.*fstype* commands `mkfs.ext3 /dev/sdb1`  or we can use mkfs via `-t` option to specify the format `mkfs -t ext3 /dev/sdb1` and both would have the same results.

If we want to assign a label to the partition during format progress we should use -L labelname with that : `mkfs -t ext3 -L MyData /dev/sdb1`

For mounting Formatted partition we can either use Partition label or **UUID**. **UUID** *is a unique identifier used in partitions to uniquely identify partitions*. to get the UUID of recent created partition try : `blkid /dev/sdb1`

Partition

Format Type

Sample Command

Notes

/dev/sdb1

ext4

mkfs -t ext4 -L data /dev/sdb1

Assigns Label,same as mkfs.ext4

/dev/sdb2

xfs

mkfs -t xfs -i size=512 /dev/sdb2

telling it to have larger inodes (normal is 256) it helps Selinux

/dev/sdc1

ReiserFS

mkfs -t reiserfs /dev/sdc1

Or you can use `mkreiserfs` command.

/dev/sdc2

vFAT

mkfs -t vfat /dev/sdc2

Or you can use `mkfs.vfat` command

/dev/sdc3

Btrfs

mkfs -t btrfs /dev/sdc3

Or you can use `mkfs.btrfs` command

### mkswap

`mkswap`command makes swap space on a device or in a file.

The device argument will usually be a disk partition (something like /dev/sdb1) but can also be a file.

The Linux kernel does not look at partition IDs, but many installation scripts will assume that partitions of hex type 82 (LINUX\_SWAP) are meant to be swap partitions.

So in order to make a swap space first create a partition using fdisk via partition type 82 and then use mkswap:

Using the created partition as a swap space requires further step which will be discussed in later lessons.

that's all!

.

.

.

<https://wiki.manjaro.org/index.php?title=Some_basics_of_MBR_v/s_GPT_and_BIOS_v/s_UEFI>

<https://developer.ibm.com/tutorials/l-lpic1-104-1/>

<https://www.geeksforgeeks.org/file-systems-in-operating-system/>

<https://likegeeks.com/linux-file-system/>

<https://developer.ibm.com/tutorials/l-lpic1-102-1/>

<https://www.computerhope.com/jargon/p/partition.htm>

<https://www.geeksforgeeks.org/fdisk-command-in-linux-with-examples/>

<https://www.tecmint.com/what-is-ext2-ext3-ext4-and-how-to-create-and-convert-linux-file-systems/>

<https://www.howtogeek.com/howto/33552/htg-explains-which-linux-file-system-should-you-choose/>

<https://developer.ibm.com/tutorials/l-lpic1-104-1/>

<https://jadi.gitbooks.io/lpic1/content/1041_create_partitions_and_filesystems.html>

.

Copy

# 104.2. Maintain the integrity of filesystems

**Weight:** 2

**Description:** Candidates should be able to maintain a standard filesystem, as well as the extra data associated with a journaling filesystem.

**Key Knowledge Areas:**

* Verify the integrity of filesystems
* Monitor free space and inodes
* Repair simple filesystem problems

**Terms and Utilities:**

* du
* df
* fsck
* e2fsck
* mke2fs
* debugfs
* dumpe2fs
* tune2fs
* XFS tools (such as xfs\_metadump and xfs\_info)

In cases when your system crashes or loses power, your filesystems may be left in an inconsistent state, with some changes completed and some not.

Operating with a damaged filesystem is not a good idea as you are likely to further compound any existing errors.We’ll take a look at some tools to help us manage such problems.

You should always back up your filesystem before attempting any repairs!

### fsck

The main tool for checking and repairing filesystems is `fsck`, which, like `mkfs`, is really a front end to filesystem-checking routines for the various filesystem types.

> Some of these are just links to e2fsck command and they are the same

The fsck command in Linux allows us to manually check for file system inconsistencies, Fsck command needs to be run with superuser privileges or **root**(ubuntu 16.04 here):

In order to use fsck the partition should be unmounted, otherwise it might cause damages!

Lets simply check file system on an unmounted ext3 partition (sdb1) and try to fix errors :

This command will attempt to check **/dev/sdb1**, and report any errors it finds.The exit code returned by fsck is one of following conditions:

* 0 No errors
* 1 Filesystem errors corrected
* 2 System should be rebooted
* 4 Filesystem errors left uncorrected
* 8 Operational error
* 16 Usage or syntax error
* 32 Checking canceled by user request
* 128 Shared-library error

`-N` option just shows what would be executed but do not attempt to repair them:

`-n`  causes these commands not to fix anything and just show what was going to be done:

Normally, **fsck** will skip parts of the filesystem marked as "clean" — meaning all pending writes were successfully made. The **-f** ("force") option specifies that **fsck** should check parts of the filesystem even if they are not "dirty". The result is a less efficient, but a more thorough check.

**What are inodes?**

As we said Linux treating everything as a file (even the hardware devices). The keyboard, mouse, printers, monitor, hard disk, processes, even the directories are treated as files in Linux. The regular files contain data such as text (text files), music, videos (multimedia files) etc. Set aside the regular data, there are some other data about these files, such as their size, ownership, permissions, timestamp etc. This meta-data about a file is managed with a data structure known as an inode (index node).

> We can also check file systems using their UUID.(use blkid command ):

fsck command example

description

fsck -M /dev/sda1

prevents running fsck on mounted filesystem

fsck -t ext3 /dev/sdb1

Check Only a Specific Filesystem Type

fsck -y -f /dev/sdb1

pass “yes” to all the questions to fix

> For checking a XFS filesystem, wehave to use xfs\_check command

## Advanced tools

There are several more advanced tools that we can use to examine or repair a filesystem.

#### Tools for ext2 and ext3 filesystems

* **tune2fs:**Adjusts parameters on ext2 and ext3 filesystems. Use this to add a journal
* **dumpe2fs:** shows all super blocks info
* **debugfs:** interactive file system editor

**Super Blocks**

You may be wondering how all these checking and repairing tools know where to start. Linux and UNIX filesystems usually have a *superblock*, which describes the filesystem *metadata*, or data describing the filesystem itself. This is usually stored at a known location, frequently at or near the beginning of the filesystem, and replicated at other well-known locations. You can use the `-n` option of `mke2fs` to display the superblock locations for an existing filesystem.

### tune2fs

The ext family of file systems also has a utility called `tune2fs`, which can be used to inspect information about the block count as well as information about whether the filesystem is journaled (ext3 or ext4) or not (ext2).

The tune2fs command allows you to set assorted filesystem parameters on a mounted ext2 or ext3 filesystem.

`-l` shows contents of the filesystem superblock, including the current values of the parameters:

> The command can also be used to set many parameters or convert an ext2 filesystem to ext3 by adding a journal using -j option: `tune2fs -j /dev/sdd1`

Also we can use tune2fs for changing or modifying partition label:

### dumpe2fs

dumpe2fs command is used to print the super block and blocks group information for the filesystem present on device.

printed information may be old or inconsistent when it is used with a mounted filesystem. Don’t forget to unmount your partition before using this command.

### debugfs

Is an interactive filesystem debugger. Use it to examine or change the state of an ext2 or ext3 filesystem. It opens the filesystem in read-only mode unless we tell it not to (with `-w` option).

if the filesystem is mounted, is alright for inspecting, but **Do not** attempt repair on a mounted filesystem.

### xfs\_info

xfs file system has it's own family commands. xfs\_info is the same as tune2fs but for xfs.

xfs\_info should be used on a mounted file system.

> xfsprogs package must be installed

xfs command

description

xfs\_info

shows information

xfs\_check

complete check of file system

xfs\_repair

check and fixes problems

xfs\_check -n

same as xfs\_check

obviously xfs\_repair does not work on mounted file system.

> In XFS, you can only extend file system and can not reduce it.

### Monitoring free space

On a storage device, a file or directory is contained in a collection of *blocks*. Information about a file is contained in an *inode.*

> **Reminder :** inodes keeps information such as who the owner is, when the file was last accessed, how large it is, whether it is a directory, and who can read from or write to it. The inode number is also known as the file serial number and is unique within a particular filesystem.

Data blocks and inodes each take space on a filesystem, so we need to monitor the space usage to ensure that your filesystems have space for growth.

### df

The `df` (DiskFree) command is used to find out about the free and used space of file systems.

If no file name is passed as an argument with df command then it shows the space available on all currently **mounted** file systems

-T print file system type, -h, –human-readableprint sizes (in power of 1024):

> `-H` make numbers human readable also (in powers of 1000).

-i list inode information instead of block usage:

> Remember? there is no owner or access rights on vfat filesystems. vfat file format has no inodes!

df command example

description

df -a

dislpay all information includes pseudo, duplicate and inaccessible file systems.

df -Th /home

Display Information of /home File System

df -k or -m or -h

displays information in Bytes, MB , GB

df -t ext3

include specific file system type

df -x xfs

exclude specific file system type

The `df` command gives information about a whole filesystem. Sometimes you might want to know how much space is used by a specific file or directory, To answer this kind of question, we use the `du` command.

### du

The Linux `du` (Disk Usage) command, used to check the information of **disk usage of files and directories** on a machine.

useful switch

description

-a

write count of all files, not just directories

-h

human readable Means we can see sizes in Bytes, KB, MB, GB,...

-c

grand total usage disk space at the last line

–max-depth=N

go N or fewer sub directories further

-s

display only total for each directory

**--time** option is used to display the last modification time in the output of du.

**--exclude=PATTERN** will exclude files that match PATTERN example: `du -ah --exclude="*.txt" /home/payam`

####

#### summary

Lets take a look at some other repairing tools beside tools which we have learned in this lesson:

file system

command

description

ext

**tune2fs**

Adjusts parameters on ext2 and ext3 filesystems and can set journaling .

ext

**dumpe2fs**

Prints the super block and block group descriptor information for an ext2 or ext3 filesystem.

ext

**debugfs**

Is an interactive filesystem debugger. Use it to examine or change the state of an ext2 or ext3 filesystem.

Reiserfs

**reiserfstune**

Displays and adjusts parameters on ReiserFS filesystems.

Reiserfs

**debugreiserfs**

Performs similar functions to dumpe2fs and debugfs for ReiserFS filesystems.

xfs

**xfs\_info**

Displays XFS filesystem information.

xfs

**xfs\_growfs**

Expands an XFS filesystem

xfs

**xfs\_admin**

Changes the parameters of an XFS filesystem.

xfs

**xfs\_repair**

Repairs an XFS filesystem when the mount checks are not sufficient to repair the system.

xfs

**xfs\_db**

Examines or debugs an XFS filesystem.

btrfs

**btrfs**

Displays many aspects of btrfs filesystem information

btrfs

**btrfsck**

Check btrfs filesystems

btrfs

**btrfs-find-root**

Finds the block that is the root of the btrfs filesystem

btrfs

**btrfs-debug-tree**

Displays btrfs internal metadata

btrfs

**btrfstune**

Tune various btrfs filesystem parameters, and enables or disables some extended features

btrfs

**btrfs-restore**

Attempt to restore files from a damaged btrfs filesystem

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-104-2/>

<https://www.thegeekstuff.com/2012/08/fsck-command-examples/>

<https://www.computerhope.com/unix/fsck.htm>

<https://www.geeksforgeeks.org/file-system-consistency-checker-fsck/><https://www.serverwatch.com/tutorials/article.php/3797306/tune2fs-Makes-It-Easy-to-Play-With-Filesystems.htm><https://jadi.gitbooks.io/lpic1/content/1042_maintain_the_integrity_of_filesystems.html>

<https://linoxide.com/linux-command/linux-inode/>

<https://www.geeksforgeeks.org/dumpe2fs-command-in-linux-with-examples/>

<https://www.geeksforgeeks.org/dumpe2fs-command-in-linux-with-examples/>

<https://www.geeksforgeeks.org/df-command-in-linux-with-examples/>

<https://www.geeksforgeeks.org/df-command-linux-examples/>

<https://www.tecmint.com/how-to-check-disk-space-in-linux/>

<https://www.geeksforgeeks.org/du-command-linux/>

<https://www.geeksforgeeks.org/du-command-linux-examples/>

<https://www.tecmint.com/check-linux-disk-usage-of-files-and-directories/>

With the special thanks of shawn powers.

.

.

Copy

# 104.3. Control mounting and unmounting of filesystems

**Weight:** 3

**Description:** Candidates should be able to configure the mounting of a filesystem.

**Key Knowledge Areas:**

* Manually mount and unmount filesystems
* Configure filesystem mounting on bootup
* Configure user mountable removable filesystems

**Terms and Utilities:**

* /etc/fstab
* /media/
* mount
* umount

In previous lessons we have learn how to partition hard drives and how to format file system on to those partitions. In this section we will learn how to mount and unmount files systems so we can access them, store and retrieves files from the actual hard drive.

### Linux filesystems

The Linux filesystem is one big tree rooted at /, and yet we have filesystems on different devices and partitions. How do we resolve this apparent incompatibility?

The root (/) filesystem is mounted as part of the initialization process. Each of the other filesystems that you create is not usable by Linux system until it is *mounted* at a *mount point*.

## mounting and unmounting

**mount** command is used to mount the filesystem found on a device to big tree structure(**Linux** filesystem) rooted at ‘**/**‘. Conversely, another command **umount** can be used to detach these devices from the Tree.

### mount

> Actually the place we specify as location is mount point. mount point should be exist other wise the device could not be mounted.

With -t option we can specify file system type, how ever it can be omitted as mount command is smart enough to determine file system type!(ubuntu 16.4):

Lets create a directory called "mydisk" as a mount point and mount /dev/sdb1 on that:

When you mount a filesystem over an existing directory, the files on the filesystem you are mounting become the files and subdirectories of the mount point. If the mount point directory already contained files or subdirectories, they are not lost, but are no longer visible until the mounted filesystem is unmounted, at which point they become visible again. It is a good idea to avoid this problem by using only empty directories as mount points.

mount command without any arguments displays all the mounts on the system:

#### mount options

The `mount` command has several options that override the default behavior. For example, we can mount a filesystem read-only by specifying `-o ro`. If the filesystem is already mounted, add `remount:`

> `notes:`

> * Use commas to separate multiple options, such as `remount` and `ro`.
> * When remounting an already mounted filesystem, it suffices to specify either the mount point or the device name. It is not necessary to specify both.
> * You cannot mount a read-only filesystem as read-write. Media that cannot be modified, such as CD-ROM discs, will automatically be mounted read-only.
> * To remount a writable device read-write, specify`-o remount,rw`

mount command examples

description

mount -l

Add the ext2, ext3 and XFS labels in the mount output.

mount -r /dev/sdb1 /mydisk

Mount the file system read-only. Same as -o ro

mount -r /dev/sdb1 /mydisk

Mount the file system read/write. This is the default. It is same as -o rw

mount -L mydata /mydisk/

Mount the partition that has the specified label

mount -U uuid /mydisk

Mount the partition that has the specified uuid

mount -t iso9660 -o ro /dev/cdrom /mnt

Mount a CD-ROM(just in case system didn't that)

mount -o loop /mydisk.iso /mnt

Mount an iso image

`mount -B /mydisk /mysecondplace` :After mounting to a directory the mount point can be changed. We will provide the current mounted point and new mount point in a row with `-B` parameter. This actually does not removes old mount only adds the new directory as the mount.

> All mounts that we create are not permanent and get vanished as system restarted. In order to make a them permanent we need to edit /etc/fstab file.

### umount

Once a file system is mounted, we can use the umount command (without an “n”) to unmount the file system. We can unmount the file system by using umount with the device or the mount point.

> Note that a file system cannot be unmounted when it is busy - for example, when there are open files on it, or when some process has its working directory there, or when a swap file on it is in use.

lets unmount /dev/sdb1 as an example:

### /etc/fstab

In previous sections about Boot Managers we learned in both GRUB and LILO root= parameter tell the boot loader what filesystem should be mounted as root. For GRUB2, this is the`setroot` statement. Once the root filesystem is mounted, the initialization process runs `mount` with the `-a` option to automatically mount a set of filesystems. The set is specified in the file /etc/fstab.

Fstab is operating system’s file system table:

* **file system :**This may be a device name such as /dev/sda1, or a label (LABEL=) or UUID (UUID=).

> > We can either mount using device name, labels or uuid. Which one is better ?Every body can set any labels the he/she wants, Device name might be changed for example if you attach two usb devices, so the best way is using uuid for mounting(use `blkid` command).

* **mount point :** mount point, butFor swap space, this should be the value ‘none’ or ‘swap’.
* **type :** Specifies the type of filesystem. it can be (**ext2,3,4, reiserfs,swap, vfat and ntfs,ISO9660,auto**)
* **option** : Specifies the mount options. Specify defaults if you want default mount options.

* sync/async - All I/O to the file system should be done (a)synchronously.
* auto - The filesystem can be mounted automatically (at bootup, or when mount is passed the -a option). This is really unnecessary as this is the default action of mount -a anyway.
* noauto - The filesystem will NOT be automatically mounted at startup, or when mount passed -a. You must explicitly mount the filesystem.
* dev/nodev - Interpret/Do not interpret character or block special devices on the file system.
* exec / noexec - Permit/Prevent the execution of binaries from the filesystem.
* suid/nosuid - Permit/Block the operation of suid, and sgid bits.
* ro - Mount read-only.
* rw - Mount read-write.
* user - Permit any user to mount the filesystem. This automatically implies noexec, nosuid,nodev unless overridden.
* nouser - Only permit root to mount the filesystem. This is also a default setting.
* defaults - Use default settings. Equivalent to rw, suid, dev, exec, auto, nouser, async.
* \_netdev - this is a network device, mount it after bringing up the network. Only valid with fstype nfs.

> note1: User-mounted filesystems default to noexec unless exec is specified afteruser.
>
> note2: noatime will disable recording of access times. Not using access times may improve performance.

* **dump:** Specifies whether the dump command should consider this ext2 or ext3 filesystem for backups. A value of 0 tells dump to ignore this filesystem.
* **pass:** Non-zero values of pass specify the order of checking filesystems at boot time,( based on check interval and mount count, try `tune2fs -l` ).

Lets add /dev/sdb1 to the /etc/fstab file using UUID and have it even after reboot:

if any thing goes wrong in /etc/fstab , it can cause system failure and system can't boots up! So try `mount -a` in order to try mounting all fstab items before rebooting the system and check for errors.

Ops! that is defaults not default, so try to edit this line again in fstab:

and we are done:

users can only mount and unmount things they are allowed to in /etc/fstab!

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-104-3/>

<https://www.geeksforgeeks.org/mount-command-in-linux-with-examples/>

<https://www.sanfoundry.com/mount-command-usage-example/>

<https://www.poftut.com/linux-mount-command-tutorial-examples/>

<https://www.thegeekdiary.com/how-to-mount-and-umount-a-file-system-in-linux/>

<https://help.ubuntu.com/community/Fstab>

<https://linoxide.com/file-system/understanding-each-entry-of-linux-fstab-etcfstab-file/>

.

Copy

# 104.4. Manage disk quotas

**Weight:** 1

**Description:** Candidates should be able to manage disk quotas for users.

**Key Knowledge Areas:**

* Set up a disk quota for a filesystem
* Edit, check and generate user quota reports

**Terms and Utilities:**

* quota
* edquota
* repquota
* quotaon

Quotas allow us to control disk usage by user or by group. Quotas prevent individual users and groups from using a larger portion of a filesystem than they are permitted, or from filling it up altogether. Here for LPIC2 exam we use quota version 2 with kernel 2.4 and above.

[In this Lesson we will enable and set quota on /dev/sdb1 with ext4 file system.]

#### Checking for the quota package

Quota package is not installed since quotas are not part of the usual default desktop install. Use `dpkg` or `rpm` to check that you have the package installed.

Copy

```
root@ubuntu16-1:~/mydisk# dpkg -l | grep quota
root@ubuntu16-1:~/mydisk# apt install quota
```

#### Adding quota support to /etc/fstab

First step to enable quotas is to add the appropriate options to the filesystem definitions in /etc/fstab, according to whether we want to implement user quotas, group quotas.

option

meaning

usrquota

Enable user quotas

grpquota

Enable group quotas

So for enabling quotas on sdb1 we need to edit the line we have previously added to /etc/fstab (ubuntu 16.04):

After editing /etc/fstab and add quotas, we need to remount the filesystems.

> mount -o remount /dev/sdb1

user quota information is stored in the aquota.user file in the root of the filesystem, and group quota is similarly stored in aquota.group.

after we remount the filesystem, we must create the quota files and enable quota checking.

#### quotacheck

The `quotacheck` command checks the quotas on all filesystems and creates the required aquota.user and aquota.group files if they do not exist. It can also repair damaged quota files.

quotacheck switch

meaning

-a

Check all mounted filesystems in /etc/mtab (except NFS filesystems)

-c

Ignore existing quota files. Run a new scan and write the results to disk

-u

Check user quotas (this is the default)

-g

Check group quotas

-v

Verbose output

aquota.user and aquota.group have been made.

aquota.user and aquota.group are both binary files and should not be edited by hand.

#### Turning quota on /off

### quotaon

The quotaon command enables disk quotas for one or more file systems specified by the FileSystem parameter. The specified file system must be defined with quotas in the /etc/filesystems file, and must be mounted.

The quotaon command looks for the quota.user and quota.group files in the root directory of the associated file system, and will return an error if not found.

The common options `-a`, `-g`, `-u`, and `-v` have the same meaning as for the `quotacheck command`. Similarly, if you do not specify the `-a` option, you must specify a filesystem. Use the `-p` option if you just want to display whether quotas are on or off.

> **quotaoff** announces to the system that the specified filesystems should have any disk quotas turned off.

#### Setting quota limits

### edquota

Quotas are controlled either through binary files in the root of the filesystem or through filesystem metadata. To set a quota for a particular user, use the `edquota` command. This command extracts the quota information for the user from the various filesystems with quotas enabled, creates a temporary file, and opens an editor for us to adjust the quotas.

* use the `-u` option (default) with one or more user names.
* To edit group quotas, use the `-g` with one or more group names.

`edquota` displays my current usage of both 1K blocks and inodes on each of the filesystems that have quota turned on.

You can think of block limits as an approximate limit on the amount of data that a user may store, and inode limits as a limit on the number of files and directories.

There are also soft and hard limits for both block and inode usage. In this example, these are 0, meaning no quota limit is enforced.

**soft limit vs hard limit**

The soft limit is the value at which a user will receive email warnings about being over quota. The hard limit is the value that a user may not exceed.

#### The grace period

Users or groups may exceed their soft limit for a *grace period*, which defaults to **seven days**. After the grace period, the soft limit is enforced as a hard limit. Once the hard limit is reached, some files must be deleted before new files can be created.

Set grace periods using edquota -t`edquota-t`. Again, you will be placed in an editor:

now lets set some hard limits on inodes on /dev/sdb1 for user1:

and lets check it :

For copying one user quota limits to the other user, use -p switch:

`edquota ‑p user1 user2 user2`

#### Quota reports

### quota

The `quota` command with no options displays the quotas for the a user on any filesystems (quota shoud have been set for that user and he or she must have some files on it):

> The `-v` option displays the information for all filesystems that have quota enabled.

Checking user quotas one user at a time is not very useful, so you will want to use the `repquota` command to generate quota reports.

### repquota

repquota stands for report for quota. This will display filesystem usage and quota information on your system.

> `-a` option produces a report for all mounted filesystems that have quota enabled. The `-v` option produces more verbose

That's all!

.

.

.

### Warning users

The `warnquota` command is used to send email warnings to users who are over quota. When a group is over quota, the email is sent to the user specified in /etc/quotagrpadmins for the group. The format of the email is controlled by the file /etc/warnquota.conf. The file /etc/quotatab is used to map names such as /dev/sdc6 to more user-friendly descriptions such as “Shared EXT3 filesystem.” Normally `warnquota` is run periodically as a `cron` job( will be discussed later).

.

<https://developer.ibm.com/tutorials/l-lpic1-104-4/>

<https://www.ibm.com/support/knowledgecenter/ssw_aix_71/q_commands/quotaon.html>

<https://linux.101hacks.com/unix/repquota/>

.

Copy

# 104.5. Manage file permissions and ownership

**Weight:** 3

**Description:** Candidates should be able to control file access through the proper use of permissions and ownerships.

**Key Knowledge Areas:**

* Manage access permissions on regular and special files as well as directories
* Use access modes such as suid, sgid and the sticky bit to maintain security
* Know how to change the file creation mask
* Use the group field to grant file access to group members

**Terms and Utilities:**

* chmod
* umask
* chown
* chgrp

####

#### Users, groups and file ownership

By now, you know that Linux is a multiuser system and that each user belongs to one primary group and possibly additional groups. It is also possible to log in as one user and become another user using the `su` commands. Ownership of files in Linux and access authority are closely related to user ids and groups.

### User and groups

To start, let’s review some basic user and group information via some commands

* whoami : It displays the username of the current user (ubuntu16.04)

* groups: We can find out what groups you are in by using the `groups` command.

* id : We can find out both user and group information using the `id` command.

> It can show numeric ID’s (UID or group ID) of the current user or any other user in the server.

users and groups information are stored in /etc/passwd and /etc/group along other information.

#### File ownership and permissions

Every file on a Linux system has one owner and one group associated with it.

Use the ls -l`ls-l` command to display the owner and group.

> As you can see, the file1 belongs to user1 and a group called user1.

The first character of a long listing describes the type of object. "-" for a regular file, "d" for a directory, "l" for a symbolic link(we will see them).

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lzej245OSElqjQxel58%252F-LzesOz9xowCLqU4YGmL%252Fpermis-filepermis.jpg%3Falt%3Dmedia%26token%3D16c698de-597b-4e70-9204-8e4a81b31809&width=768&dpr=4&quality=100&sign=f0884c80&sv=2)

Permissions are specified separately for the file’s owner, members of the file’s group, and everyone else.

The Linux permission model has three types of permission for each filesystem object.

The permissions are read (r), write (w), and execute (x). Write permission includes the ability to alter or delete an object. A `-` indicates that the corresponding permission is not granted. example:

As you can see fsck can be read, written and executed by its owner (root) and all root group members, but others can just read and execute that(probably with limited results )

#### Directories ownership and permissions

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lzej245OSElqjQxel58%252F-LzetqNy-ZIjilYOFYpJ%252Fpermis-dirpermis.jpg%3Falt%3Dmedia%26token%3D1c524b89-cf94-4a37-ba19-33e0bf99448e&width=768&dpr=4&quality=100&sign=fd900a60&sv=2)

Directories use the same permissions flags as regular files, but they are interpreted differently.

* Read permission for a directory allows a user with that permission to list the contents of the directory.
* Write permission means a user with that permission can create or delete files in the directory.
* Execute permission allows the user to enter the directory and access any subdirectories.

Without execute permission on a directory, the filesystem objects inside the directory are not accessible. Without read permission on a directory, the filesystem objects inside the directory are not viewable in a directory listing, but these objects can still be accessed as long as you know the full path to the object on disk. example:

The first charcter indicates that this a directory. The owner (user1) has read,write, execute access but other members of user1 group and others have just read and execute access on this directory, (as we mentioned, execute lets them to see files inside it )

#### Changing permissions

### chmod

The command you use to change the permissions on files is called chmod , which stands for “change mode". There are to ways to tell this command what you want to do:

* using short codes
* using ocatl codes

**1- using short codes:** That is easier way.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LzfACWbBJHoewfSDO8O%252F-LzfKoouBQB9kxZY3Ii9%252Fpermis-chmodshortcodes.jpg%3Falt%3Dmedia%26token%3D9c5ac485-c560-441c-8c07-b4cf4f13e9e9&width=768&dpr=4&quality=100&sign=e11b07ae&sv=2)

reference can be

* u as user (file's owner)
* g as group (users who are members of the file's grou)
* o as others (users who are not the file's owner / members of the file's group)
* a as all (All three of the above, same as ugo)

Operator can be

* + Adds the specified modes to the specified classes
* - Removes the specified modes from the specified classes
* = The modes specified are to be made the exact modes for the specified classes

obviously modes might be

* r :Permission to read the file
* w :Permission to write (or delete) the file.
* x : Permission to execute the file, or, in the case of a directory, search it.

> If we want to set different permissions for user, group, or other, we can separate different expressions by commas —for example, `ug=rwx,o=rx`

> using a as ugo with = operator to set exact mode easier

**2- using ocatl codes :** So far we have used symbols (ugoa and rxw) to specify permissions. we can also set permissions using octal numbers instead of symbols.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LzfACWbBJHoewfSDO8O%252F-LzfTQt_XlHx-FilE1GW%252Fpermis-chmodoctalcodes.jpg%3Falt%3Dmedia%26token%3D7b0f1e67-05d5-4b69-bde3-ff2b9b011260&width=768&dpr=4&quality=100&sign=aa4f79ae&sv=2)

For using octal codes with chmod we have to create an octal string, and that's is nothing more than a simple sum of numbers:

Symbolic

note

Octal

rwx

4+2+1

7

rw-

4+2

6

r-x

4+1

5

r--

4

4

-wx

2+1

3

-w-

2

2

--x

1

1

---

0

0

To change permissions recursively on directories and files use `-R` option:

#### Access modes

When we log in, the new shell process runs with your user and group IDs. This usually means that you cannot access files belonging to others and cannot write system files. From the other side, users are totally dependent on other programs to perform operations.

An important example is the /etc/passwd file, which cannot be changed by normal users directly, because write permission is enabled only for root. However, normal users need to be able to modify /etc/passwd somehow:

So, if the user is unable to modify this file, how can this be done? What is that "s"?

### suid , guid

The Linux permissions model has two special access modes called suid (set user id) and sgid (set group id). When an executable program has the suid access modes set, it will run as if it had been started by the file’s owner, rather than by the user who really started it. Similarly, with the sgid access modes set, the program will run as if the initiating user belonged to the file’s group rather than to his own group.

> #### Directories and sgid
>
> When a directory has the sgid mode enabled, any files or directories created in it will inherit the group ID of the directory. This is particularly useful for directory trees that are used by a group of people working on the same project.

### sticky bit

We have just seen how anyone with write permission to a directory can delete files in it. This might be acceptable for a group project, but is not desirable for globally shared file space such as the /tmp directory. Fortunately, there is a solution. That is called the *sticky* bit.

If set stickybit for a directory, it permits only the owning user or the superuser (root) to delete or unlink a file.

Okey lets wrap up what we have learned:

access mode

**on file**

**on directory**

**SUID**

executes with permissions of file owner

nothing

**GUID**

executes with the permissions of group

new files have group membership of directory

**Sticky Bit**

nothing

only owner can delete files

#### How suid, guid and stickybit are implemented?

As there is no more room for setting Access modes, execution character is used. "s" letter is used for both suid and guid but "t" letter is for stickybit. Again we use `+/-` for adding and removing permissions.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LzkMDvPLUTmflnayESr%252F-LzkbY1dqbkBGPFPeIiE%252Fpermis-accessmodes.jpg%3Falt%3Dmedia%26token%3D2be9e340-0719-49e0-b05a-06b0c51df61b&width=768&dpr=4&quality=100&sign=5af31f52&sv=2)

> As you have probably noticed, if the file or directory is already executable **s** and **t**  would be displayed after setting access modes.
>
> But if the file or directory hasn't been executable before setting access mode, **S** and **T** would be appear.

As an example for suid consider ping command, as ping needs to access network card it needs root permissions, but an ordinary user can use it:

Now we try setting guid on a directory and we will create a file with another user:

And finally lets try how stickybit works on /tmp:

#### Setting Access Modes via octal codes:

We can also use octal codes to set suid, guid and stickybit:

Access Mode

octal

**SUID**

4000

**GUID**

2000

**StickyBit**

1000

And again we can use sum of digits.

### umask

When a new file or directory is created, the creation process specifies the permissions that the new file or directory should have. Where do they come from? They came from the umask.

We can view your umask setting with the `umask` command:

#### How umask work?

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-Lzfxv7Pp3Gj1QqT8QIn%252F-LzgJXglH_J3fzEv7R22%252Fpermis-umask.jpg%3Falt%3Dmedia%26token%3De0d8e515-abfb-4756-b99a-86fd7f9f3643&width=768&dpr=4&quality=100&sign=6f8c429b&sv=2)

When a new file is created, the creation process specifies the permissions that the new file should have. Often, the mode requested is 0666, which makes the file readable and writable by anyone (but not executable). Directories usually default to 0777. However, this permissive creation is affected by a *umask* value, which specifies what permissions a user does **not** want to grant automatically to newly created files or directories. The system uses the umask value to reduce the originally requested permissions.

Usually umask is set system wide (it could be set per user) and we can find its configuration in one of these places (based on your linux distribution):

> * /etc/profile (usually)
> * /etc/bashrc (usually)
> * /etc/logindefs (ubuntu)

as we are using ubuntu here lets take look at /etc/logindefs:

it say umask would be 002 if USERGROUPS\_ENAB is set, lets check it out:

which is why umask is 002 in our system.

#### Setting file owner and group

All files in Linux belong to an owner and a group. We can set the owner by using `chown` command, and the group by the `chgrp` command.

### chown

The root user can change the ownership of a file using the `chown` command.We can use user name or user ID.

The file’s group may be changed at the same time by adding a colon and a group name or ID right after the user name or ID.

If only a colon is given, then the user’s default group is used:

the -R option will apply the change recursively and `-c`  Reports when a file change is made. We can also use other file ownership via `--referenece` switch.

### chgrp

chgrp command in Linux is used to change the group ownership of a file or directory.

**Note1:** We need to have administrator permission to add or delete groups

**Note2:** the owner of file can always change the group of his/her file or directory to its own group or one of the groups that him/her is a member of.

As with many of the commands covered in this tutorial, `chgrp` has a `-R` option to allow changes to be applied recursively to all selected files and subdirectories.

--refrence Uses the groupname of a reference file to change the group of another file or folder.

.

.

.

**Primary and secondary groups**

There are actually two types of groups — **primary** and **secondary**.

The **primary group** is the one that’s recorded in the **/etc/passwd** file, configured when an account is set up. When a user creates a file, it’s their primary group that is associated with it.

**Secondary groups** are those that users might be added to once they already have accounts. Secondary group memberships show up in the /etc/group file.

A user can change his/her **primary group** (**default group**) with `newgrp` command, and after that all file/directories the user creates will have that group.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-104-5/>

<https://jadi.gitbooks.io/lpic1/content/1045_manage_file_permissions_and_ownership.html>

<https://www.geeksforgeeks.org/chmod-command-linux/>

<https://www.geeksforgeeks.org/permissions-in-linux/>

<https://www.geeksforgeeks.org/chown-command-in-linux-with-examples/>

<https://www.geeksforgeeks.org/chgrp-command-in-linux-with-examples/>

<https://www.networkworld.com/article/3409781/mastering-user-groups-on-linux.html>

.

.

.

Copy

# 104.6. Create and change hard and symbolic links

**Weight:** 2

**Description:** Candidates should be able to create and manage hard and symbolic links to a file.

**Key Knowledge Areas:**

* Create links
* Identify hard and/or soft links
* Copying versus linking files
* Use links to support system administration tasks

**Terms and Utilities:**

* ln
* ls

### Introducing links

On a storage device, a file or directory is stored in a collection of blocks. Information about a file is held in an *inode*, which records information such as the owner, when the file was last accessed, how large it is, whether it is a directory or not, and who can read from or write to it.

A *directory entry* contains a name for a file or directory and a pointer to the inode where the information about the file or directory is stored.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LzlbQMxvxelh1wTW90T%252F-Lzm3WO3ORTyRLcmH937%252Flinks-inodes.jpg%3Falt%3Dmedia%26token%3D378c0b3b-59fb-437f-81a0-3d0cb34f5cc7&width=768&dpr=4&quality=100&sign=c6985e20&sv=2)

> The inode number is unique within a particular filesystem.

> -i switch print the index number of each file

**Whats is link ?**  A link is simply an additional directory entry for a file or directory, allowing two or more names for the same thing.

#### Creating links

There are two types of links : **Hard Link** and **Soft Link**.

A **hard link** is a directory entry that points to an inode, while a **soft link** or *symbolic link* is a directory entry that points to an inode that provides the name of another directory entry. Symbolic links are also called *symlinks*.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-LzzouLMB7ojDJt9r5g-%252F-LzzqTJAXpftALWyYmRR%252Flink-links.jpg%3Falt%3Dmedia%26token%3Dce319c34-5e8c-4dae-a99a-5928ec2980f0&width=768&dpr=4&quality=100&sign=15fef5c3&sv=2)

> hard links point to an inode, and inodes are only unique within a particular file system, hard links cannot cross file systems(different partitions or hard disks).

> You can create hard links only for files and not for directories. The exception is the special directory entries in a directory for the directory itself and for its parent (. and ..)

### Hard Links vs Soft Links

hard link

soft link

have same inodes number.

have different inodes numbers.

can’t cross the file system boundaries

can cross the file system

can’t link directories

allows you to link between directories

Links have actual file contents

contains the path for original file and not the contents

if the original file is removed, the link will still show you the contents of the file

Removing soft link doesn't affect anything but when the original file is removed, the link becomes a 'dangling' link that points to nonexistent file.

permissions will be updated if we change the permissions of source file

permissions will not be updated

#### Creating links

### ln

we can use ln command to create both hard links and soft links

### Hard Links

Use the `ln` command to create additional hard links to an existing file (but not to a directory, even though the system sets up . and .. as hard links).

ls -l command shows all the links with the link column showing the number of links:

look at that"2" infront of file1, it was "1" before creating HardLink.

### Soft Links

`ln` command with the `-s` option creates soft links. Soft links use file or directory names, which may be relative or absolute. If you are using relative names, you will usually want the current working directory to be the directory where you are creating the link. Otherwise, the link you create will be relative to another point in the file system.

ls -l command shows all links with second column value 1 and the link points to the original file.

#### Broken symlinks

Since hard links always point to an inode that represents a file, they are always valid. However, symlinks can be broken for many reasons, including:

* Either the original file or the target of the link did not exist when the link was created
* The target of a link is deleted or renamed.
* Some element in the path to the target is removed or renamed.

**Identifying links via find command**

To find which files are hard links to a particular inode, use the `find` command and the `-samefile` option with a file name or the `-inum` option with an inode number:

We can also use the `find` command to search for symbolic links using the `-type l` find expression:

### Copying versus linking

Depending on what we want to accomplish, sometimes we will use links and sometimes it may be better to make a copy of a file.

* The major difference is that links provide multiple names for a single file, while a copy creates two sets of identical data under two different names.
* You would certainly use copies for backup and also for test purposes where you want to try out a new program without putting your operational data at risk.
* You use links when we need an alias for a file (or directory), possibly to provide a more convenient or shorter path.
* when we update a file, all the links to it see the update, which is not the case if you copy a file.

symbolic links can be broken but that subsequent write operations may create a new file. Use links with care.

#### Links and system administration

Links, especially symbolic links, are frequently used in Linux system administration.

1- **Aliasing commands to a particular version**

Commands are often aliased, so the user does not have to know a version number for the current command but can access other versions by longer names if necessary.

2-**Command alias examples**

Other uses come into play when multiple command names use the same underlying code, such as the various commands for stopping and for restarting a system. Sometimes, a new command name, such as `genisoimage`, will replace an older command name, but the old name (mkisofs) is kept as a link to the new command.

3- **Library links**

Library names are also managed extensively using symlinks, either to allow programs to link to a general name while getting the current version, or to manage systems such as 64-bit systems that are capable of running 32-bit programs.

.

.

.

**remove symbolic links**

We canremove (delete) symbolic links using the `rm`, `unlink`, and `find` commands.

*To remove a symlink, you need to have writing permissions on the directory that contains the symlink. Otherwise, you will get “Operation not permitted” error.*

**Remove Symbolic Links with** `rm`

To delete a symlink, invoke the `rm` command followed by the symbolic link name as an argument: `rm symlink_name`

With `rm` you can delete more than one symbolic links at once. To do that pass the names of the symlinks as arguments, separated by space: `rm symlink1 symlink2` Try -i to get confirmed.

If the name of the argument ends with `/`, the `rm` command assumes that the file is a directory. The error happens because, when used without the `-d` or `-r` option, `rm` cannot delete directories.

#### Remove Symbolic Links with `unlink`

The unlink command deletes a given file`!` Unlike rm, unlink accepts only a single argument.

To delete a symbolic link, run the unlink command followed by the symlink name as an argument: `unlink symlink_name`

Do not append the / trailing slash at the end of the symlink name because unlink cannot remove directories`.`

#### Find and Delete Broken Symbolic Links

To find all broken symbolic links under a given directory, run the following command: `find /path/to/directory -xtype l`

Once you find the broken symlinks, you can either manually remove them with `rm` or `unlink` or use the `-delete` option of the `find` command`: find /path/to/directory -xtype l -delete`

#### Conclusion

To remove a symbolic link, use either the `rm` or `unlink` command followed by the name of the symlink as an argument. When removing a symbolic link that points to a directory do not append a trailing slash to the symlink name.

.

<https://developer.ibm.com/tutorials/l-lpic1-104-6/>

<http://bambamdeo-linux.blogspot.com/2014/11/soft-link-and-hard-link.html>

<https://www.ostechnix.com/explaining-soft-link-and-hard-link-in-linux-with-examples/>

<https://linoxide.com/linux-how-to/difference-soft-link-hard-link/>

<https://www.geeksforgeeks.org/soft-hard-links-unixlinux/>

[`https://linuxize.com/post/how-to-remove-symbolic-links-in-linux/`](https://linuxize.com/post/how-to-remove-symbolic-links-in-linux/)

.

Copy

# 104.7. Find system files and place files in the correct location

**Weight:** 2

**Description:** Candidates should be thoroughly familiar with the Filesystem Hierarchy Standard (FHS), including typical file locations and directory classifications.

**Key Knowledge Areas:**

* Understand the correct locations of files under the FHS
* Find files and commands on a Linux system
* Know the location and purpose of important file and directories as defined in the FHS

**Terms and Utilities:**

* find
* locate
* updatedb
* whereis
* which
* type
* /etc/updatedb.conf

There are over 200 Linux distributions available , all having a lot of things in common, there should be a standard way to place files in the system, and that's where FHS comes to play.

### FHS

The Filesystem Hierarchy Standard (FHS) is a document that specifies a common layout of directories on a Linux/ UNIX system.

Directory

Purpose

bin

Essential command binaries

boot

Static files of the boot loader

dev

Device files

etc

Host-specific system configuration

lib

Essential shared libraries and kernel modules

media

Mount point for removable media

mnt

Mount point for mounting a filesystem temporarily

opt

Add-on application software packages

sbin

Essential system binaries

srv

Data for services provided by this system

tmp

Temporary files

usr

Secondary hierarchy

var

Variable data

home

User home directories (optional)

lib

Alternate format essential shared libraries (optional)

root

Home directory for the root user (optional)

The `/usr` and `/var` hierarchies are complex enough to have complete sections of the FHS devoted to them.

The`/usr`Contains binaries, libraries, documentation, and source-code for second level programs.

* **/usr/bin** contains binary files for user programs.
* **/usr/sbin** contains binary files for system administrators.
* **/usr/lib** contains libraries for /usr/bin and /usr/sbin
* **/usr/local** contains users programs that you install from source.
* **/usr/src** holds the Linux kernel sources, header-files and documentation.

The `/var` filesystem contains variable data files, including spool directories and files, administrative and logging data, and transient and temporary files. Some portions of `/var` are not shareable between different systems, but others, such as `/var/mail`, `/var/cache/man`, `/var/cache/fonts`, and `/var/spool/news`, may be shared.

### PATH

When you run a program at the command line, the bash (or other) shell searches through a list of directories to find the program you requested. The list of directories is specified in your PATH environment variable.

As you can see, the PATH variable is just a list of directory names, separated by colons. Note the differences between the user path and root path

As we said in previous sections we can change our path with export `PATH=$PATH:/new/path/dir` or by adding thant inside **.bash\_profile** or **.bashrc** .

#### which, type, and whereis

### which

The `which` command to search your path and find out which command will be executed (if any) when you type a command.

> The `which` command shows you the first occurrence of a command in your path. If you want to know if there are multiple occurrences, then add the `-a` option

### type

There are some commands that the `which` command will not find, such as shell builtins.

The `type` command is a builtin that understand bash keywords and can tell us how a given command string will be evaluated for execution.

### whereis

If you want more information than just the location of a program, you can use the `whereis` command.

The `whereis` command can also search for man pages and source codes of programs alongside their binary location .

### find

In an earlier tutorial in this series "104-7", you learned how to find files based on name (including wildcards), path, size, or timestamp. In another earlier tutorial in this series, “104-6” you learned how to find the links to a particular file or inode.

The `find` command is the Swiss Army knife of file-searching tools on Linux systems. Two other capabilities that you may find useful are its ability to find files based on user or group name and its ability to find files based on permissions.

#### Finding by Owner and Permissions

We can also search for files by the file owner or group owner (discussed in "104-5"). We do this by using the `-user` and `-group` parameters respectively.

> use -nouser or -nogroup to search for a file with no user or with no group id.

We can also search for files with specific permissions. If we want to match an exact set of permission `find / -perm 644`

If we want to specify anything with at least those permissions:`find / -perm -644` .

#### filtering by depth

We can specify the maximum depth of the search under the top-level search directory:

Also it is possible to combine the min and max depth parameters to focus in on a narrow range `find -mindepth num -maxdepth num -name file`:

> Like other tests, you can add a ! just before any phrase to negate it. So this will find files not belonging to user1 : `find . ! -user user1`

#### locate & updatedb

The `find` command searches all the directories you specify, every time you run it. To speed things up, you can use another command, `locate`, which uses a database of stored path information rather than searching the filesystem every time.

### locate

The `locate` command searches for matching files in a database that is usually updated daily (by cron job).

The `locate` command matches against any part of a path name, not just the file name.

### updatedb

The default database used by locate is stored in the `/var` filesystem, in a location such as `/var/lib/locatedb`. *This may be different on systems that use slocate or mlocate packages to provide additional security or speed*. You can find statistics on your locate database using locate-S :

The database is created or updated using the `updatedb` command. `(`This is usually run daily as a cron job).

> use -v for verbose mode to see what is going on after updatedb command!

The file `/etc/updatedb.conf`, or sometimes `/etc/sysconfig/locate`, is the configuration file for `updatedb:`

There are some PRUNING on the configuration file which cause locate never search for those kinds of files or directories like `/tmp` or `/var/spool` . You can let locate to search for them too if you like by manipulating this file.

that's all.

## Congratulation we have done lpic1-101 !!!

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-104-7/>

<https://www.geeksforgeeks.org/linux-file-hierarchy-structure/>

<https://www.digitalocean.com/community/tutorials/how-to-use-find-and-locate-to-search-for-files-on-a-linux-vps><https://jadi.gitbooks.io/lpic1/content/1047_find_system_files_and_place_files_in_the_correct_location.html>

.

Copy

# 105.1. Customize and use the shell environment

## **105.1 Customize and use the shell environment**

**Weight**: 4

**Description:** Candidates should be able to customize shell environments to meet users’ needs. Candidates should be able to modify global and user profiles.

**Key Knowledge Areas:**

* Set environment variables (e.g. PATH) at login or when spawning a new shell
* Write Bash functions for frequently used sequences of commands
* Maintain skeleton directories for new user accounts
* Set command search path with the proper directory

**The following is a partial list of the used files, terms and utilities:**

* source
* /etc/bash.bashrc
* /etc/profile
* env
* export
* set
* unset
* ~/.bash\_profile
* ~/.bash\_login
* ~/.profile
* ~/.bashrc
* ~/.bash\_logout
* function
* alias
* lists

We have already talk about environment variables in section "103-1". In this section we want to talk about user profiles and system wide profile , and how they interact when user log on.

### Login shell and Non login shell

The shell program, for example Bash, uses a collection of startup scripts to create an environment. Each script has a specific use and affects the login environment differently. Every subsequent script executed can override the values assigned by previous scripts.

Startup is configured differently for Login shells and Non login shells.

1. **Login shells** : If you open a shell or terminal (or switch to one), and it asks you to log in (Username? Password?) before it gives you a prompt, it's a login shell.
2. **Non login shells** : If it doesn't ask you log in (like *gnome-terminal*), and lets you use it straight away, it's a non-login shell (GUI)

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-8cRJkhLU5effAxLIk%252F-M-9-hYMFT39RCZYt7up%252Fcustshell-loginshelvsnon.jpg%3Falt%3Dmedia%26token%3D6d3073b8-e6ef-4b5c-86c4-9e75104d69ed&width=768&dpr=4&quality=100&sign=89a3214c&sv=2)

#### Adding global configuration for login shell

### /etc/profile

/etc/profile contains Linux system wide environment and startup programs. It is used by all users with bash, ksh, sh shell. It only runs for login shell.

### /etc/profile.d

if you need to customize the login environment for all users on your system, you can use /etc/profile, but as the distribution files in /etc, such as /etc/profile, can be modified by system updates, so it is better not to edit them directly. Rather, create additional files in /etc/profile.d.

#### adding global configs for non-login (interactive) shell

### /etc/bash.bashrc & /etc/bashrc

You can use /etc/bash.bashrc ( or /etc/bashrc )[based on your distro] for adding global configs and global aliases.

#### user specfic configs

### /home/user/.bash\_profile & /home/user/.bashrc

`~/.bash_profile` and `~/.bashrc` are shell scripts that contain shell commands. These files are executed in a user's context when a new shell opens or when a user logs in so that their environment is set correctly. As we mentioned`~/.bash_profile` is executed for login shells and `~/.bashrc` is executed for interactive non-login shells.

This means that when a user logs in (via username and password) to the console (either locally or remotely via something like SSH), the `~/.bash_profile` script is executed before the initial command prompt is returned to the user. After that, every time a new shell is opened, the `~/.bashrc` script is executed.

> Most of the time PATH and env vars go into the in ~/.bash\_profile and aliases go into the ~/.bashrc.

### Aliases

In bash, you can define aliases for commands. You use aliases to provide an alternative name for a command, to provide default parameters for the command, or sometimes to construct a new or more-complex command.

You set aliases or list aliases with the `alias` command and remove them with the `unalias` command.

in order to make aliases permanent for user they are defined in `/home/user/.bashrc` :

> Another common use of aliases is for the root user. The `cp`, `rm`, and `mv` commands are usually aliased to include the `-i` parameter, to help prevent accidental destruction of files.

### /etc/skel

You might be wondering how files like ~/.bash\_profile, ~/.bashrc, or ~/.bash\_logout got created in your home directory. These are skeleton files that are copied from /etc/skel.

### .bash\_logout

The file .bash\_logout is read and executed every time a login shell exits. It clears the screen whenever you log out. Without .bash\_logout whatever you were working on could be visible for the next user!

### . and source

If a script runs in a child shell, any variables it might export are lost when it returns to the parent.

So if .profile runs the ~/.bashrc script, why aren’t the variables and functions that are exported from ~/.bashrc lost? The answer is that you run the script in the current environment by using the `source` (or `.`) command.

### Shell functions

Aliases are useful, but what happens if you want to handle parameters? Aliases expand only the first word, and everything else on the command line is appended to the expansion. If you want to run a command with some parameters and then process the output somehow, you are out of luck with an alias. In this case, you need a shell function.

`$1` returns the first argument

Shell functions have a couple of advantages over aliases:

* You can handle parameters.
* You can use programming constructs, such as testing and looping, to enhance your processing.

We can use `unset` command inorder to unset our defined function.

### lists

Shell supports a different type of variable called an array variable. This can hold multiple values at the same time. Arrays provide a method of grouping a set of variables. Instead of creating a new name for each variable that is required, you can use a single array variable that stores all the other variables.

Another example:

Keep your eyes on syntax!

.

.

.

<http://howtolamp.com/articles/difference-between-login-and-non-login-shell/>

<https://askubuntu.com/questions/155865/what-are-login-and-non-login-shells>

<https://www.cyberciti.biz/faq/set-environment-variable-linux/>

<https://developer.ibm.com/tutorials/l-lpic1-105-1/>

<https://jadi.gitbooks.io/lpic1/content/1051_customize_and_use_the_shell_environment.html>

<https://www.tutorialspoint.com/unix/unix-using-arrays.htm>

With the special thanks of shawn powers.

.

Copy

# 105.2. Customize or write simple scripts

**Weight:** 4

**Description:** Candidates should be able to customize existing scripts, or write simple new Bash scripts.

**Key Knowledge Areas:**

* Use standard sh syntax (loops, tests)
* Use command substitution
* Test return values for success or failure or other information provided by a command
* Perform conditional mailing to the superuser
* Correctly select the script interpreter through the shebang (#!) line
* Manage the location, ownership, execution and suid-rights of scripts

**Terms and Utilities:**

* for
* while
* test
* if
* read
* seq
* exec

This lesson is all about shell scripting in linux and we start writing some simple scripts. We can put almost every command we use, inside a shell script. But before starting there are some notes to consider.

### shebang (#!)

In Linux and opensource world script files are very important. There are different type of scripting language used to write script files. As file extension is just a label for a script, **shebang** (file script file interpreter line )is used to specify the scripting language.

Beside that, there are different kinds of shell and You can’t guarantee which shell your potential users might prefer. shebang makes scripts portable to all shell environments by instructing the shell to run your script in a particular shell.

> `#` and `!` makes this line special because `#` is used as comment line in bash.

The shebang line must be the first line of your script, and the rest of the line contains the path to the shell that your program must run under.

### variables

In prior sections in this series, we learned how to define a variable `VARIABLE="value"` . We can do the same thing in a script, as an example:

We have assigned string values to variables. Bash supports shell arithmetic using integers.

**declare**

The **declare** is a builtin command of the **bash** shell. It is used to declare shell variables and functions, set their attributes and display their values. `-i` make a VARIABLE to have 'integer' attribute.

`-p`displays the options and attributes of each variable name if it is used with name arguments:

### command substitution

Sometimes we might need to use the result of a command for another command or a variable.

If we surround a command with `$(` and `)`, or with a pair of backticks, we can substitute the command’s output as input to another command. This technique is called *command substitution*.

example:

### executing scripts

Inorder to run a shell script, the script should be executabe.

> Another way of executing a script is giving our script name as a parammeter to `sh` or `bash` commands. `sh ./script1` or `bash ./script1`

### locating scripts

if our script is executable we can locate that in 3 ways:

* We can use `./scriptname` if we are in the same directory
* We can use absolute path `/home/user1/sandbox/scriptname`
* putting our script in one of `$PATH` directories or editting `PATH` variable.

### conditioning

In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability.

The simplest form is the **if** statement, which has the genaral form:

### if

> the esle part is optional and can be ommited.

> The actual checking of the condition is done by `test` command which is writter as `test EXPRESSION` it is the same as `[ EXPRESSION ].`

Expressions take the following forms:

Expression

Meaning

STRING1 **=** STRING2

the strings are equal

STRING1 != STRING2

the strings are not equal

INTEGER1 -eq INTEGER2

INTEGER1 is equal to INTEGER2

INTEGER1 -ge INTEGER2

INTEGER1 is greater than or equal to INTEGER2

INTEGER1 -gt INTEGER2

INTEGER1 is greater than INTEGER2

INTEGER1 -le INTEGER2

INTEGER1 is less than or equal to INTEGER2

INTEGER1 -lt INTEGER2

INTEGER1 is less than INTEGER2

INTEGER1 -ne INTEGER2

INTEGER1 is not equal to INTEGER2

-n STRING

the length of STRING is nonzero

-z STRING

the length of STRING is zero

-f FILE

FILE exists and is a regular file

-s FILE

FILE exists and has a size greater than zero

-X FILE

FILE exists and execute (or s

-d FILE

FILE exists and is a directory

### read

`read` command read a line from the standard input.

### loops

The purpose of loops is to repeat the same, or similar code a number of times. This number of times could be specified to a certain number, or the number of times could be dictated by a certain condition being met. There are usually a number of different types of loops including for loops, while loops and‌ ... .

### for

The `for` loop processes each item in a sequence

> please py attention to syntax `;` , `do` , `done` .

> LIST can be a list of strings, an array or output of commands, etc

### **seq**

**seq is a very usefull command.** it generates squence of numbers for loop from FIRST to LAST in steps of INCREMENT.

seq in for loop :

> We can also define a range with {START..END..INCREMENT} syntax and it would do the same thing.

for loop works with strings too:

### while

while loops evaluate a condition each time the loop starts and execute the command list if the condition is true. If the condition is not initially true, the commands are never executed.

example:

> The **let** is a builtin command and used to evaluate arithmetic expressions on shell variables. What does it mean ? Without let MYVAR=MYVAR-1 whould have "3-1" value as string!

> If you want to use a variable value in an arithmetic expression, you don’t need to use `$` before the variable name, although you can if you want.

**infinite loops**

if the condition of while loop is never met, it goes running for ever, that is called infinite loop and we have to use ctrl+c to break that!

infinite loops are not that much bad ! The OS is an infinite loop which constantly checks for input and response accordingly.

**until**
until loops execute the command list and evaluate a condition each time the loop ends. If the condition is true, the loop is executed again. Even if the condition is not initially true, the commands execute at least once.

### exec

**exec** command in Linux is used to execute a command from the bash itself. This command does not create a new process it just replaces the bash with the command to be executed. If the exec command is successful, it does not return to the calling process. try `exec BLAH` and `exec ls` and compare results.

### Mailing notifications to root

For sending mail first we need to have `mailutils` installed. Then we can send mail:

Suppose your script is running an administrative task on your system in the dead of night while you’re sound asleep. What happens when something goes wrong? Fortunately, it’s easy to mail error information or log files to yourself or to another administrator or to root. Simply pipe the message to the `mail` command, and use the `-s` option to add a subject line,

> If you need to mail a log file, use the `<` redirection function to redirect it as input to the `mail` command. If you need to send several files, you can use `cat` to combine them and pipe the output to `mail`.

**bash scripting cheatsheet**

I also encourage you to visit my bash scripting cheatsheet at: <https://borosan.gitbook.io/bash-scripting/>

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-105-2/>

<https://www.poftut.com/linux-bin-bash-shell-and-script-tutorial/>

<https://www.geeksforgeeks.org/declare-command-in-linux-with-examples/>

<https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html>

<https://jadi.gitbooks.io/lpic1/content/1052_customize_or_write_simple_scripts.html>

<https://www.computerhope.com/unix/test.htm>

<https://www.dpscomputing.com/blog/2012/09/13/programming-the-purpose-of-loops/>

<https://www.geeksforgeeks.org/seq-command-in-linux-with-examples/>

<https://linux4one.com/bash-for-loop-with-examples/>

<https://www.geeksforgeeks.org/let-command-in-linux-with-examples/>

<https://www.quora.com/What-are-some-practical-uses-of-infinite-loops>

<https://www.geeksforgeeks.org/exec-command-in-linux-with-examples/>

.

Copy

# 105.3. SQL data management

**Weight:** 2

**Description:** Candidates should be able to query databases and manipulate data using basic SQL commands. This objective includes performing queries involving joining of 2 tables and/or subselects.

**Key Knowledge Areas:**

* Use of basic SQL commands
* Perform basic data manipulation

**Terms and Utilities:**

* insert
* update
* select
* delete
* from
* where
* group by
* order by
* join

So far in this series of tutorials, we used flat text files to store data. Flat text files can be suitable for small amounts of data, but they are not good for storing large amounts of data or to querying that data. Over the years, several kinds of databases were developed for that purpose, the most common is now the **relational database**.

Several relational database systems exist today, including commercial products such as Oracle Database and IBM DB2®, and open source projects such as MySQL, PostgreSQL SQLite, and MariaDB (a fork of MySQL). Relational databases use SQL as a data definition and query language.

SQL (pronounced "ess-que-el") stands for Structured Query Language. SQL is used to communicate with a database. it is the standard language for relational database management systems. SQL statements are used to perform tasks such as update data on a database, or retrieve data from a database.

### Databases, tables, columns, and rows

A relational database consists of a set of *tables*. Think of each *row* of data in the table as a record, with each *column* of the table corresponding to the fields in the record for the corresponding row. The data in a column is all of the same *type*— such as character, integer, date, or binary data (such as images).

We are not going to install MySQL or create some databases from zero, our focus is on SQL and we use existing Data Base (ubuntu16.04):

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-ZKIJ4ZeBeJaQwE4R8%252F-M-ZRMcW6B6D_saoR1Bz%252Fsql-mydata.jpg%3Falt%3Dmedia%26token%3Dc986a424-f586-4327-a55e-50b3d9cb44aa&width=768&dpr=4&quality=100&sign=c0de27cb&sv=2)

#### MySQL command line

mysql has simple SQL shell command line which we use to ineteractivly connect to a mysql-server.

it means that I'm going to use `u` ser root and the `p`assword which i will provide. It is also possible to type the password on the command and define which database i am going to use , which is not a great idea!

#### using a database

After connecting to the mysql-server, we should define which database we are going to use. There might too many databases, first we see them via SHOW DATABASES command and then we use use the define which database we are going to use.

Usually MySQL commands are typed with CAPITAL LETTERS and names and values , ... in lower case. There should be a ; at the end of each MySQL command.

lets see tables:

### Exploring tables and columns

### SELECT

The **select** statement is used to query the database and retrieve selected data. We can select everything in the table using `*` , or we can select from particular columns:

> SELECT *column1*, *column2, ...*
> FROM *table\_name*;

### WHERE

We can choose which data to display by using the `WHERE :`

> SELECT *column1*, *column2, ...*
> FROM *table\_name*
> WHERE *condition*;

it is also possible to make desired condition via AND and OR when using WHERE:

### ORDER BY

ORDERBY is used if we want to sort the data based on one field:

> SELECT *column1*, *column2, ...*
> FROM *table\_name*
> ORDER BY *column1, column2, ...*

and it can sort results based on any fields:

### GROUP BY

Sometimes you want aggregate information from a table. For example, you want to know how many big hatchbacks you have. We can use the `GROUP BY` clause to group your data for this purpose:

> SELECT *column\_name(s)*
> FROM *table\_name*
> WHERE *condition*
> GROUP BY *column\_name(s)*

it acts like unique command and group the result , to understand how many rows have been grouped by we can use count:

### Creating, changing, and deleting data and tables

### INSERT

`INSERT` command add one or more rows of data to a table.

> INSERT INTO *table\_name* (*column1*, *column2*, *column3*, ...)
> VALUES (*value1*, *value2*, *value3*, ...);

> the order is not important and bellow query would have the same result:

### UPDATE

`UPDATE` command to fix this mistake . It update row but which row? we should specified that with WHERE command.

> UPDATE *table\_name*
> SET *column1* = *value1*, *column2* = *value2*, ...
> WHERE *condition*;

### DELETE

The DELETE statement is used to delete existing records in a table.

> DELETE FROM *table\_name* WHERE *condition*;

Be careful when deleting records in a table! Notice the at WHERE in the DELETE statement. The WHERE clause specifies which record(s) should be deleted. If you omit the WHERE clause, all records in the table will be deleted!

### JOIN

A JOIN clause is used to combine rows from two or more tables, based on a related column between them. If no related column is given, Every single row from second table (sedan) is copied in front of the first table (hatchback).

and if we give JOIN a common field to JOIN the tables based on that, the magic happens:

### Different Types of SQL JOINs

Here are the different types of the JOINs in SQL:

* **(INNER) JOIN**: Returns records that have matching values in both tables
* **LEFT (OUTER) JOIN**: Returns all records from the left table, and the matched records from the right table
* **RIGHT (OUTER) JOIN**: Returns all records from the right table, and the matched records from the left table
* **FULL (OUTER) JOIN**: Returns all records when there is a match in either left or right table

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-QH7hU816zHbFP9G3W%252F-M-QJic_PBq990F6_28P%252Fsql-jointypes.jpg%3Falt%3Dmedia%26token%3D2a77c34f-b6b8-42cb-800c-84007512cc9e&width=768&dpr=4&quality=100&sign=3f2ca1fa&sv=2)

finally use quit command to get out of MySQL command line.

that's all!

.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-105-3/>

<http://www.sqlcourse.com/intro.html>

<https://dev.mysql.com/doc/refman/8.0/en/mysql.html>

<https://jadi.gitbooks.io/lpic1/content/1053_sql_data_management.html>

[`https://www.w3schools.com/sql/sql_select.asp`](https://www.w3schools.com/sql/sql_select.asp)

<https://tableplus.com/blog/2018/08/mysql-how-to-turn-off-only-full-group-by.html>

.

Copy

# 106.1. Install and configure X11

## **106.1 Install and configure X11**

**Weight:** 2

**Description:** Candidates should be able to install and configure X11.

**Key Knowledge Areas:**

* Verify that the video card and monitor are supported by an X server
* Awareness of the X font server
* Basic understanding and knowledge of the X Window configuration file

**Terms and Utilities:**

* /etc/X11/xorg.conf
* xhost
* DISPLAY
* xwininfo
* xdpyinfo
* X

In the days of very expensive computers that were shared among many users, X terminals provided a low cost way for many users to share the resources of a single computer. Nowadays computers have become as much powerful that no one doesn't think about sharing resources, but there are some history lessons which should know about!

### X

The X Window System, often known as X, is a windowing system for graphics workstations developed at MIT. It is based on a client/server model : The client/server model in X system works in reverse to typical client/server model, where the client runs on the local machine and asks for services from the server. In X system, the server runs on the local machine and provides its display and services to the client programs. The client programs may be local or remotely exist over different networks, but X serverc appear transparently.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-d44bRGYhm_zT5e2in%252F-M-dCX40atYcuR7JWNL1%252Fx-overviewall.jpg%3Falt%3Dmedia%26token%3Dd030cca0-a3bc-4f82-8ff5-40613ef933fc&width=768&dpr=4&quality=100&sign=f68eb43b&sv=2)

X11 display server protocol

Beside displaying the windows for the clients(applications ) The **X server also** handles input devices such as keyboards, mice, and touchscreens

**XOrg** Server was the free and open-source implementation of the display server for the X Window System managed by the X.Org Foundation. The X11 name points to X Windows version 11.

In many modern linux distributions , the Display manager server still exists, but X Window has been replaced by new solutions like wayland.

### /etc/X11/xorg.conf

The file xorg.conf is a file used for configuring the X.Org Server. xorg.conf usually is located in /etc/X11/xorg.conf but that does not exist any more on modern linux distributions , so we use a sample xorg.conf to explain that.

The xorg.conf configuration file is organized into sections which may be specified in any order. The general section format is

> Section "SectionName"
>
> SectionEntry ...
>
> EndSection

Lets take a quick look at most important ones:

* Files - pathnames for files such as fontpath

* Module - which modules to load

For example `glx` takes care of 3d graphical effects.

* InputDevice - keyboard and pointer (mouse)

These InputDevice sections are configured for any input devices, such as touchpads, mice, keyboards, that you may have plugged in to your system.

* Monitor - display device description

* Device - video card description/information

* Screen - binds a video adapter to a monitor

* ServerLayout - binds one or more screens with one or more input devices

### xwininfo

There may be situations where-in we need to fetch detailed information about an application window on our Linux system. For example, we might need to get the size and position of the window.

xwininfo is the tool that'll help us in this case. It's basically a window information utility for X (or X-Windows system). It gives Various information about that window depending on which options are selected. Information like size, position, color, depth, … .

### xdpyinfo

Xdpyinfo is a utility for displaying information about an X server.

### xhost

As we said **X** is designed to be network transparent, so that an X server can display windows from local or networked application sources.

The primary command for executing these network activities is xhost — the server access control program for X. Typically, remote access will be disabled, as it poses a security risk. But, if you need to run a GUI application on a remote computer, and have the GUI show up on your own screen, XHOST can be used to allow the remote computer. let get started:

* xhost with no option tells us the access status:

* xhost + : Turns off access control (all remote hosts will have access to X server)
* xhost - : Turns access control back on.

* xhost + hostname: Adds hostname to X server access control list.
* xhost - hostname: Removes hostname from X server access control list.

The xhost program is used to add and delete user names to the list allowed to make connections to the X server:

* xhost +si:localuser:some\_user Grants "some\_user" access to the "localuser" X, (localuser refers to the user who is currently logged in.)
* xhost -si:localuser:some\_user Revokes access of "some\_user".

### DISPLAY

The magic word in the X window system is DISPLAY. A display consists (simplified) of:

* a keyboard,
* a mouse
* and a screen.

A DISPLAY is managed by X server program. The server serves displaying capabilities to other programs that connect to it. The remote server knows where it have to redirect the X network traffic via the definition of the DISPLAY environment variable which generally points to an X Display server located on your local computer.

The value of the display environment variable is: `hostname:D.S`

where:

* **hostname** is the name of the computer where the X server runs. An omitted hostname means the localhost.
* **D** is a sequence number (usually 0). It can be varied if there are multiple displays connected to one computer.
* **S** is the screen number. A display can actually have multiple screens. Usually there's only one screen though where 0 is the default.

> :0.0 means that we are talking about the first screen attached to your first display in your local host

We can change the DISPLAY environment and connect my graphical output to another machine.

In this case if a graphical program is run , its output (windows) will be shown on another machine

> When using the OpenSSH ssh command on Linux, the -X option can be used to specify X11 forwarding.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-106-1/>

<https://kb.iu.edu/d/adnu>

<https://commons.wikimedia.org/wiki/File:X11_display_server_protocol.svg>

<https://en.wikipedia.org/wiki/X.Org_Server>

<https://mg.pov.lt/xorg.conf>

<https://www.faqforge.com/linux/fetch-detailed-information-application-window-linux/> <https://www.x.org/releases/X11R7.7/doc/man/man1/xwininfo.1.xhtml> <https://linux.die.net/man/1/xdpyinfo> <https://www.x.org/releases/X11R7.7/doc/man/man1/xdpyinfo.1.xhtml> <https://www.lifewire.com/linux-command-xhost-4093456> <https://beamtic.com/xhost-linux> <https://linux.die.net/man/1/xhost> <https://askubuntu.com/questions/432255/what-is-the-display-environment-variable>

.

Copy

# 106.2. Setup a display manager

**Weight:** 1

**Description:** Candidates should be able to describe the basic features and configuration of the LightDM display manager. This objective covers awareness of the display managers XDM (X Display Manger), GDM (Gnome Display Manager) and KDM (KDE Display Manager).

**Key Knowledge Areas**:

* Basic configuration of LightDM
* Turn the display manager on or off
* Change the display manager greeting
* Awareness of XDM, KDM and GDM

**Terms and Utilities:**

* lightdm
* /etc/lightdm/

A Linux desktop environment is a collection of applications designed to work well with each other and provide a consistent user experience. A desktop environment is usually paired with a login manager. The login manager also known as a greeter or display manager

#### What is Display Manager ?

The display manager is a bit of code that provides the GUI login screen for your Linux desktop. After you log in to a GUI desktop, the display manager turns control over to the window manager.

> Kernel -> X -> DisplayManager -> Desktop

When you log out of the desktop, the display manager is given control again to display the login screen and wait for another login.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-hpCjXW2rxPM4a-Zg5%252F-M-hthKqisxt_d6awp9Z%252Fdisplaymanager-centos7gdm.jpg%3Falt%3Dmedia%26token%3D62c83f45-ff38-473a-8733-063e84b423f5&width=768&dpr=4&quality=100&sign=fff64800&sv=2)

There are several display managers—some are provided with their respective desktops while some others not.

Any of the display managers can be used for your login screen regardless of which desktop you are using. Such is the flexibility of Linux and well-written, modular code.

Desktop

Display Manager

notes

GNOME

GDM

GNOME Display Manager

KDE

KDM

KDE Display Manager (up through Fedora 20)

KDE

SDDM

Simple Desktop Display Manager (Fedora 21 and above)

LXDE

LXDM

LXDE Display Manager

XDM

Default X Window System Display Manager

LightDM

Lightweight Display Manage

to get the default display manager you can try :

#### installing and switching to lightdm

In this lesson we use CentOS7 which uses gdm display manager by default. Lets switch to lightdm using bellow commands and check it:

if you reboot the service your system will be crashed.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-hpCjXW2rxPM4a-Zg5%252F-M-htttC3K4JZxPIBTDY%252Fdisplaymanager-centos7lightdm.jpg%3Falt%3Dmedia%26token%3D787912e8-e618-4c15-8974-b6a1ff3467e7&width=768&dpr=4&quality=100&sign=48be705a&sv=2)

lightdm greeter session

### LightDM

LightDM is a free and open-source X display manager that aims to be lightweight, fast, extensible and multi-desktop.

> **LightDM** is the display manager running in Ubuntu up to version 16.04 LTS. While it has been replaced by GDM in later Ubuntu releases

### /etc/lightdm

LightDM configuration is located in /etc/lightdm directory:

lets see some confiurations inside /etc/lightdm/lightdm.conf :

In some distributions (ubuntu )configuration files are located inside lightdm.conf.d directory:

#### changing greeter session:

For instance lets install another greeter session for lightdm and test it

next we need to edit lightdm.conf and change line bellow:

restart lightdm using `systemctl restart lightdm` and see the result:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-jAiFDQDcgmuCMGSkG%252F-M-jLXSKmAsGA6nyvHL3%252Fdisplaymanager-slickgreeter.jpg%3Falt%3Dmedia%26token%3Dfeadbd97-3ef4-446b-9730-cbc6fe2e7cc2&width=768&dpr=4&quality=100&sign=5868c600&sv=2)

slick greeter for lightdm

#### Controlling Display managers

Installing and switching between different Display Managers is pretty easy , as we have seen in CentOS, we can install new DM via `yum /apt` commands. Next some modifications in configuration files might be needed example `/etc/lightdm/lightdm.conf` .And finally we should enable previous DM and enable the new one with `systemctl enable/disable lightdm` commands and `reboot`.

For disabling Display Manager ang going to text mode it depends on your distribution! We can either use `telinit` command or set default target via `systemctl set-default` command.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-106-2/>

<https://opensource.com/article/16/12/yearbook-best-couple-2016-display-manager-and-window-manager>

<https://en.wikipedia.org/wiki/LightDM>

<https://wiki.ubuntu.com/LightDM>

.

Copy

# 106.3. Accessibility

**Weight:** 1

**Description:** Demonstrate knowledge and awareness of accessibility technologies.

**Key Knowledge Areas:**

* Basic knowledge of keyboard accessibility settings (AccessX)
* Basic knowledge of visual settings and themes
* Basic knowledge of assistive technology (ATs)

**Terms and Utilities:**

* Sticky/Repeat Keys
* Slow/Bounce/Toggle Keys
* Mouse Keys
* High Contrast/Large Print Desktop Themes
* Screen Reader
* Braille Display
* Screen Magnifier
* On-Screen Keyboard
* Gestures (used at login, for example GDM)
* Orca
* GOK
* emacspeak

There are some people with disabilities . A disability is any condition that makes it more difficult for a person to do certain activities or interact with the world around them. People with disabilities might like to work with Linux too . The good news is that Linux distributions provide great advantages over proprietary alternatives for people with disabilities!

#### What is Accessibility?

Accessibility , means making software usable by disabled people. That includes blind people of course, but also people who have low vision, are deaf, colorblind, have only one hand, can move only a few fingers, or even only the eyes.

These options are available in display managers (login screen) and in major desktops (like gnome, kde, xfce, ...). Its logo is a human stretching its hands a legs.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-pP88V2fHmrXWeUd4z%252F-M-pjpconw0p9WPnTRob%252Faccsessibilty-login.jpg%3Falt%3Dmedia%26token%3D8a8a8a05-3692-451e-90ec-9458faa6c715&width=768&dpr=4&quality=100&sign=fb8dbb36&sv=2)

> In Gnome the config is located at Settings ~ Universal Access.

Linux provides accessibility in 3 sections:

1. **AccessX :****AccessX** or the **Keyboard Accessibility** preference tool allows you to set some options for people who have difficulty with keyboard .
2. **Visual Settings :** Visual Settings help people with vision problems:
3. **Assistive Technologies :** things like text-to-speech (tts)

### AccessX

* **Sticky keys**: Helps users who have trouble pressing multiple keys at once, and users who have use of only one hand
* **Slow keys** allows the user to specify the duration for which one must press-and-hold a **key** before the system accepts the keypress.
* **BounceKeys:** Requires a delay between keystrokes before accepting the next keypress .
* **MouseKeys:** Enables a group of keys to emulate a mouse. Pressing keys in this group will move a pointer around the screen and perform mouse button actions.
* **RepeatKeys:** Enables the user who has trouble releasing keys quickly once they press to slow down how fast keys start repeating once they're pressed.
* **Hover Click:**  Enable **click** or drag simply by **hovering** **mouse** pointer over a control or object on the screen.

### Visual Settings

* **High-contrast** : Helps users who have trouble seeing text unless contrast is corrected, such as white text on a black background, or vice versa.
* **zoom (Magnifier)** : Helps users with visual impairments who need larger text and images.
* **Large Text**: Make reading text easier by using larger fonts in menus.
* **On screen keyboard**: Helps users who cannot type at all, but who can use a mouse.

**GOK** is the *Gnome On-Screen Keyboard*. As the title implies, it is a keyboard that appears on the display as an alternative for those who are not able to use a regular keyboard.

* **Visual alerts**: Replace system sounds with visual cues(like flashing th e screen)
* **Screen reader**: A text-to-speech system to read what's on the screen

### Text to speech

There are some Text to speech software in Linux which read dialog boxes for us . Software like **orca** and **emac speak** .

.

.

.

<https://lwn.net/Articles/302159/>

<https://opensource.com/life/15/5/accessibility-linux><https://accessibility.linuxfoundation.org/a11yweb/presentations/2005f2f/johnson-20050124-accessx.html>

<https://wiki.ubuntu.com/Accessibility/Reviews/GOK>

<https://jadi.gitbooks.io/lpic1/content/1063_accessibility.html>

.

Copy

# 107.1. Manage user and group accounts and related system files

## **107.1 Manage user and group accounts and related system files**

**Weight:** 5

**Description:** Candidates should be able to add, remove, suspend and change user accounts.

**Key Knowledge Areas:**

* Add, modify and remove users and groups
* Manage user/group info in password/group databases
* Create and manage special purpose and limited accounts

**Terms and Utilities:**

* /etc/passwd
* /etc/shadow
* /etc/group
* /etc/skel/
* chage
* getent
* groupadd
* groupdel
* groupmod
* passwd
* useradd
* userdel
* usermod

## Changing password

### passwd

The passwd command changes passwords for user accounts. A normal user can only change the password for their own account, but the superuser can change the password for any account.

1. Before a normal user can change their own password, they must first enter their current password for verification. (The superuser can bypass this step when changing another user's password.)
2. After the current password has been verified, **passwd** checks to see if the user is allowed to change their password at this time or not. Then user is then prompted twice.
3. Next, the password is tested for complexity.passwords should consist of at least 6 characters.

The root user can change any users password to anything (weak passwords) without providing their current password:

> Groups can also have passwords, which you set with the `gpasswd` command, but it is not used at all!

## Users and Groups

We have learned that Linux is a multiuser system.Recall that we can log in as one user and become another user by using the su or sudo commands.

Linux also has the concept of groups .

* each user belongs to one primary group and possibly to additional groups.
* Each file belongs to one user and one group

We learn how to create, delete, and manage users and groups.

## Managing users

### useradd

We add a user to a Linux system with the `useradd` command.

switch

description

-d

home directory of the new account

-m

create the user's home directory

-s

login shell of the new account

-G

add to Additional Groups

-c

comment, most of the time user's actual name

In most distributions useradd creates home directory for the new user but we can make sure using -m switch. example(ubunru 16):

### /etc/skel

#### The home directory skeleton

When you create a new user and a new home directory is created, the directory is populated with several files and subdirectories that, by default, are copied from /etc/skel.

### usermod

We can use the `usermod` command to modify a user account. we can use most of the options that you use with `useradd`, except that you cannot create or populate a new home directory for the user.

switch

description

-L

lock the user account

-U

unlock the user account

-g

force use GROUP as new primary group

-G

new list of Additional GROUPS ( user will be removed from all previous Additional groups )

-aG

append the user to the Additional GROUPS(without removing him/her from other groups)

### userdel

We can delete a user with the `userdel` command.

userdel by default does not remove user's home directory.

switch

description

-f

force removal of files

-r

remove home directory and mail spool

### Managing Groups

Similarly, we can add or delete groups with the `groupadd` and `groupdel` commands.

### groupadd

switch

description

-g

use GID for the new group

-f

exit successfully if the group already exists, and cancel -g if the GID is already used

-p

use this encrypted password for the new group

### groupmod

When you need to modify group information, use the `groupmod` command.

switch

description

-n

change the group name

-g

change the group ID

### groupdel

In fact, the `groupdel` command to delete a group requires only the group name; it has no options. You cannot delete any group that is the primary group of a user.

> Note: If root deletes a group with members, people wont be deleted! They will just wont be the members of that group anymore.

When we run ‘**useradd**‘ command in Linux terminal, it performs following major things:

1. It edits /etc/passwd, /etc/shadow, /etc/group and /etc/gshadow files for the newly created User account.
2. Creates and populate a home directory for the new user.
3. Sets permissions and ownerships to home directory.

What are those files?

### /etc/passwd

/etc/passwd is the *password* file containing basic information about users.

it has one line for each user in the system. the format of it is :

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-xV6NvGIwnVZSFslRk%252F-M-xXILE5b7f5HWgH25F%252Fusergroup-passwd.jpg%3Falt%3Dmedia%26token%3D66c41acb-d156-4b68-a36b-ca9eb85353c1&width=768&dpr=4&quality=100&sign=16f1fccb&sv=2)

1. **Username**: should be between 1 and 32 characters
2. **Password** *(will be discussed)*
3. **User ID (UID)**: Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
4. **Group ID (GID)**: The primary group ID (stored in /etc/group file)
5. **The comment field**. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.
6. **Home directory**
7. **Command/shell**: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. It does not have to be a shell.

> There are some users with /sbin/nologin shell, They are actually system accounts that run a service and no one can interactively login using them. Some times it has been set to /bin/false.

Every user should have read access to /etc/passwd :

In old days there was a place that all users information even the user's password, and it is not so hard thick about security issue that it caused. To solve the problem /etc/shadow was invented. An x character indicates that encrypted password is stored in /etc/shadow file

### /etc/shadow

The /etc/shadow file contains encrypted passwords, along with password- and account-expiration information.

Lets see what's inside that:

> Note: !! means user can not log in with any passwords. Most of service accounts are like this.

Passwords can be encrypted with one of several encryption algorithms. Older systems used DES or MD5, but modern systems typically use Blowfish, SHA-256, or SHA-512, or possibly MD5. Regardless of encryption algorithm, passwords are *salted* so that two otherwise identical passwords do not generate the same encrypted value.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-tH8V4bCqGZvE_tGPg%252F-M-uLHrRjDOKr9qaPRDE%252Fusergroup-shadow.jpg%3Falt%3Dmedia%26token%3D49888624-e4c5-422d-b92a-a8f25c44707b&width=768&dpr=4&quality=100&sign=291c39d0&sv=2)

1. **Username** : It is your login name.
2. **Password** : It is your encrypted password. The password should be minimum 8-12 characters long including special characters, digits, lower case alphabetic and more. Usually password format is set to `$id$salt$hashed`, *The $id is the algorithm used On GNU/Linux as follows: $1$ is MD5 $2a$ is Blowfish $2y$ is Blowfish $5$ is SHA-256 $6$ is SHA-512*
3. **Last password change (lastchanged)** : Days since Jan 1, 1970 that password was last changed
4. **Minimum** : The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
5. **Maximum** : The maximum number of days the password is valid (after that user is forced to change his/her password)
6. **Warn** : The number of days before password is to expire that user is warned that his/her password must be changed
7. **Inactive** : The number of days after password expires that account is disabled
8. **Expire** : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.

The last 6 fields provides password aging and account lockout features. You need to use the chage command to setup password aging.

**epoch time**

Unix time is a system for describing a point in time. It is the number of seconds that have elapsed since the Unix epoch, that is the time 00:00:00 UTC on 1 January 1970, minus leap seconds.

### chage

**chage** command is used to view and change the user password expiry information. This command is used when the login is to be provided for a user for limited amount of time or when it is necessary to change the login password time to time.

chage without any options lets do editing all items interactively ,lets try -l option on user1:

> `chage -d 0 user-name` will force user to change his password in next login.

> **passwd** can also change or reset the account's validity period — how much time can pass before the password expires and must be changed.

### /etc/group

/etc/group is the *group* file containing basic information about groups and which users belong to them. It contains one line for each group in the system.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M-uX009cWq3fZAo_bx8%252F-M-ualu_vYKb6HRcJ6GH%252Fusergroup-group.jpg%3Falt%3Dmedia%26token%3D9c66a7c4-ae41-4661-a751-6c3eec0798aa&width=768&dpr=4&quality=100&sign=beabdb0f&sv=2)

1. **group\_name**: It is the name of group. If you run ls -l command, you will see this name printed in the group field.
2. **Password**: Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups.
3. **Group ID (GID)**: Each user must be assigned a group ID. You can see this number in your /etc/passwd file.
4. **Group List**: It is a list of user names of users who are members of the group. The user names, must be separated by commas.

Like /etc/passwd file, /etc/group is shadowed for security reasons and must be world readable, but encrypted passwords should not be world readable.

groups password are stored in /etc/gshadow file which is readable only by root.

> its format is :
>
> `Group name:Encrypted password:Group administrators: Group members`

> ! :groups can have passwords but it have never been used in any distribution!

### getent

**getent** is a Linux command that helps the user to get the entries in a number of important text files called databases.

we use the getent command for processing groups and user information, instead of manually reading /etc/passwd, /etc/groups.

do not forget to use id command.

.

.

.

**Bonus:** Commands and options for changing user accounts

usermod

passwd

chage

Purpose

-L

-l(lowercase L)

N/A

Lock or suspend the account.

-U

-u

N/A

Unlock the account.

N/A

-d

N/A

Disable account by setting it passwordless

-e

-f

-E

Set the expiration date for an account.

N/A

-n

-m

The minimum password lifetime in days.

N/A

-X

-M

The maximum password lifetime in days.

N/A

-W

-W

The number of days of warning before a password must be changed.

-f

-i

-I(uppercase i)

The number of days after a password expires until the account is disabled.

N/A

-S

-l(lowercase L)

Output a short message about the current account status.

.

.

.

<https://developer.ibm.com/technologies/linux/tutorials/l-lpic1-map/>

<https://www.computerhope.com/unix/upasswor.htm>

<https://jadi.gitbooks.io/lpic1/content/1071_manage_user_and_group_accounts_and_related_system_files.html>

<https://askubuntu.com/questions/639990/what-is-the-group-id-of-this-group-name>

<https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/>

<https://www.cyberciti.biz/faq/understanding-etcshadow-file/>

<https://en.wikipedia.org/wiki/Unix_time>

<https://www.cyberciti.biz/faq/understanding-etcgroup-file/>

<https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/4/html/Introduction_To_System_Administration/s3-acctsgrps-gshadow.html>

<https://www.geeksforgeeks.org/chage-command-in-linux-with-examples/>

.

Copy

# 107.2. Automate system administration tasks by scheduling jobs

**Weight:** 4

Description: Candidates should be able to use cron or anacron to run jobs at regular intervals and to use at to run jobs at a specific time.

**Key Knowledge Areas:**

* Manage cron and at jobs
* Configure user access to cron and at services
* Configure anacron

**Terms and Utilities:**

* /etc/cron.{d,daily,hourly,monthly,weekly}/
* /etc/at.deny
* /etc/at.allow
* /etc/crontab
* /etc/cron.allow
* /etc/cron.deny
* /var/spool/cron/
* crontab
* at
* atq
* atrm
* anacron
* /etc/anacrontab

Many system administration tasks must be done regularly, such as rotating log files, backing up files or databases, preparing reports, or installing system updates. In this lesson we will learn how to automate these kinds of jobs by setting up scheduling for them

By scheduling :

* We can start a job for a time at which system usage is low
* Errors will be reduced due to less manual interaction is needed.
* We are sure that jobs always run the same way
* System administrators can sleep more!

### Run jobs at regular intervals

Linux systems have two facilities for scheduling jobs to run at regular intervals:

* The original `cron` facility is best suited to servers and systems that are continuously powered on.
* The `anacron` (or anachronistic `cron`) facility is suited to systems such as desktops or laptops that can be asleep or running on battery power.

cron

anacron

Good for servers

Good for laptops and desktops

Granularity from one minute to one year

Daily, weekly, and monthly granularity

Job runs only if system is running at scheduled time

Job runs when system is next available

Can be used by normal users

Needs root authority

### Schedule periodic jobs with cron

The `cron` facility consists of the `cron` daemon and a set of tables that describe what work is to be done and with what frequency. The `cron` daemon is usually started by the `init`, `upstart`, or `systemd` process at system startup.

### crontab file syntax and Operators

Crontab (cron table) is a text file that specifies the schedule of cron jobs. The `cron` daemon wakes up every minute and checks each crontab for jobs that need to run.

There are two types of crontab files. The individual user crontab files and system-wide crontab files.

#### crontab syntax and operators

Each line in the user crontab file contains six fields separated by a space followed by the command to be run.

* `*` -The asterisk operator means any value or always.
* `,` -The comma operator allows you to specify a list of values for repetition.
* `-` -The hyphen operator allows you to specify a range of values.
* `/` -The slash operator allows you to specify values that will be repeated over a certain interval between them.

> Also if you have `@reboot` or `@daily` instead of time fields, the command will be run once after the reboot or daily.

Lets see some examples:

## user specific crons

### /var/spool/cron/

Users crontab files are stored by the user’s name, and their location varies by operating systems. In Red Hat based system such as CentOS, crontab files are stored in the `/var/spool/cron` directory while on Debian and Ubuntu files are stored in the `/var/spool/cron/crontabs` directory.

Although you can edit the user crontab files manually, it is recommended to use the `crontab` command.

### crontab command

The crontab command allows you to install or open a crontab file for editing.

You can use the crontab command to view, add, remove, or modify cron jobs using the following options:

* `crontab -e` : Edit crontab file, or create one if it doesn’t already exist.
* `crontab -l` : Display crontab file contents.
* `crontab -r` : Remove your current crontab file.
* `crontab -i` :Remove your current crontab file with a prompt before removal.
* `crontab -u`  : Edit other user crontab file. Requires system administrator privileges.

The crontab -e command opens the crontab file using the editor specified by the `VISUAL` or `EDITOR` environment variables.

as an example add bellow line to above and it would send and email every 5 mintues:

crontab -e also check the syntax before exiting the file , which is really helpful.

crontab -l would show the above contents. Lets check if user crontab file has been created:

## system wide cron

In addition to the user crontab files in /var/spool/cron, the `cron` daemon also checks /etc/crontab and any crontabs in the /etc/cron.d directory.

### /etc/crontab , /etc/cron.d

`/etc/crontab` and the files inside the `/etc/cron.d` directory are system-wide **crontab** files that can be edited only by the system administrators.

> /etc/crontab is updated by direct editing. You cannot use the `crontab` command to update file files or files in the /etc/cron.d directory.

#### System-wide Crontab Files

The syntax of system-wide crontab files is slightly different than user crontabs. It contains an additional mandatory user field that specifies which user will run the cron job.

This file should be edited with an editor directly and we can mention which user runs command(s).

### /etc/cron.{daily,hourly,monthly,weekly}/

In most Linux distributions you can also put **scripts** inside the `/etc/cron.{hourly,daily,weekly,monthly}` directories and the scripts will be executed every `hour/day/week/month`.

as an example lets take look at one of them:

### anacron

The cron facility works well for systems that run continuously.If the system is down when the cron should run a task, that cron job wont run till the next occurrence! But anacron creates the timestamp each time a daily, weekly or monthly job runs.

> Note: anacron checks the timestamps at BOOT TIME and does not handle jobs that must run hourly or every minute.

> ### /etc/anacron

The table of jobs for `anacron` is stored in /etc/anacrontab, which has a slightly different format from /etc/crontab.

> just like/etc/crontab , /etc/anacrontab is updated by direct editing.

#### Anacrontab Format

* **period in days** : specifies the frequency of execution of a job in *N* days.
* **delay in minutes**: number of minutes anacron should wait before executing the job after reboot.
* **job-identifier :**It is the name for the job’s timestamp file. It should be unique for each job. This will be available as a file under the /var/spool/anacron directory.
* **command**: specifies the command to execute.

### /var/spool/anacron

`anacron` keeps a time stamp file in /var/spool/anacron for each job to record when the job runs. When `anacron` runs, it checks to see if the required number of days has passed since a job last ran and runs the job if necessary.

This file will contain a single line that indicates the last time when this job was executed.

### at

Sometimes you need to run a job at a future time just once, rather than regularly. For this purpose you use the `at` command. (ubuntu: `apt install at`)

A typical **at** command sequence looks like this

By running at command It then places you at a special prompt, where you can type in the command (or series of commands) to be run at the scheduled time. When you're done, press **Control-D** on a new line, and your command will be placed in the queue.

> warning: commands will be executed using /bin/sh

Some other examples of at command:

at command has other members in its family:

### atq

lists the pending jobs of users

### atrm

delete jobs by their job number

atq command only shows the list of jobs but if you want to check what script/commands are scheduled with that task use `at -c JobNum` command and see the last line.

both cron and are system services.

## Configure user access to job scheduling

We can control access to the crontab command by using two files in the /etc/cron.d directory: cron.deny and cron.allow. These files permit only specified users to perform crontab command tasks such as creating, editing, displaying, or removing their own crontab files.

> The cron.deny and cron.allow files consist of a list of user names, one user name per line.

### /etc/cron.allow , /etc/cron.deny

These access control files work together as follows:

* If cron.allow exists, only the users who are listed in this file can create, edit, display, or remove crontab files.
* If cron.allow does not exist, all users can submit crontab files, except for users who are listed in cron.deny.
* If neither cron.allow nor cron.deny exists, superuser privileges are required to run the crontab command.

Superuser privileges are required to edit or create the cron.deny and cron.allow files.

### /etc/at.allow , /etc/at.deny

The corresponding /etc/at.allow and /etc/at.deny files have similar effects for the `at` facility.

.

.

.

### Crontab Variables

The cron daemon automatically sets several environment variables.

* The default path is set to `PATH=/usr/bin:/bin`. If the command you are calling is present in the cron specified path, you can either use the absolute path to the command or change the cron `$PATH` variable. You can’t implicitly append `:$PATH` as you would do with a regular script.
* The default shell is set to `/bin/sh`. You can set a different shell by changing the `SHELL` variable.
* Cron invokes the command from the user’s home directory. The `HOME` variable can be overridden by settings in the crontab.
* The email notification is sent to the owner of the crontab. To overwrite the default behavior, you can use the `MAILTO` environment variable with a list (comma separated) of all the email addresses you want to receive the email notifications. If `MAILTO` is defined but empty (`MAILTO=""`), no mail is sent.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-107-2/>

<https://linuxize.com/post/scheduling-cron-jobs-with-crontab/>

<https://jadi.gitbooks.io/lpic1/content/1072_automate_system_administration_tasks_by_scheduling_jobs.html>

<https://www.thegeekdiary.com/centos-rhel-anacron-basics-what-is-anacron-and-how-to-configure-it/>

<https://www.thegeekstuff.com/2011/05/anacron-examples/>

<https://www.computerhope.com/unix/uat.htm>

<https://tecadmin.net/one-time-task-scheduling-using-at-commad-in-linux/>

<https://docs.oracle.com/cd/E19253-01/817-0403/sysrescron-23/index.html>

.

Copy

# 107.3. Localisation and internationalisation

**Weight:** 3

**Description:** Candidates should be able to localize a system in a different language than English. As well, an understanding of why LANG=C is useful when scripting.

**Key Knowledge Areas:**

* Configure locale settings and environment variables
* Configure timezone settings and environment variables

**Terms and Utilities:**

* /etc/timezone
* /etc/localtime
* /usr/share/zoneinfo/
* LC\_\*
* LC\_ALL
* LANG
* TZ
* /usr/bin/locale
* tzselect
* timedatectl
* date
* iconv
* UTF-8
* ISO-8859
* ASCII
* Unicode

There are thousands of different languages used throughout the world. Numbers and dates can be formatted differently, and there are over 40 alphabets in existence. People use either a 12-hour clock or a 24-hour clock for time. There are also different systems of measurement. In this lesson we will learn how to configure our Linux system to adapt it to our *locale* .

## timezone

The term time zone can be used to describe several different things, but mostly it refers to the local time of a region or a country.The local time within a time zone is defined by its difference from Coordinated Universal Time (UTC), the world's time standard.

There are a number of time management utilities available on Linux such as **date** and **timedatectl** commands to get the current timezone of system.

### date

**date** command is used to display the system date and time. date command is also used to set date and time of the system. By default the date command displays the date in the time zone on which unix/linux operating system is configured.You must be the super-user (root) to change the date and time.(ubuntu16)

`date -u` Displays the time in GMT(Greenwich Mean Time)/UTC(Coordinated Universal Time )time zone.

**Date forma**t : FORMAT is a sequence of characters which specifies how output will appear. The syntax is The syntax is `date +%`  :

date format option

Purpose of Option

%Y

year

%y

last two digits of year (00..99)

%m

month (01..12)

%d

day of month (e.g., 01)

%D

%D date; same as %m/%d/%y

%H

hour (00..23)

%M

minute (00..59)

### timedatectl

For all Linux distributions that use systemd. There should be a timedatectl command.

The timedatectl command allows us to query and change the configuration of the system clock and its settings, we can use this command to set or change the current date, time and timezone or enable automatic system clock synchronization with a remote NTP server (Next lesson).

#### Configuring user time zone

We can configure our time zone during OS installation process, using GUI, or we can use date and time setting in the GUI panel But as always there are some terminal tools which help us. In old days tzconfig command were used but it has been deprecated, instead use tzselect:

### tzselect

The **tzselect** program asks the user for information about the current location, and outputs the resulting timezone description to standard output. The output is suitable as a value for the **TZ** environment variable.

At the end the process suggest us to set TZ (Time Zone) Environment variable:

As noted in the output, you can set and export it in your .profile file if you want to use a time zone that is different from your system time zone.

#### configuring system time zone

### /usr/share/zoneinfo

The /usr/share/zoneinfo is a directory which keeps all the timezone info.

and it contains required time zone binary files:

### /etc/localtime

Linux looks at /etc/localtime to determine the current time of your machine. This can either be a symbolic link to the correct time zone or a direct copy of the time zone file.

we can use one of bellow commands to change or system time zone(Tehran):

* `ln -s /usr/share/zoneinfo/Asia/Tehran /etc/localtime`
* `cp /usr/share/zoneinfo/Asia/Tehran /etc/localtime`

> if you got an error while trying to create symlink, remove it first: `sudo unlink /etc/localtime` or  `sudo rm -rf /etc/localtime`

### /etc/timezone

This file is holding timezone name on debian based systems. `/etc/sysconfig/clock`  is holding timezone name on RHEL based systems.

There are some other ways to configure the time zone on Linux distributions.

* using **timedatectl** in distributions with systemd:`timedatectl set-timezone Europe/Amsterdam`
* Using dpkg-reconfigure in (Debian/Ubuntu) distributions: `dpkg-reconfigure tzdata`

## Configuring Languages

We can configure system languages from settings (Regional&Languages) but there is always terminal tools

### locale

A **locale** is a set of environmental variables that defines the language, country, and character encoding settings (or any other special variant preferences) for your applications and shell session on a Linux system. These environmental variables are used by system libraries and locale-aware applications on the system.

> To view information about the current installed locale, use the **locale** :

> variables format is like: "Language\_COUNTRY.*ENCODING"*

### LANG

The **LANG** environment variable value is established at installation. (This Provides default value for LC\_\* variables unless that variable is set).

* LANGUAGE
* LC\_CTYPE How characters are classified as letters, numbers etc. This determines things like how characters are converted between upper and lower case.
* LC\_NUMERIC How you format your numbers. For example, in many countries a period (.) is used as a decimal separator, while others use a comma (,).
* LC\_TIME How your time and date are formatted. Use for example "en\_DK.UTF-8" to get a 24-hour-clock in some programs.
* LC\_COLLATE How strings (file names...) are alphabetically sorted. Using the "C" or "POSIX" locale here results in a strcmp()-like sort order, which may be preferable to language-specific locales.
* LC\_MONETARY What currency you use, its name, and its symbol.
* LC\_MESSAGES What language should be used for system messages.
* LC\_PAPER Paper sizes: 11 x 17 inches, A4, etc.
* LC\_NAME How names are represented (surname first or last, etc.).
* LC\_ADDRESS How addresses are formatted (country first or last, where zip code goes etc.).
* LC\_TELEPHONE What your telephone numbers look like.
* LC\_MEASUREMENT What units of measurement are used (feet, meters, pounds, kilos etc.).
* LC\_IDENTIFICATION Metadata about the locale information.

as an example, lets change LC\_TIME to another thing:

### LC\_ALL

Overrides the value of the **LANG** environment variable and the values of any other **LC\_\*** environment variables.

> we can also use bellow command to work with locale ans set or install languages :
>
> * `dpkg-reconfigure locales` (Debian)
> * `system-config-language` (Redhat)
>
> there is also *localectl* in systemd systems, which display and control system locale settings.

### LANG=C

The LANG=C does two things:

* It forces applications to use the default language for output:

* forces sorting to be byte-wise

It is also possible to do a LC\_ALL=C.

### Character Encoding

A computer represents information in numbers and, when they need to be communicated to Humans (and vice versa) they need to be encoded.

* **ASCII** is a seven-bit encoding technique which assigns a number to each of the 128 characters used most frequently in American English. This allows most computers to record and display basic text. ASCII does not include symbols frequently used in other countries, such as the British pound symbol or the German umlaut. ASCII is understood by almost all email and communications software.
* **ISO 8859** is an eight-bit extension to ASCII developed by ISO (the International Organization for Standardization). ISO 8859 includes the 128 ASCII characters along with an additional 128 characters, such as the British pound symbol and the American cent symbol. Several variations of the ISO 8859 standard exist for different language families
* **Unicode** is an attempt by ISO and the Unicode Consortium to develop a coding system for electronic text that includes every written alphabet in existence. Unicode uses 8-, 16-, or 32-bit characters depending on the specific representation, so Unicode documents often require up to twice as much disk space as ASCII

* ASCII: 7 bits. 128 code points.
* ISO-8859-1: 8 bits. 256 code points.
* UTF-8: 8-32 bits (1-4 bytes). 1,112,064 code points.

> Check for available encoding on your system with `locale -m` command.

> use `file` command to see character encoding of a file.

### iconv

We can use the `iconv` program to convert between character encodings. Obviously, if you go from a large character set to a smaller one, the conversion does not happen properly.

example:

If no input file is provided then it reads from standard input. Similarly, if no output file is given then it writes to standard output. Example:

> `iconv -l` list all known character set encodings..

.

.

<https://developer.ibm.com/technologies/linux/tutorials/l-lpic1-map/>

<https://www.tecmint.com/check-linux-timezone/>

<https://www.geeksforgeeks.org/date-command-linux-examples/>

<https://www.computerhope.com/unix/udate.htm>

<https://www.tecmint.com/set-time-timezone-and-synchronize-time-using-timedatectl-command/>

<https://www.timeanddate.com/time/time-zones.html>

<https://jadi.gitbooks.io/lpic1/content/1073_localisation_and_internationalisation.html>

<https://linux.die.net/man/8/tzselect>

<https://linuxacademy.com/blog/linux/changing-the-time-zone-in-linux-command-line/>

<https://www.2daygeek.com/linux-change-check-timezone/>

<https://linux-audit.com/configure-the-time-zone-tz-on-linux-systems/>

<https://help.ubuntu.com/community/Locale>

<https://docs.oracle.com/cd/E23824_01/html/E26033/glmbx.html>

<https://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do>

<https://www.praim.com/en/news/character-encodings-in-linux-ascii-utf-8-and-iso-8859/>

<https://kb.iu.edu/d/ahfr>

<https://www.geeksforgeeks.org/iconv-command-in-linux-with-examples/>

.

Copy

# 108.1. Maintain system time

## **108.1 Maintain system time**

**Weight:** 3

**Description:** Candidates should be able to properly maintain the system time and synchronize the clock via NTP.

**Key Knowledge Areas:**

* Set the system date and time
* Set the hardware clock to the correct time in UTC
* Configure the correct timezone
* Basic NTP configuration
* Knowledge of using the pool.ntp.org service
* Awareness of the ntpq command

**Terms and Utilities:**

* /usr/share/zoneinfo/
* /etc/timezone
* /etc/localtime
* /etc/ntp.conf
* date
* hwclock
* ntpd
* ntpdate
* pool.ntp.org

When we install a Linux® system graphically, we set the clock and choose a time zone suitable for our needs ,we can also choose to use the Network Time Protocol (NTP) to set your clock automatically. In this lesson we show how to go below the graphical interfaces and configure the various time-related aspects of Linux system.

#### How Linux keep tack of time

there are 2 clocks in each computer. The first is the Hardware Clock. This is the clock on a motherboard chip that keeps time even when the machine is powered off.

The other clock is the virtual System Clock. Linux asks the Hardware Clock chip what time it is on power up and then keeps track of the time itself with software.

Hardware clock can be the localtime (your computers timezone) or UTC time (standard time).

> We can determine which one is set by checking /etc/adjtime . This file is empty unless the Hardware has been set manually.

Usually the hardware clock is set on UTC , so when ever system boots up, Software clock reads Hardware clock and then calculates the difference based on our timezone.

#### Setting The System Clock

### date

**date** command is used to display the system date and time. By default the date command displays the date in local time, even if your hardware clock keeps UTC. Use the `-u` option to display UTC.

Use the `-u` option to display UTC:

date command is also used to set date and time of the system ( Automatic Adjustment (ntp) should not be enabled, otherwise it won't work):

Although we can set time using date command, the big problem with this idea is that time change will only last until the next reboot. Unless we somehow set the system time to the hardware clock.

### Setting The Hardware Clock

### hwclock

To change the Hardware Clock, you can use the motherboard’s BIOS utility at startup, but if you miss that opportunity, there is still hope. The "hwclock" command.

`hwclock` is a utility for accessing the hardware clock, also referred to as the Real Time Clock (RTC). As we mentioned it is independent of the operating system you use and works even when the machine is shut down.

> hwclock date shows the date in the localtime (time after adding the timezone to the UTC time) , even when the hardware clock is set on UTC!

hwclock syntax : `hwclock [function] [option...]` where :

lets do some examples:

the hwclock --localtime -w would do the same thing , but setting hardware clock to your local time is not a good idea, so use hwclock -u -w instead.

### NTP

**Network Time Protocol (NTP)** is an application layer protocol used for clock synchronization between hosts on a TCP/IP network. The goal of NTP is to ensure that all computers on a network agree on the time, since even a small difference can create problems.

NTP uses a hierarchical system of time sources. At the top of the structure are highly accurate time sources – typically atomic or GPS clocks. These clocks are known as **stratum 0** servers. **Stratum 1** servers are directly linked to stratum 0 servers and computers run NTP servers that deliver the time to **stratum 2** servers, and so on (image source: Wikipedia):

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0JOOL4hYaYrD9Y63o1%252F-M0JUti2Hp0zmQ_uBLj_%252Fmaintaintime-ntp.jpg%3Falt%3Dmedia%26token%3Dc6da1182-6729-440b-ad58-05bb4138ef09&width=768&dpr=4&quality=100&sign=5466326b&sv=2)

> NTP uses a client-server architecture; one host is configured as the NTP server and all other hosts on the network are configured as NTP clients.

### pool.ntp.org

The pool.ntp.org project is a big virtual cluster of timeservers providing reliable easy to use NTP service for millions of clients.

The pool is being used by hundreds of millions of systems around the world. It's the default "time server" for most of the major Linux distributions and many networked appliances

### ntpdate

**ntpdate** sets the local date and time by polling the Network Time Protocol (NTP) **server**(s) given as the server arguments to determine the correct time. It must be run as root on the local host. (you might need to install it). `-v` : verbose

After this, we need to set the hwclock to the just corrected system time by sudo `hwclock -w` or `hwclock -u -w` to make sure you are setting that on utc .

> -q switch will query for time and just show the result with out setting that.

### ntpd

Instead of manually setting the time each time, we can use a linux service called ntp. The `ntpd` utility is an operating system daemon which sets and maintains the system time of day in synchronism with Internet standard time servers.

Fun fact: we can not use natpdate while ntp service is running:

### /etc/ntp.cpnf

The ntpd configuration file is located at **/etc/ntp.conf**. It is read at initial startup by the ntpd daemon in order to specify the appropriate synchronization sources:

You can change the ntp servers to the ntp server(s) you want. Do not forget to restart the service after any modifications.

### ntpq

The **ntpq** utility program is used to monitor NTP daemon **ntpd** operations and determine performance.

`-p :`Print a list of the peers known to the server as well as a summary of their state.

**-n** : Output all host addresses in dotted-quad numeric format rather than converting to the canonical host names.

the meaning :

tha's all.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-108-1/>

<http://xed.ch/help/time.html>

<https://www.geeksforgeeks.org/date-command-linux-examples/>

<https://jadi.gitbooks.io/lpic1/content/1081_maintain_system_time.html>

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-configuring_the_date_and_time-hwclock>

<https://www.geeksforgeeks.org/hwclock-command-in-linux-with-examples/>

<https://geek-university.com/ccna/network-time-protocol/>

<https://www.ntppool.org/en/>

<https://linux.die.net/man/8/ntpdate>

<https://docs.ntpsec.org/latest/ntpd.html>

<https://detailed.wordpress.com/2017/10/22/understanding-ntpq-output/>

.

Copy

# 108.2. System logging

**Weight:** 3

**Description:** Candidates should be able to configure the syslog daemon. This objective also includes configuring the logging daemon to send log output to a central log server or accept log output as a central log server. Use of the systemd journal subsystem is covered. Also, awareness of rsyslog and syslog-ng as alternative logging systems is included.

**Key Knowledge Areas:**

* Configuration of the syslog daemon
* Understanding of standard facilities, priorities and actions
* Configuration of logrotate
* Awareness of rsyslog and syslog-ng

**Terms and Utilities:**

* syslog.conf
* syslogd
* klogd
* /var/log/
* logger
* logrotate
* /etc/logrotate.conf
* /etc/logrotate.d/
* journalctl
* /etc/systemd/journald.conf
* /var/log/journal/

#### Why Logging?

A Linux system has many subsystems and applications running. We use system logging to gather data about our running system from the moment it boots. Sometimes we just need to know that all is well. At other times we use this data for auditing, debugging, knowing when a disk or other resource is running out of capacity, and many other purposes.

### syslog

Syslog is a standard for sending and receiving notification messages–in a particular format–from various network devices. The messages include time stamps, event messages, severity, host IP addresses, diagnostics and more.

### syslogd

The syslog daemon is a server process that provides a message logging facility for application and system processes.Unfortunately linux logging is one of aspects of linux which is transition fase. The traditional syslog facility and its syslogd daemon has been supplemented by other logging facilities such as rsyslog, syslog-ng, and the systemd journal subsystem.

### syslog.conf

The syslog.conf file is the main configuration file for the **syslogd.** Whenever syslogd receives a log message, it acts based on the message's type (or facility) and its priority (called selector fields).

**Facilities** are simply categories. Some facilities in Linux are: `auth, user, kern, cron, daemon, mail, local1, local2, ...`

* `auth`: Security/authentication messages
* `user` : User-level messages
* `kern` : Kernel messages
* `corn` : Clock daemon
* `daemon` : System daemons
* `mail` : Mail system
* `local0 – local7` : Locally used facilities

**priorities** Unlike facilities, which have no relationship to each other, priorities are hierarchical. Possible priorities in Linux are: `emerg/panic, alert, crit, err/error, warn/warning, notice, info, debug`

1. `emerg :` System is unusable
2. `alert :` Action must be taken immediately
3. `critical :` Critical conditions
4. `err :` Error conditions
5. `warning :` Warning conditions
6. `notice :` Normal but significant conditions
7. `info :` Informational messages
8. `debug :` Debug-level messages

> if we log some specific priority , all the more important things will be logged too

**Action:** Each line in this file specifies one or more facility/priority selectors followed by an action . On the action field we can have things like:

action

example

notes

filename

/var/log/messages

Writes logs to specified file

username

user2

Will notify that person on the screen

@ip

@192.168.10.42

Will send logs to specified log server and that server decides how to treat logs based on its configs.

In the following syslog.conf line, mail.notice is the selector and /var/log/mail is the action (i.e., “write messages to /var/log/mail”):

Within the selector, “mail” is the facility (message category) and “notice” is the level of priority. You can see part of syslog.conf (CentOS6) :

> `*`: wildcard . signifying “any facility” or "any priority"
>
> dash - : means it can use memory cache (:don't waist time constantly writing to the disk )
>
> equal sign = : to log ONLY one specific level of priority. `facility.=priority action`

There is also /etc/rsyslog.d/ directory and it is better for different softwares and admins to add their specific configs there, instead of editing the main configuration file (See Ubuntu16).

### klogd

How do boot-time kernel messages get logged before a file system is even mounted? The kernel stores messages in a ring buffer in memory. The `klogd` daemon processes these messages directly to a console, or a file such as /var/log/dmesg, or through the syslog facility.

### /var/log

Almost all logfiles are located under /var/log directory and its sub-directories on Linux(CentOS6).

You can use your favorite text editor or less or tail commands in conjunction with grep to read these log files.

### creating rsyslog listener

We can creating rsyslog listener and catch other systems log messages. That is pretty easy.

and finally do not forget to restart the service `systemctl restart rsyslog` .

### journalctl

Systemd also has its own journaling program called **journald** and it stores things in binary files. We can't go and see text files (like what we did in syslog/rsyslog), so we have to use special tool called journalctl to access them(CentOS7):

As we mentioned earlier , linux logging is one of aspects of linux which is in under change. Distributions with systemd has journald, beside that some of them still preserve rsyslog and some other not. Try to find out your linux logging system

### /etc/systemd/journald.conf

The config file of journalctl is located at /etc/systemd/journald.conf (CentOS7)

### logger

The Linux logger command provides an easy way to generate some logs(centOS6)

and it will appear at /var/log/syslog (or /var/log/messages):

### logrotate

With the amount of logging that is possible, we need to be able to control the size of log files. This is done using the `logrotate`utility , which is usually run as a cron job.

The important files to pay attention to are:

* /usr/sbin/logrotate -- the logrotate command itself (the executable)
* /etc/cron.daily/logrotate -- the shell script that runs logrotate on a daily basis (note that it might be /etc/cron.daily/logrotate.cron on some systems)
* /etc/logrotate.conf -- the log rotation configuration file

Another important file is /etc/logrotate.d, included in the process through this line in the /etc/logrotate.conf file:

### /etc/logrotate.conf

Use the /etc/logrotate.conf configuration file to specify how your log rotating and archiving should happen.

Each log file may be handled daily, weekly, monthly, or when it grows too large.

parameter

meaning

missingok

don’t write an error message if the log file is missing

daily, weekly, monthly

rotate logs daily, weekly, monthly

rotate *N*

keep the latest *N* logs and delete the older ones

compress

compress the log (creates gz files)

**create** mode owner group

Immediately after rotation (before the **postrotate** script is run) the log file is created with this acces and owner

minsize N

Log files are rotated when they grow bigger than size bytes, but not before the additionally specified time interval(daily,...)

this file contains some default settings and sets up rotation for a few logs that are not owned by any system packages. It also uses an `include` statement to pull in configuration from any file in the `/etc/logrotate.d` directory(CentOS6).

### /etc/logrotate.d

Any packages we install that need help with log rotation will place their Logrotate configuration here.

These are the meaning of some of these parameters:

parameter

meaning

missingok

don’t write an error message if the log file is missing

notifempty

don’t rotate the log file if it is empty.

shared scripts

Run **prerotate** and **postrotate** scripts for every log file which is rotated

delaycompress

Postpone compression of the previous log file to the next rotation cycle

That's all!

.

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-108-2/>

<https://stackify.com/syslog-101/>

<https://www.ibm.com/support/knowledgecenter/en/SSB23S_1.1.0.15/gtpc1/hsyslog.html>

<https://linux.die.net/man/5/syslog.conf>

<https://www.linuxjournal.com/article/5476>

<https://jadi.gitbooks.io/lpic1/content/1082_system_logging.html>

<https://en.wikipedia.org/wiki/Syslog>

<https://renenyffenegger.ch/notes/Linux/logging/klogd/index>

<https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/>

<https://www.digitalocean.com/community/tutorials/how-to-manage-logfiles-with-logrotate-on-ubuntu-16-04>

<https://linux.die.net/man/8/logrotate>

<https://www.digitalocean.com/community/tutorials/how-to-manage-logfiles-with-logrotate-on-ubuntu-16-04>

.

Copy

# 108.3. Mail Transfer Agent (MTA) basics

**Weight:** 3

**Description:** Candidates should be aware of the commonly available MTA programs and be able to perform basic forward and alias configuration on a client host. Other configuration files are not covered.

**Key Knowledge Areas:**

* Create e-mail aliases
* Configure e-mail forwarding
* Knowledge of commonly available MTA programs (postfix, sendmail, qmail, exim) (no configuration)

**Terms and Utilities:**

* ~/.forward
* sendmail emulation layer commands
* newaliases
* mail
* mailq
* postfix
* sendmail
* exim
* qmail

### MTAs

Mail transfer agents deliver mail between users and between systems. Most Internet mail uses the Simple Mail Transfer Protocol (SMTP), but local mail may be transferred through other possibilities. There are different kinds of MTAs available and each distribution might have one of them as default. As an administrator we can chose the right MTA based on our needs.

### sendmail

Sendmail is the oldest Linux MTA. It was originally derived from the delivermail program that was used on the ARPANET in 1979. sendmail is big and it is not easy to configure. Over the years many vulnerabilities have been found in sendmail although it's a bit enhanced now.

#### Other mail transfer agents

In response to security issues with sendmail, several other mail transfer agents were developed during the 1990’s. Postfix is perhaps the most popular, but qmail and exim are also widely used.

### qmail

Qmail is the one of the most secure Linux mail server software solutions on the market today. Although unsupported, and not currently in development (Qmail hasn't been updated since 1997), Qmail has a large fan base.

Qmail is also faster, and scales better with higher mail loads than Sendmail. However, Qmail is not easy to configure, or easy to extend.

> qmail is not a GPL software it is public domain.

### exim

Exim has been out since 1995, and growing in popularity ever since. The biggest strength of Exim is it's almost infinite level of customization. Exim supports the ability for a server administrator to create a custom ruleset that handles incoming and outgoing emails in any particular manner.(authentication, access control list)

Although Exim was not designed for performance, Exim can be configured to run as a high performance mail server. Exim is an excellent MTA if you need to create a complex or custom mail configuration.

### postfix

Postfix is possibly the fastest growing MTA on the market today. Postfix is extremely popular because of it's performance, and it's past security history. It is far harder (or almost impossible) to compromise the root user on a server that runs Postfix, than for instance Sendmail or Exim.

Postfix also runs faster with less system resources than most other MTAs (or at least, with standard configurations).Standard configurations are easy to create, but if you need a unique setup, it can be a pain with Postfix.

### sendmail emulation layer

As sendmail has been around so long , no matter which email server we use, it comes with send mail emulation layer. In other words, all of other MTAs include tools which are backward compatible. so if we type `sendmail` or `mailq` commands they respond and act as if sendmail is installed.

### Mail aliases

Sometimes you might want all the mail for a user to go to some other place. For example, you may have a server farm and want all the root mail to go to a central system administrator. Or you may want to create a mailing list where mail goes to several people. To do this, we use aliases that allow us to define one or more destinations for a given user name.

mail aliases are located in `/etc/aliases .` You must first become root before modifying this file: (CentOS7, output has been truncate)

So it if there is a message for `"lpic1"` it will be sent to the `root` user.

The last line tell that `payam` is reading `root` emails . This let `payam` to read `root` emails without login with root.

### newaliases

Modifications to the `/etc/aliases` file are not complete until the `newaliases` command is run to build `/etc/aliases.db`.

### mail command

There are plenty of ways for sending email while using GUI , using browser or with an email client. But options are limited when it comes to command line interface.

The `mail` command is an old standby that can be used to script the sending of mail as well as receive and manage your incoming mail. (CentOS: install mailx)

mail command example

usage

mail -s “subject” user1@domain.com

sending an email

mail -s “subject” user1@domain.com < /root/test.txt

send an email from a file

mail -s “subject” user1@domain.com -a /path/to/file

add an attachment

> It also can send email from within the scripts like 'echo -e "email content" | mail -s "email subject" "example@example.com"'

We can use `mail` interactively to send messages by passing a list of addressees, or with no arguments you can use it to look at your incoming mail.

Because of aliases we have modified, Any email which is sent to lpic1 email address would be forwarded to root, as we have define payam as a person who should get root's emails :

> Whenever a mail is sent, initially the mail command calls the mail binary, which in turns connects to the local MTA to send the mail to its destination. The local MTA is a locally running smtp server that accepts mails on port 25.

### ~/.forward

The aliases file must be managed by a system administrator. Individual users can enable forwarding of their own mail using a .forward file in their own home directory. You can put anything in your .forward file that is allowed on the right side of the aliases file. The file contains plain text and does not need to be compiled. When mail is destined for you, sendmail checks for a .forward file in your home directory and processes the entries the same way it processes aliases.

now lets end an email to user1 and check its mail box:

### mailq

Linux mail handling uses a store-and-forward model. You have already seen that your incoming mail is stored in a file in /var/mail until you read it. Outgoing mail is also stored until a receiving server connection is available. You use the `mailq` command to see what mail is queued.

Obviously in a health system mailq should be always empty.

.

.

.

<https://en.wikipedia.org/wiki/Message_transfer_agent>

<https://developer.ibm.com/tutorials/l-lpic1-108-3/>

<https://jadi.gitbooks.io/lpic1/content/1083_mail_transfer_agent_mta_basics.html>

<http://linuxconsultant.info/tutorials/linux-mail-server-software.html>

<https://hoststud.com/resources/comparison-between-mtas-postfix-vs-exim-vs-sendmail.158/>

with the special thanks of shawn powers.

Copy

# 108.4. Manage printers and printing

**Weight:** 2

**Description:** Candidates should be able to manage print queues and user print jobs using CUPS and the LPD compatibility interface.

**Key Knowledge Areas:**

* Basic CUPS configuration (for local and remote printers)
* Manage user print queues
* Troubleshoot general printing problems
* Add and remove jobs from configured printer queues

**Terms and Utilities:**

* CUPS configuration files, tools and utilities
* /etc/cups/
* lpd legacy interface (lpr, lprm, lpq)

Although much of our communication today is electronic and paperless, we still have considerable need to print material from our computers.

### cups

CUPS is the standards-based, open source printing system developed by Apple Inc. for macOS® and other UNIX®-like operating systems.It stands for Common UNIX Printing System. The CUPS system can act as a printer server for a local machine or a network of machines.

CUPS consists of:

* Print spooler/scheduler: Lines up printing jobs to be sent to the printer.
* Filter system: Converts data so that the attached printer can understand and format the data being printed.
* Backend system: Transports data from filters to printer.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0SfZO1LI2iM_6n3XLv%252F-M0SiR3QhivescBbWTrZ%252Fmanageprinters-cupsdiagram.jpg%3Falt%3Dmedia%26token%3D54222e72-c2a9-4f59-b7f9-8f8ec24267bb&width=768&dpr=4&quality=100&sign=d3ace837&sv=2)

> At the heart of the CUPS printing system is the `cupsd` print server which runs as a daemon process.

#### cups web interface

There are different interfaces for cups like gui , web interfaces and even traditional command line interfaces. Here we show the CUPS web administration tool (`http://localhost:631 or http://127.0.0.1:631`) to search for or add printers.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0SfZO1LI2iM_6n3XLv%252F-M0Sok4pZYACIeQjVndC%252Fmanageprinters-cupsweb.jpg%3Falt%3Dmedia%26token%3D08b8e960-dd36-4ea6-ba36-23fe8987b4b6&width=768&dpr=4&quality=100&sign=3bf75bad&sv=2)

> If you are asked for a username and password when accessing the CUPS web interface (localhost:631), use your login name and password.
>
> Obviously adding printer requires root access.(in ubuntu members of cups admin group are accepted too)

We need to know what driver to use for your printer. Not all printers are fully supported on Linux and some may not work at all, or only with limitations. Check the printer manufacturer’s website or take a look at OpenPrinting.org.

### /etc/cups

The /etc/cups directory contains other configuration files related to CUPS (Fedora 30).

The CUPS configuration file is normally located in /etc/cups/cupsd.conf

> note1:The default CUPS configuration limits administration to the local machine.
>
> note2: Most of the settings are accessible from the web interface and it is not recommended to edit this file.

If any printer has been configured, the setting are stored in etc/cups/printers.conf

> `DO NOT EDIT THIS FILE WHEN CUPSD IS RUNNING!`

### lpd legacy interface

In UNIX and Linux systems, printing initially used the Berkeley Software Distribution (BSD) printing subsystem, consisting of a line printer daemon (lpd) running as a server, and client commands such as lpr to submit jobs for printing.

Nowadays many of these legacy tools still exist to keep backward compatibility.

command

usage

lpr

send file to printer

lpq

show print jobs

lprm

remove print jobs

lpc status

show printer status

**lpq : q** stands for **queue** and it is use full when we want to see printer jobs

* `-P` : show the jobs of specific printer
* `-a` : show jobs of all printers.

> There should be no space between -P and Printer's name! `-Pprintername`

**lpr :**  The simplest way to print any file is to use the `lpr` command and provide the file name. Again use `-P` to specify printer:

**lprm :** lprm removes job(s) from the printer's queue. We need to define Job ID for this command, if no Job ID is specified the older job is removed.

> again -P can be used to specify the printer. Also we can use `lprm -Pprintername -` to remove all printer's jobs. And `lprm -` will remove all jobs from the default printer.
>
> Each user can remove his/her own jobs, but root can do any thing!

**lpc** : we can use lpc status command in order to check the printer health and troubleshoot (become root for better results!).

where

* **queuing is enabled**: it means that printer will accept new jobs, if it was disabled it won't accept any new job even if the printer was ok.
* **printing is disabled**: means that printer can not actually print on the paper. That happens if the printer is out of ink or paper or experiencing a paper jam.

In my case, my printer is out of paper. But there are some other cups command which might be helpful specially when a problem occurs:

command

describe

**cupsaccept**

tells the printer queue to accept new jobs

**cupsreject**

tells the printer to reject any new job

**cupsenable**

enables the actual/physical printing of the jobs

**cupsdisable**

disables the physical printing of the jobs

with all commands we can specify printer's name without -P switch !

Adding some papers :

And if we want to disable a printer intentionally, we can mention the reason with -r switch:

that's all!

.

.

.

<https://developer.ibm.com/tutorials/l-lpic1-108-4/>

<https://wiki.archlinux.org/index.php/CUPS>

<https://www.linux.com/tutorials/linux-101-printing/>

<https://jadi.gitbooks.io/lpic1/content/1084_manage_printers_and_printing.html>

[https://www.cups.org/](https://www.cups.org/faq.html)

.

Copy

# 109.1. Fundamentals of internet protocols

## **109.1 Fundamentals of internet protocols**

**Weight:** 4

**Description:** Candidates should demonstrate a proper understanding of TCP/IP network fundamentals.

**Key Knowledge Areas:**

* Demonstrate an understanding of network masks and CIDR notation
* Knowledge of the differences between private and public “dotted quad” IP addresses
* Knowledge about common TCP and UDP ports and services (20, 21, 22, 23, 25, 53, 80, 110, 123, 139, 143, 161, 162, 389, 443, 465, 514, 636, 993, 995)
* Knowledge about the differences and major features of UDP, TCP and ICMP
* Knowledge of the major differences between IPv4 and IPv6
* Knowledge of the basic features of IPv6

**Terms and Utilities:**

* /etc/services
* IPv4, IPv6
* Subnetting
* TCP, UDP, ICMP

#### IP

The IP (Internet Protocol) is the fundamental protocol for communications on the Internet. It specifies the way information is packetized, addressed, transferred, routed, and received by networked devices.

#### IP Address

An **IP address** is a number identifying of a computer or another device on the Internet. It is similar to a mailing address, which identifies where postal mail comes from and where it should be delivered. IP addresses uniquely identify the source and destination of data transmitted with the Internet Protocol.

### IPv4

IPv4 addresses are 32 bits long (four bytes). An example of an IPv4 address is 216.58.216.164, which is the front page of Google.com.

**IP v4 address breakdown**

The address is made up of 32 binary bits.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0WcEP_VlRb1LT60koq%252F-M0Wvvp4o4dNbRb3twR4%252Ffundamentalip-ipv4oct.jpg%3Falt%3Dmedia%26token%3D28d711fb-d1d2-450d-ad2e-f19b8feeefe2&width=300&dpr=4&quality=100&sign=ead6c4e5&sv=2)

The 32 binary bits are broken into four octets (1 octet = 8 bits). Each octet is converted to decimal and separated by a period (dot). For this reason, an IP address is said to be expressed in dotted decimal format.

**Here is how binary octets convert to decimal:** The right most bit, or least significant bit, of an octet holds a value of 2^0. The bit just to the left of that holds a value of 2^1. This continues until the left-most bit, or most significant bit, which holds a value of 2^7. So if all binary bits are a one, the decimal equivalent would be 255 as shown here:

Here is a sample octet conversion when not all of the bits are set to 1.

And this sample shows an IP address represented in both binary and decimal.

The maximum value of a 32-bit number is 232, or 4,294,967,296. So the maximum number of IPv4 addresses, which is called its address space, is about 4.3 billion. In the 1980s, this was sufficient to address every networked device, but scientists knew that this space would quickly become exhausted.

> Technologies such as NAT have delayed the problem by allowing many devices to use a single IP address, but a larger address space is needed to serve the modern Internet.

### IPv6

A major advantage of IPv6 is that it uses 128 bits of data to store an address, permitting 2128 unique addresses, or 340,282,366,920,938,463,463,374,607,431,768,211,456. The size of IPv6's address space — 340 duodecillion — is much, much larger than IPv4.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0gBuR5XUU3QZYq79CA%252F-M0gFlmJynNjHA7RDTMq%252Ffundamentalip-ipv6oct.jpg%3Falt%3Dmedia%26token%3D98829be1-abcd-4eeb-9394-946a667a9d23&width=768&dpr=4&quality=100&sign=3e5e5345&sv=2)

#### IP address classes

With an IPv4 IP address, there are five classes of available IP ranges: Class A, Class B, Class C, Class D and Class E, while only A, B, and C are commonly used.

#### subnetmask

Within an Internet Protocol or IP network, every connected host must have both an IP host address and a subnet mask to operate properly. Any device using the IP protocol can refer to itself with the IP address 127.0.0.1 and subnet mask 255.0.0.0, but to communicate with other devices on the network, each device must have a (private or public) IP address and subnet mask.

netmask is a 32-bit binary which bounds that IP class to have prefixed number of Networks and prefixed number of Hosts per network.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0gG2J0ln5Hjm90msjF%252F-M0gI0Bm4NMqWjzHWXqY%252Ffundamentalip-ipv4format.jpg%3Falt%3Dmedia%26token%3Da1dc4973-0be3-4aed-858b-d6b62162709d&width=768&dpr=4&quality=100&sign=51a8f413&sv=2)

* Netid: The part of an IP address that identifies the network.
* Hostid: The part of an IP address that identifies a host in a network.

The netid and hostid are of varying lengths, depending on the class of the address.

Each IP class is equipped with its own default subnet mask (netmask) and allows for a range of valid IP addresses, shown in the following table:

Class

Address range

subnetmask

Supports

**Class A**

1.0.0.1 to 126.255.255.254

255.0.0.0

Supports 16 million hosts on each of 127 networks.

**Class B**

128.1.0.1 to 191.255.255.254

255.255.0.0

Supports 65,000 hosts on each of 16,000 networks.

**Class C**

192.0.1.1 to 223.255.254.254

255.255.255.0

Supports 254 hosts on each of 2 million networks.

**Class D**

224.0.0.0 to 239.255.255.255

N/A

Reserved for multicast groups.

**Class E**

240.0.0.0 to 254.255.255.254

N/A

Reserved for future use, or research and development purposes.

> Ranges 127.x.x.x are reserved for the loopback or localhost, for example, **127.0.0.1** is the loopback address. Range **255.255.255.255** broadcasts to all hosts on the local network.

**Private IPs**

The Internet Assigned Numbers Authority (IANA) has assigned several address ranges to be used by private networks.

Address ranges to be use by private networks are:

* Class A: `10.0.0.0` to `10.255.255.255`
* Class B: `172.16.0.0` to `172.31.255.255`
* Class C: `192.168.0.0` to `192.168.255.255`

Any private network that needs to use IP addresses internally can use any address within these ranges without any coordination. Addresses within this private address space are only unique within a given private network.

Classful IP addressing does not provide any flexibility of having less number of Hosts per Network or more Networks per IP Class, where subnetting comes to play.

### subnetting

The process of deviding an IP Class into smaller blocks, or groups of IPs, known as subnetting.

Subnetting can improve security and help to balance overall network traffic.

**CIDR**

CIDR or **Classless Inter Domain Routing** is based on subnetting concept.CIDR and subnetting are virtually the same thing. The term Subnetting is generally used when you use it at the organizational level. CIDR is generally used when you it at the ISP level or higher.

**How subnetting works ?**subnetting is a bitwise operation on a network of ip addresses which take place using netmask (subnetmask).

it provides the flexibility of borrowing bits of Host part of the IP address and using them as Network in Network, called Subnet. By using subnetting, one single Class A IP address can be used to have smaller sub-networks which provides better network management capabilities.

* **Class A Subnets**

  In Class A, only the first octet is used as Network identifier and rest of three octets are used to be assigned to Hosts (i.e. 16777214 Hosts per Network). To make more subnet in Class A, bits from Host part are borrowed and the subnet mask is changed accordingly.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0XTHYACUjUQc3ABXCq%252F-M0XVR6yb8j8uraleJGX%252Ffundamentalip-classasub.jpg%3Falt%3Dmedia%26token%3D4c5c9ce3-2d29-459c-88ed-7c260f9794f8&width=768&dpr=4&quality=100&sign=a5af19&sv=2)

* **Class B Subnets**

  By default, using Classful Networking, 14 bits are used as Network bits providing (2^14) 16384 Networks and ((2^16)-2) 65534 Hosts. Class B IP Addresses can be subnetted the same way as Class A addresses, by borrowing bits from Host bits. Below is given all possible combination of Class B subnetting.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0XTHYACUjUQc3ABXCq%252F-M0XVn0yLIcWlpsk7AjT%252Ffundamentalip-classbsub.jpg%3Falt%3Dmedia%26token%3Df04ea442-4149-4800-ab36-a1a6189f8169&width=768&dpr=4&quality=100&sign=38976c6d&sv=2)

* **Class C Subnets**

  Class C IP addresses are normally assigned to a very small size network because it can only have 254 hosts in a network. Given below is a list of all possible combination of subnetted Class B IP address

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0XTHYACUjUQc3ABXCq%252F-M0XVsJsWaHIViclxLmy%252Ffundamentalip-classcsub.jpg%3Falt%3Dmedia%26token%3D1de199d5-c9a9-43a0-a047-344f23966d65&width=768&dpr=4&quality=100&sign=833e6946&sv=2)

## Communication Protocols

A network protocol defines the rules and procedures in which data communication occurs between devices over a network. Without predefined rules or procedures, the messages traversing a network would be without any particular formatting and may not be meaningful to the receipt device.

**OSI model :**OSI (Open Systems Interconnection) model was created by the International Organization for Standardization (ISO), an international standard-setting body. It was designed to be a reference model for describing the functions of a communication system. The OSI model has seven layers.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0fPT_09sZcjPpmtE5b%252F-M0fbLg2eVZoXV8zFAQ1%252Ffundamentalip-osi.jpg%3Falt%3Dmedia%26token%3Df6eead97-f260-44d6-8697-1796c0768054&width=300&dpr=4&quality=100&sign=6e742c98&sv=2)

**TCP/IP model :**The TCP/IP model was created in the 1970s by the Defense Advance Research Project Agency (DARPA) as an open, vendor-neutral, public networking model. Just like the OSI model, it describes general guidelines for designing and implementing computer protocols. It consists of four layers.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0fPT_09sZcjPpmtE5b%252F-M0fbQzJrSXgLh_cTgnM%252Ffundamentalip-tcp.jpg%3Falt%3Dmedia%26token%3D32449cdc-389b-4763-8edb-bbc7ab569002&width=300&dpr=4&quality=100&sign=41af2fc8&sv=2)

comparison between the TCP/IP model and OSI model:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0fPT_09sZcjPpmtE5b%252F-M0fbm2X0bpDmx2NyRas%252Ffundamentalip-ositcp.jpg%3Falt%3Dmedia%26token%3De8b71fac-d0ca-4681-829a-0053f0a095cf&width=300&dpr=4&quality=100&sign=e335346f&sv=2)

let’s discuss some of the popular protocols (ITCP/UDP/ICMP) and their respective port numbers :

### TCP

Transmission Control Protocol (TCP) is a **connection-oriented** protocol which operates are the Transport Layer of both the (OSI) reference model and the (TCP/IP) protocol stack. It is designed to provide reliable transportation of the datagrams over a network. It provides reassurance by initializing a 3-way handshake before communicating data between the sender the receiver.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0fgkyRCLTUT0zNA_KW%252F-M0fogdC_iePQ__IoSwU%252Ffundamentalip-howtcp.gif%3Falt%3Dmedia%26token%3D55387b56-3c3c-4147-ab97-98f80d8cd7d1&width=768&dpr=4&quality=100&sign=e7f37306&sv=2)

### UPD

User Datagram Protocol (UDP), is a connectionless protocol. This protocol also operates at the Transport Layer of both the (OSI) reference model and the (TCP/IP) protocol stack. However, unlike Transmission Control Protocol (TCP), the User Datagram Protocol (UDP) does not provide any guarantee or reassurance of the delivery of datagrams across a network. Not all protocols at the Application Layer uses TCP, there are many Layer 7 protocols which uses the User Datagram Protocol (UDP).

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0fgkyRCLTUT0zNA_KW%252F-M0foq5225gG-JcziMjR%252Ffundamentalip-howudp.gif%3Falt%3Dmedia%26token%3Dfadca491-6c21-459f-b86c-2d1897f28287&width=768&dpr=4&quality=100&sign=8d8b71f0&sv=2)

#### Comparison of TCP and UDP

tcp

UDP

Reliable

Very fast in delivery of data

Uses Acknowledgments to confirm receipt of data

Very low overhead on the network

Re-sends data of any of the packets are lost during transmission

Does not require any acknowledgment packets

Delivers the data in sequential order and handles reassembly

If packets are lost during transmission, it does not resend any lost data

Applications: HTTP, FTP, SMTP, Telnet.

Applications: DHCP, DNS, SNMP, TFTP, VoIP, IPTV.

### ICMP

On a network, whether on a Local Area Network (LAN) or a Wide Area Network (WAN), host devices will be communicating to exchange data and information between each other and sometimes an error can occur.

Internet Control Message Protocol (ICMP) is typically used to provide error reporting on a network. There are many types of Internet Control Message Protocol (ICMP) messages which provide different actions and give feedback if an error occurs, and also the issue which exists. A good example of using ICMP Protocol is ping command:

#### Ports

As we said on a TCP/IP network every device must have an IP address.The IP address identifies the device e.g. computer. However an IP address alone is not sufficient for running network applications, as a computer can run multiple applications and/or services.

Just as the IP address identifies the computer, The network port identifies the application or service running on the computer. The use of ports allow computers/devices to run multiple services/applications.

The diagram below shows a computer to computer connection and identifies the IP addresses and ports:

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0fqzS78nV8c-4w3ErZ%252F-M0ftbWk7VUpXx-rML4A%252Ffundamentalip-tcpipsock.jpg%3Falt%3Dmedia%26token%3D0d3d69d7-5b5c-47e5-8435-86d0fbb41566&width=768&dpr=4&quality=100&sign=3a7bf521&sv=2)

The default port of some protocols are as follow. These are very important and most admins know them:

port

usage

20,21

FTP (One data, one control)

22

ssh

23

telnet

25

SMTP

53

DNS

80

HTTP

110

POP3

123

ntp

139

NetBIOS

143

IMAP

161,162

SNMP

389

ldap

443

https

465

SMTPS

636

ldaps

993

IMAPS

995

POP3S

> all ports above 400 ends with S, which stands for Secure

### /etc/services

The /etc/services file contains information regarding the known services available in the Internet. For each service, a single line should be present with the following information:

`official_service_name port_number/protocol_name aliases`

and so on .... .

.

.

.

<https://www.computerhope.com/jargon/i/ip.htm>

<https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html>

<https://itstillworks.com/calculate-host-id-7542379.html>

<https://www.computerhope.com/jargon/n/netmask.htm>

<http://compunetworx.blogspot.com/2013/01/difference-between-hostid-and-netid-in.html>

<https://www.computerhope.com/jargon/s/subnetma.htm>

<https://www.ibm.com/support/knowledgecenter/en/SSSHRK_4.2.0/disco/concept/dsc_private_addr_ranges.html>

<https://en.wikipedia.org/wiki/IPv6_address#/media/File:Ipv6_address_leading_zeros.svg>

<https://www.tutorialspoint.com/ipv4/ipv4_subnetting.htm>

<http://www.itgeared.com/articles/1347-cidr-and-subnetting-tutorial/>

<http://www.steves-internet-guide.com/tcpip-ports-sockets/>

<https://hub.packtpub.com/understanding-network-port-numbers-tcp-udp-and-icmp-on-an-operating-system/>

<https://study-ccna.com/osi-tcp-ip-models/>

<https://www.inetdaemon.com/tutorials/internet/tcp/3-way_handshake.shtml>

<https://nordvpn.com/blog/tcp-or-udp-which-is-better/>

<http://www.qnx.com/developers/docs/6.5.0/index.jsp?topic=%2Fcom.qnx.doc.neutrino_utilities%2Fs%2Fservices.html>

Cisco got you here? <https://www.pcwdld.com/cisco-commands-cheat-sheet>

.

Copy

# 109.2. Basic network configuration

**Weight:** 4

**Description:** Candidates should be able to view, change and verify configuration settings on client hosts.

**Key Knowledge Areas:**

* Manually and automatically configure network interfaces
* Basic TCP/IP host configuration
* Setting a default route

**Terms and Utilities:**

* /etc/hostname
* /etc/hosts
* /etc/nsswitch.conf
* ifconfig
* ifup
* ifdown
* ip
* route
* ping

In this tutorial, we learn hat make network configurations persistent in linux.

### ifconfig

**ifconfig** ( **interface configuration)** utility is used to configure, or view the configuration of, a network interface via command line interface(CentOS6).

The “**ifconfig**” command with no option, displays current network configuration information:

> the lo is the loopback adapter , with ip address 127.0.0.1 which is used by operating system for its own internal communications.

ifconfig option

description

-a

display all the interfaces available, even if they are down.

-s

display a short list (like netstat -i)

-v

be more verbose for some error conditions

We can use ifconfig to change network configurations, but this will require root access:

ifconfig command

description

ifconfig eth0 172.16.43.155

Assign a IP Address

ifconfig eth0 netmask 255.255.255.224

Assign a Netmask

ifconfig eth0 172.16.43.155 netmask 255.255.255.224

Assign a IP, Netmask

ifconfig can be used to turn an interface up and down ,again this will need root access:

* ifconfig *interface* up: used to activate the driver for the given interface
* ifconfig *interface* down: used to deactivate the driver for the given interface

If you're still using ifconfig, you're living in the past! ifconfig command is deprecated and replaced by ip command.

### ifup , ifdown

Same as previous commands, ifup and ifdown are used to enable and disable an interface.

### gateway

One benefit of chopping ip addresses into classes and subnets is controlling broad casts.This happens using subnetmask. But what is two compuyers from two different networks wants to communicate with each other?

A **gateway** is a node or a router that acts as an access point to passes network data from local networks to remote networks.

the address which is used as a gateway to reach to other networks outside our local network is called **default gateway**. There are different ways to set gateway.

### Network Configuration files

The bad news is that all configurations that we have done using ifconfig command are not persistent and got vanished whe system restarts ot the interface turns up and down. So we should find out a way to make our setting persistent and the only way we can achieve that by using network configuration files.

Unfortunately the network configuration files in linux are placed in different places and it depend on the distribution which we are talking about.

#### RedHat Based systems

In Redhat , CentOS, and fedora the files are located at `/etc/sysconfig/network-scripts/` .

and the default gateway is configured via file: `/etc/sysconfig/network`

lets take a look at eth0 configuration file:

#### Debian Based Systems

In debian based systems line Ubuntu , ... the main network configuration file location is `/etc/network/interfaces` and there is no separated file for gateway configuration :

there might be `/etc/network/interfaces.d` directory for configuration files.

> ifdown and ifup commands use this configuration file.

#### DNS configuration file

### /etc/resolv.conf:

As you have noticed DNS configuration is in the same file that interface configuration is located but there is another place in linux which contains DNS information `/etc/resolv.conf` :

Again setting in this file are not permanent and it is not recommended to change this file by hand , except for temporary tests.

### hostname

**Hostname** is the program that is used to either set or display the current host, domain or node name of the system (we are usiong centOS).

The new hostname will appear if you open a new terminal but get vanished if you restart the system. To configure hostname permanently there are a couple of other places which should be changed

1. `/etc/hostname` (Ubuntu) OR `/etc/sysconfig/network` (CentOS)
2. `/etc/hosts` (both Ubuntu , CentOS)

### /etc/hostname

/etc/hostname contains name of the machine and is one of the configuration files that should be modified in order to make a new hostname persistent in Debian based systems.(ubuntu16 here)

### /etc/sysconfig/network

Another place which contains hostname and should be changed in RedHat based systems to have persistent hostname(CentOS6)

### /etc/hosts

The **/etc/hosts** is an operating system file that translate hostnames or domain names to IP addresses , it do the same thing that DNS do. We can using for testing purposes or when DNS server is absent. Do not forget that it has a highr priority than DNS, (means that operating system first look inside /etc/hosts file to gain the ip address of a host, if it wasn't successful then it would query DNS Server).

For making new hostname permanent it is another file which should be modified.

### route

All network devices, whether they are hosts, routers, or other types of network nodes such as network attached printers, need to make decisions about where to route TCP/IP data packets. The routing table provides the configuration information required to make those decisions. the **route** command is used to view and make changes to the kernel routing table.

route command make temporary setting, use config files instead!

Running **route** command without any options displays the routing table entries:

> This shows us how the system is currently configured. If a packet comes into the system and has a destination in the range **172.16.43.0** through **172.16.43.255**, then it is forwarded to the gateway **\***, which is **0.0.0.0** — a special address which represents an invalid or non-existant destination. So, in this case, our system will not route these packets.
>
> If the destination is not in this IP address range, it is forwarded to the default gateway (in this case, **172.16.43.2**, and that system will determine how to forward the traffic on to the next step towards its destination.

By default route command displays the host name in its output. We can request it to display the numerical IP address using `-n` option:

The following route add command will set the default gateway as 172.16.43.2:

use route del for deleting:

> Kernel maintains the routing cache information to route the packets faster. We can list the kernel’s routing cache information by using the -C flag.

> `netstat -rn` also shows routing table.

### ip

This command replaces old good and now deprecated ifconfig command, however, **ifconfig**  command is still works and available for most of the Linux distributions.

It can be used to assign and remove addresses , bring interfaces up or down, manipulate routing, and many more things.

ip command example

description

ip address show

show all IP addresses associated on all network devices

ip address show eth0

view the information of any particular interface

ip addr add 192.168.50.5/24 dev eth0

Assign a IP Address to Specific Interface

ip addr del 192.168.50.5/24 dev eth0

Remove an IP Address

ip link show

Display Network Interface(s)

ip link set eth0 up

Enable Network Interface

ip link set eth0 down

Disable Network Interface

ip route show

Show routing table information

ip route add 10.10.20.0/24 via 192.168.50.100 dev eth0

Add static route

ip route del 10.10.20.0/24

Remove static route

> All the above settings will be lost after a system restart. use config files instead.

### ping

The `ping` command is one of the most used utilities for troubleshooting, testing, and diagnosing network connectivity issues.

Ping works by sending one or more ICMP (Internet Control Message Protocol) Echo Request packages to a specified destination IP on the network and waits for a reply. When the destination receives the package, it will respond back with an ICMP echo reply.

With the `ping` command, we can determine whether a remote destination IP is active or inactive. You can also find the round-trip delay in communicating with the destination and check whether there is a packet loss.

ping command switch

description

**-n**

Numeric output only.do not try to resolve hostname

**-i interval**

Wait interval seconds between sending each packet

**-I interface**

Set source address to specified interface address

**-a**

Audible ping

> for ipv6 environment use ping6 command.

### /etc/nsswitch

This file determines where the system finds things like host names, passwords, and protocol numbers:

Here’s a snippet from a sample /etc/nsswitch.conf file

In this example, user information (the passwd and group services) come first from “files” (like /etc/passwd or /etc/group), and if no entries are found there, a query to an NIS server (configured elsewhere) will be used.

Host information first comes from /etc/hosts (files), then a DNS server (dns), and if neither of those work, at least a fallback of “myhostname” so that the local machine has *some* name.

> The non-complexity comes in the “and if that doesn’t work” rule. When multiple services are listed, they’re tried in order, and a sevice either succeeds or fails. If it fails, the next is tried, etc.

that's all.

.

.

.

### Consistent network device naming

Red Hat Enterprise Linux provides methods for consistent and predictable network device naming for network interfaces. These features change the name of network interfaces on a system in order to make locating and differentiating the interfaces easier.

Traditionally, network interfaces in Linux are enumerated as `eth[0123…]`, but these names do not necessarily correspond to actual labels on the chassis. Modern server platforms with multiple network adapters can encounter non-deterministic and counter-intuitive naming of these interfaces. This affects both network adapters embedded on the motherboard (*Lan-on-Motherboard*, or *LOM*) and add-in (single and multiport) adapters.

In Red Hat Enterprise Linux, **udev** supports a number of different naming schemes. The default is to assign fixed names based on firmware, topology, and location information. This has the advantage that the names are fully automatic, fully predictable, that they stay fixed even if hardware is added or removed (no re-enumeration takes place), and that broken hardware can be replaced seamlessly. The disadvantage is that they are sometimes harder to read than the eth0 or wlan0 names traditionally used. For example: enp5s0.

* for disabling that (how ever it is not recommanded Add both `net.ifnames=0` and `biosdevname=0` as kernel parameter values to the `GRUB_CMDLINE_LINUX` variable )

.

.

<https://developer.ibm.com/tutorials/l-lpic1-109-2/>

<https://www.computerhope.com/unix/uifconfi.htm>

<https://www.tecmint.com/ifconfig-command-examples/>

<https://www.geeksforgeeks.org/ifconfig-command-in-linux-with-examples/>

<https://www.unixmen.com/how-to-find-default-gateway-in-linux/>

<https://jadi.gitbooks.io/lpic1/content/1092_basic_network_configuration.html>

<https://www.tecmint.com/setup-local-dns-using-etc-hosts-file-in-linux/>

<https://opensource.com/business/16/8/introduction-linux-network-routing>

<https://www.computerhope.com/unix/route.htm>

<https://www.thegeekstuff.com/2012/04/route-examples/>

<https://linuxize.com/post/linux-ip-command/>

<https://www.geeksforgeeks.org/ip-command-in-linux-with-examples/>

<https://www.tecmint.com/ip-command-examples/>

<https://linuxize.com/post/linux-ping-command/>

<https://linux.die.net/man/8/ping>

<https://developers.redhat.com/blog/2018/11/26/etc-nsswitch-conf-non-complexity/>

.

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/ch-consistent_network_device_naming>

.

Copy

# 109.3. Basic network troubleshooting

**Weight:** 4

Description: Candidates should be able to troubleshoot networking issues on client hosts.

**Key Knowledge Areas:**

* Manually and automatically configure network interfaces and routing tables to include adding, starting, stopping, restarting, deleting or reconfiguring network interfaces
* Change, view, or configure the routing table and correct an improperly set default route manually
* Debug problems associated with the network configuration

**Terms and Utilities:**

* ifconfig
* ip
* ifup
* ifdown
* route
* host
* hostname
* dig
* netstat
* ping
* ping6
* traceroute
* traceroute6
* tracepath
* tracepath6
* netcat

Till now we have learned about fundamentals of internet protocols and we have get familiar with some of network configuration files and utilities. The truth is that some times things doesn't work as we expected and need troubleshooting. In this section we try to show some steps to resolve the problem, additionally some new commands will be introduced.

### ifconfig & ip (interface or ip address problems)

The first command we have learned is ifconfig . Some times there might be an inactive interface which doesn't appear in results:

use -a with ifconfig or ip command instead:

Bring up the interface with `ifup ens33` or `ifconfig ens33` up , and next check for your ip address.

> You can check your ip address either from GUI or trough config files.If you are on Automatic ip assignment use `dhclient -r` and `dhclient` to release and renew your ip address.

### ping (detecting the problem)

ping is our best friend when we are troubleshooting network problems.

Check whether you can ping another computer in the same network?

from a simple ping command we can determine whether the target is up and running or not. Also there might be a firewall in your network, which filters out ICMP packets, check for host firewall first and then hardware firewall if there are any.

Some times you might ping a wrong ip address or the server might have two interfaces or two ip adresses.

### ping6

Regular ping command only works with IPv4 address. Use ping6 command to send ICMPv6 ECHO\_REQUEST packets to network hosts from a host or gateway.

### route (gateway and routing problems)

If you cant reach any network except computers you are in the same subnet with, you should doubt about you gateway.

we can also use netstat -rn command to see current gateway:

If there were no default gate way, you should use `route add default gw x.x.x.x` to add a default gateway. Next check the gate way, and make sure packets are going out from the right interface:

Every thing seems okey, but you cant reach specific ip address in another building. Hmm there might be routing problems in physical routers! how to check that?

### traceroute

The traceroute command maps the journey that a packet of information undertakes from its source to its destination. This tool uses **ICMP** messages, but unlike *ping*, identifies every router in the path. **traceroute** is useful when troubleshooting network problems because it can help you to localize problems in network connectivity (you might need to install it `apt install traceroute`):

> use -i to Specifies the interface through which traceroute should send packets.

### traceroute6

traceroute with option `-6` supports ipv6, instead we can use traceroute6 command.

What is MTU ? , the maximum transmission unit is the size of the largest protocol data unit that can be communicated in a single network layer transaction.

### tracepath

Tracepath traces a path to a designated network address, reporting on the "time to live" or TTL lag and maximum transmission units (MTU) along the way. This command can be run by any user other with access to the command line prompt.

> Traceroute is essentially the same as Tracepath except that by default, it will only give the TTL value.

### tracepath6

**tracepath6** is good replacement for **traceroute6.**

### dig

**Dig** stands for (**Domain Information Groper**) is a network administration command-line tool for querying **Domain Name System** (**DNS**) name servers. It is useful for verifying and troubleshooting **DNS** problems and also to perform **DNS** lookups and displays the answers that are returned from the name server that were queried.

> By default, dig sends the DNS query to name servers listed in the resolver(/etc/resolv.conf) unless it is asked to query a specific name server.

The dig command output has several sections sections , to have just Answer section use +short switch :

to query specific Name server use `@NameServerIP` :

### netstat

**netstat** (network statistics) is a command-line tool that displays network connections (both incoming and outgoing), routing tables, number of network interface and even network protocol statistics.

> By default, netstat displays a list of open sockets .( A socket is one end-point of a two-way communication link between two programs running on the network.) as an example X11:

So we usually use a combination of switches with netstat :

netstat command example

usage

netstat -a

Listing all the LISTENING Ports of TCP and UDP connections

netstat -na

all LISTENING ports, but shows numerical addresses

netstat -at

Listing TCP Ports connections

netstat -au

Listing UDP Ports connections

netstat -l

Listing all LISTENING(TCP&UDP) Connections

netstat -s

Showing Statistics by Protocol(TCP&UDP&...)

netstat -tp

Displaying Service name with PID

netstat -rn

Displaying Kernel IP routing

> use netstat in conjunction with grep to get a better results.

### netcat

The `nc` (or netcat) utility is used for just about anything under the sun involving TCP or UDP. It can open TCP connections, send UDP packets, listen on arbitrary TCP and UDP ports, do port scanning, and deal with both IPv4 and IPv6. Unlike telnet, nc scripts nicely, and separates error messages onto standard error instead of sending them to standard output, as telnet does with some.

The -l parameter means that netcat is in listen (server) mode, and 8888 is the port it listens to; netcat will create a socket server and wait for connections on port 8888 . The terminal will remain on hold for a client to connect to the open server with netcat. We can verify that a host service listens on port 8888.We need to open a new terminal to the host station and run the command:

.

.

.

<https://www.cyberciti.biz/faq/howto-test-ipv6-network-with-ping6-command/>

<https://www.lifewire.com/traceroute-linux-command-4092586>

<https://geek-university.com/linux/traceroute-command/>

<https://www.techwalla.com/articles/differences-between-traceroute-tracepath>

<http://netstat.net/>

<http://journals.ecs.soton.ac.uk/java/tutorial/networking/sockets/definition.html>

<https://www.geeksforgeeks.org/netstat-command-linux/>

<https://www.tecmint.com/20-netstat-commands-for-linux-network-management/>

<https://linux.die.net/man/1/nc>

<https://www.mvps.net/docs/what-is-netcat-and-how-to-use-it/>

.

Copy

# 109.4. Configure client side DNS

**Weight**: 2

**Description:** Candidates should be able to configure DNS on a client host.

**Key Knowledge Areas:**

* Query remote DNS servers
* Configure local name resolution and use remote DNS servers
* Modify the order in which name resolution is done

**Terms and Utilities:**

* /etc/hosts
* /etc/resolv.conf
* /etc/nsswitch.conf
* host
* dig
* getent

We have seen all of these topics in previous lessons, so in this lesson first we take a quick look at them and then we will talk about steps of Name Resolution on client side.

#### DNS

The DNS (Domain Name System) resolves the names of internet sites with their underlying IP addresses .

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M0zyus5hkAs8d4u9Us8%252F-M10vxahyDk9rCu97XMl%252Fclientdns-howdns.jpg%3Falt%3Dmedia%26token%3Df2000063-1fb7-49a4-8922-902870ab0a03&width=768&dpr=4&quality=100&sign=3052724c&sv=2)

#### Query remote DNS servers

### dig

Dig (Domain Information Groper) is a powerful command-line tool for querying DNS name servers. It is the most commonly used tool among system administrators for troubleshooting DNS problems because of its flexibility and ease of use.

In its simplest form, when used to query a single host (domain) without any additional options, the `dig` command is pretty verbose.

> don't forget, by default, dig sends the DNS query to name servers listed in the resolver(/etc/resolv.conf), how ever, we can query different DNS server usnig @.

### host

the host command is a DNS lookup utility, finding the IP address of a domain name. It also performs reverse lookups, finding the domain name associated with an IP address.

And vica-versa To find out the hostname of the host with the IP address**:**

> If no arguments or options are given, *host* prints a short summary of its command line arguments and options:

#### Client Name Resolution

When client wants to access any other computers in the network, first it needs to know about target ip address. There are different places inside os which keeps information, lets review them togther :

### /etc/host

If we don’t want to use a DNS server for name resolution, we can use the **/etc/hosts** file for the purpose of name resolution. This is a simple text file that contains IP addresses to hostnames mappings. Each line consists of an IP address, followed by one or more hostnames(ubuntu16):

you can see the typical default content of the **hosts** file that contains entries for the loopback addresses. To set up our own mappings, add the entries in the form of `IP_ADDRESS HOSTNAME` :

The line `172.217.164.238 thisismyexample.com` will map the IP address of **172.217.164.238** to the **thisismyexample.com** hostname . We can now use the **thisismyexample** hostname to communicate with the remote machine:

### /etc/resolv.conf

/etc/resolv.conf contain information about current system DNS server. Altough we can manually modify it but don't forget our settings would not be permanent in last until next reboot.

### /etc/nsswitch

The /etc/nsswitch.conf file defines the order in which to contact different name services. For Internet use, it is important that *dns* shows up in the "hosts" line:

The hosts line specifies the order in which various name resolution services will be tried. The default is to:

* `files` reads `/etc/hosts`
* `mdns4_minimal` resolves IPv4 addresses with multicast DNS ONLY if the requested hostname ends with `.local`.
* `[NOTFOUND=return]` stops the resolving process if that `.local` hostname was not found
* `dns` probably does DNS resolution

> you can change the the order of name resolution here.

### getent

As we said **getent** is a Linux command that helps the user to get the entries in a number of important text files called databases. This includes the *passwd* and *the group* of databases which stores the user information. The fact is that The **getent** command displays entries from databases supported by the Name Service Switch libraries, which are configured in /etc/nsswitch.conf.

.

.

.

<https://www.networkworld.com/article/3268449/what-is-dns-and-how-does-it-work.html>

<https://computer.howstuffworks.com/dns3.htm>

<https://linuxize.com/post/how-to-use-dig-command-to-query-dns-in-linux/>

<https://www.computerhope.com/unix/host.htm>

<https://www.geeksforgeeks.org/host-command-in-linux-with-examples/>

<https://geek-university.com/linux/etc-hosts-file/>

<https://www.shellhacks.com/setup-dns-resolution-resolvconf-example/><https://www.linuxtopia.org/online_books/introduction_to_linux/linux__etc_nsswitch.conf.html><https://www.reddit.com/r/linuxquestions/comments/co02ui/hosts_and_mdns_configuration_in_etcnsswitchconf/>

<https://ubuntuforums.org/showthread.php?t=971693>

<https://www.geeksforgeeks.org/getent-command-in-linux-with-examples/>

<https://linux.die.net/man/1/getent>

.

Copy

# 110.1. Perform security administration tasks

## **110.1 Perform security administration tasks**

**Weight:** 3

**Description:** Candidates should know how to review system configuration to ensure host security in accordance with local security policies.

**Key Knowledge Areas:**

* Audit a system to find files with the suid/sgid bit set
* Set or change user passwords and password aging information
* Being able to use nmap and netstat to discover open ports on a system
* Set up limits on user logins, processes and memory usage
* Determine which users have logged in to the system or are currently logged in
* Basic sudo configuration and usage

**Terms and Utilities:**

* find
* passwd
* fuser
* lsof
* nmap
* chage
* netstat
* sudo
* /etc/sudoers
* su
* usermod
* ulimit
* who, w, last

In this lesson we just take a look at basic security audits. First we review several commands we have learned from the security perspective and then get introduced to some other new commands.

## find suid/guid

We have learned about suid/guid when we talked about managing file permissions and owner ship, as a quick review see table bellow:

access mode

**on file**

**on directory**

**SUID**

executes with permissions of file owner

nothing

**GUID**

executes with the permissions of group

new files have group membership of directory

**Sticky Bit**

nothing

only owner can delete files

There are some security concerns while using suid/guid such as, what will happen if a destructive program has suid/guid permission set on it? Why should dangerous programs such as rm has suid permission? To search for all suid/guid files we use find command:

> sudo find / -perm -u+s
>
> sudo find / -perm -g+s

obviously going to each of these files and finding out what they do is beyond the scope of this course, but we should keep our eyes open to find if any of these don't make sense, like thing might be find in home directory of users. It is recommended to save this list for future comparing and detecting new changes.

## looking for open ports

It is important to verify which ports are listening on the server’s network interfaces. Below are the different categories of ports:

1. **0-1023** – the Well Known Ports, also referred to as System Ports.
2. **1024-49151** – the Registered Ports, also known as User Ports.
3. **49152-65535** – the Dynamic Ports, also referred to as the Private Ports.

We need to pay attention to open ports to detect an intrusion. Apart from an intrusion, for troubleshooting purposes, it may be necessary to check if a port is already in use by a different application on our servers. For example, we may install Apache and Nginx server on the same system!

This section provides steps to use the netstat, lsof and nmap command to check the ports in use and view the application that is utilizing the port.

### netstat

One of **netstat** command line tool usage is for monitoring network incoming and outgoing connections. By default, netstat displays a list of open sockets which is not very usefull so we usually use it along with `-tuna` switches.

netstat switch

usage

-t

show tcp ports

-u

show udp ports

-n

Show numerical addresses instead of trying to determine symbolic host, port or user names

-a

Show both listening and non-listening (for TCP this means established connections)

Before a TCP connection can be opened, we need to have a **server** with a listener. The listener will listen on incoming connections on a specific port, This state is represented as `LISTEN`. If everything worked properly, the connection is marked as `ESTABLISHED` on both end-point. In these tables `0.0.0.0` dictates *any address* or *any interface*.

### lsof

**lsof** meaning **‘LiSt Open Files’** is used to find out which files are open by which process. As we know, in Linux everything is a file, so we can even check the files that are opened by some network connections in the system using lsof command with -i switch, -i list all network connections:

this command shows the command, PID, user running it and source and destination IP and tells of if this is a LISTENING or STABLISHED connection.

lsof switch

usage

-iTCP *or* -iUDP

just show TCP or UDP Connections

-i 4 *or* -i 6

you can have IPv4 and IPv6 files displayed separately

-n

Do not use DNS name

-P

do not convert port numbers to port names

If we want to check which process is using specific port , we can grep the output of any above commands or simply use the `fuser` command.

### fuser

The fuser command is a very smart utility used to find which process is using a file, a directory or a socket.

The following command creates a tcp listener on port 8080:

Since a tcp server is listening on port 8080, the fuser utility can be used to find the process which is using the server’s socket. The `-v` option is used to put the fuser utility in verbose mode and the `-n` option is used to select the tcp protocol as a name space:

By default, the fuser tool will look in both IPv6 and IPv4 sockets, but the default option can be changed with the -4 and -6 options.

### nmap

The **Nmap** aka **Network Mapper** is an open source and a very versatile tool for Linux system/network administrators. **Nmap** is used for **exploring networks**, **perform security scans**, **network audit** and **finding open ports** on local or remote machine.

Please note that scanning websites from Nmap is not legal, in some cases if you are trying to too much in deep then you will need written permissions from the owner of the website and the IP holder.

By **default**, **Nmap** scans the most common 1,000 ports for each protocol.

nmap Target selection

Description

nmap 192.168.10.151

scan a single IP

nmap scanme.nmap.org

scan a host

nmap 192.168.10.150-155

scan a range of IPs

nmap 192.168.10.0/24

scan a subnet

nmap -iL myserverlist.txt

scan targets from a text file

nmap -6 [IP-V6-HERE]

enables IP v6 scanning

nmap has lots of switches to gain more information about hosts.

nmap switch

usage

-v

gives more detailed information

-p

scan for information regarding a specific port

-A

discover the operating system information

-O

reveal further operating system information

## examine sudo configuration

#### su vs sudo

sudo and su, the very important and mostly used commands in Linux. It is very important for a Linux user to understand these two to increase security and prevent unexpected things that a user may have to go through. Firstly we will see what these commands do then we’ll know the difference between both of them. So let’s get started.

before beginning, in some distributions like ubuntu the default root password is not set by default when you install a fresh os, so set it using`sudo passwd root`command first.

### su

The Linux command ‘su’ is used to switch from one account to another. User will be prompted for the password of the user switching to.

Users can also use su to switch to root account. If user types only ‘su’ without any option then It will be considered as root and user will be prompted to enter root user password.

**what's the difference between 'su' and 'su -' ?**

Well, difference is environment variables. su - change environment, su don't. the su keeps the environment of the old/original user even after the switch to root has been made, while the su - creates a new environment (as dictated by the ~/.bashrc of the root user), similar to the case when you explicitly log in as root user from the log-in screen.

plaese note that `-, -l, --login`switches are all the same.

### sudo

As we all know, Linux in many ways protects users’ computer being used for bad purposes by some nasty people around us. Using sudo is one of those good ways. Whenever a user tries to install, remove and change any piece of software, the user has to have the root privileges to perform such tasks. sudo, linux command is used to give such permissions to any particular command that a user wants to execute. sudo requires the user to enter user password to give system based permissions. For example user wants to update the operating system by passing command:

This error is due to not having root privileges to the user ‘payam’. The root privileges can be required by passing sudo at the very beginning, like below:

### /etc/sudoers

but how sudo knows who should has root permission? which command could be run under root privilages? sudo keeps its configurations in /etc/sudoers file:

The syntax specification for a rule in the `sudoers` file is:

> user (host)=(user:group) commands

the 3 important lines:

* (root ALL=(ALL) ALL) just lets root do everything on any machine as any user.
* (%admin ALL=(ALL) ALL) lets anybody in the admin group run anything as any user.
* %sudo ALL=(ALL:ALL) ALL all users in the sudo group have the privileges to run any command

> note: In CentOS, the ***wheel*** **group** is often found instead of ***sudo*** **group**.

#### The difference between *wheel/sudo* group and *sudo* user

In CentOS and Debian, a user belonging to the *wheel /sudo* group can execute ***su*** and directly ascend to *root*. Meanwhile, a *sudo* user would have use the *sudo su* first. Essentially, there is no real difference except for the syntax used to ***become root***, and users belonging to both groups can use the *sudo* command.

**How to edit** `/etc/sudors` **file ?** If you use a plain editor, mess up the syntax, and save... `sudo` will (probably) stop working, and, since `/etc/sudoers` is only modifiable by `root`, you're stuck! so we use **visudo** instead. **visudo** edits the `sudoers` file in a safe fashion, by doing two things:

* **visudo** checks the file syntax *before* actually overwriting the `sudoers` file.
* Additionally, **visudo** locks the`sudoers` file against multiple simultaneous edits. This locking is important if you need to ensure nobody else can mess up your carefully considered config changes.

## Managing system resources

Linux operating systems have the ability to limit the amount of various system resources available to a user process. These limitations include how many files a process can have open, how large of a file the user can create, and how much memory can be used by the different components of the process. **ulimit** is the command used to accomplish this.

### ulimit

The ulimit command provides control over the resources available to the shell and/or to processes started by it.

To get the report in details, add the “-a” flag at the end. This will print all the resource limits for the current user.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M30tWLV6EmKc5685RJj%252F-M31_3oCHKhML8NU_T-4%252Fperformsecadmin-ulimit.jpg%3Falt%3Dmedia%26token%3Df2001874-3cda-4944-8280-e3823259c882&width=768&dpr=4&quality=100&sign=ebdf3c83&sv=2)

To set ulimit value on a parameter use the below command:

`ulimit -`

as an example lets put limits on file size in the current shell:

For the ulimits to persists across reboots we need to set the ulimit values in the configuration file **/etc/security/limits.conf**. it is also used for system wide limits:

There are two types of limits: A **soft limit** is like a warning and **hard limit** is a real max limit. For example, following will prevent anyone in the faculty group from having more than 50 processes, and a warning will be given at 20 processes.

note: soft limit cannot be higher than the hard limit.

> ulimits is a part of pluggable authentication module(PAM) system which will be discussed in lpic-2 book.

## checking the users in the system

As a system administrator, you may want to know who is on the system at any give point in time. You may also want to know what they are doing. In this article let us review 3 different methods to identify who is on your Linux system.

### w

**w** command in Linux is used to show who is logged on and what they are doing. This command shows the information about the users currently on the machine and their processes.

The output of the w command contains the following columns:

1. The header shows, in this order, the current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes.
2. The following entries are displayed for each user:

* `Name of the user`
* `User’s machine number or tty number`
* `Remote machine address`
* `User’s Login time`
* `Idle time (not usable time)`
* `Time used by all processes attached to the tty (JCPU time)`
* `Time used by the current process (PCPU time)`
* `Command currently getting executed by the users`

`w` has some options, try `w --help` to see them.

### who

The who command is used to get information about currently logged in user on to system.

The who command displays the following information for each user currently logged in to the system if no option is provided :

1. `Login name of the users`
2. `Terminal line numbers`
3. `Login time of the users in to system`
4. `Remote host name of the user`

who has lots of option try `who --help`.

w and who reads their information from /var/run/utmp file. This file contains information about the users who are currently logged onto the system.

so we need another command to get information about logged out people, and that is `last` .

### last

The **last** command in Linux is used to display the list of all the users **logged in and out**.

The output of this command contains the following columns:

1. `User name`
2. `Tty device number`
3. `Login date and time`
4. `Logout time`
5. `Total working time`

the last command uses /var/log/wtmp file to display listing of last logged in users. This file is like history for utmp file, i.e. it maintains the logs of all logged in and logged out users (in the past).

/var/log/btmp keeps track of failed login attempts. So try `last -f /var/log/btmp` to check last failed logins .

`last` also gives us information about latest system reboots, do not forget to take a look at `last --help`.

.

.

.

<https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/>

<https://www.tecmint.com/find-open-ports-in-linux/>

<https://blog.confirm.ch/tcp-connection-states/> (tcp 3-way handshake)

<https://jadi.gitbooks.io/lpic1/content/1101_perform_security_administration_tasks.html>

<https://www.geeksforgeeks.org/lsof-command-in-linux-with-examples/>

<https://www.cyberciti.biz/faq/how-to-check-open-ports-in-linux-using-the-cli/>

<https://linux.die.net/man/8/lsof>

<https://www.digitalocean.com/community/tutorials/how-to-use-the-linux-fuser-command>

<https://www.tecmint.com/nmap-command-examples/>

<https://www.tecmint.com/nmap-command-examples/>

<https://phoenixnap.com/kb/nmap-command-linux-examples>

<https://www.linux.com/training-tutorials/how-use-sudo-and-su-commands-linux-introduction/>

<https://superuser.com/questions/580568/any-differences-between-su-vs-su-beside-the-pathing>

<https://www.howtoforge.com/tutorial/sudo-vs-su/>

<https://help.ubuntu.com/community/Sudoers>

<https://www.hostinger.com/tutorials/sudo-and-the-sudoers-file/>

<https://support.hostway.com/hc/en-us/articles/115001509750-How-To-Install-and-Configure-Sudo>

<https://unix.stackexchange.com/questions/27594/why-do-we-need-to-use-visudo-instead-of-directly-modifying-the-sudoers-file>

<https://www.computerhope.com/unix/visudo.htm>

<https://www.thegeekdiary.com/understanding-etc-security-limits-conf-file-to-set-ulimit/>

<http://geekswing.com/geek/quickie-tutorial-ulimit-soft-limits-hard-limits-soft-stack-hard-stack/>

<https://gerardnico.com/os/linux/limits.conf>

<https://www.thegeekstuff.com/2009/03/4-ways-to-identify-who-is-logged-in-on-your-linux-system/>

<https://www.geeksforgeeks.org/w-command-in-linux-with-examples/>

<https://www.geeksforgeeks.org/who-command-in-linux/>

<https://www.geeksforgeeks.org/last-command-in-linux-with-examples/>

.

Copy

# 110.2. Setup host security

**Weight:** 3

**Description:** Candidates should know how to set up a basic level of host security.

**Key Knowledge Areas:**

* Awareness of shadow passwords and how they work
* Turn off network services not in use
* Understand the role of TCP wrappers

**Terms and Utilities:**

* /etc/nologin
* /etc/passwd
* /etc/shadow
* /etc/xinetd.d/
* /etc/xinetd.conf
* /etc/inetd.d/
* /etc/inetd.conf
* /etc/inittab
* /etc/init.d/
* /etc/hosts.allow
* /etc/hosts.deny

We have previously talked about /etc/passwd , /etc/nologin and /etc/shadow. So lets review them quickly:

### /etc/passwd

**/etc/passwd** file stores essential information, which required during login. In other words, it stores user account information. The /etc/passwd is a plain text file.

Each line in /etc/passwd file represents an individual user account and contains following seven fields separated by colons (**:**)

1. Username or login name
2. Encrypted password
3. User ID
4. Group ID
5. User description
6. User’s home directory
7. User’s login shell

The /etc/passwd file should have general read permission as many command utilities use it to map user IDs to user names. However, write access to the /etc/passwd must only limit for the superuser/root account.

as we said, in old days /etc/passwd was a place that all users information even the user's password, and it caused security issues . To solve the problem /etc/shadow was invented. An x character indicates that encrypted password is stored in /etc/shadow file.

### /etc/shadow

The /etc/shadow file contains encrypted passwords, along with password- and account-expiration information.

Each line in **/etc/shadow** file represents an individual user account and contains following nine fields separated by colons (**:**)

1. Username
2. Encrypted password
3. Date of last password change
4. Minimum required days between password changes
5. Maximum allowed days between password changes
6. Number of days in advance to display password expiration message
7. Number of days after password expiration to disable the account
8. Account expiration date
9. Reserve field

Unlike **/etc/passwd** file, the **/etc/shadow** file is not world readable. It is readable only by the root user or super user.

### /etc/nologin

If the file /etc/nologin exists and is readable, login will allow access only to root. Other users will be shown the contents of this file and their logins will be refused. Delete this file and the users will be able to login again.

> /etc/nologin removed during reboot by shutdown script.

### turn off network services

As an system administrator it is our task to find unnecessary running services and disable them in order to minimize security risks. Previously we learned different linux distributions use different initialization solutions when system boots up, so use appropriate commands based on your service manager for disabling services:

Linux Distro

service manager

command

older linux systems (pre 2006)

SysV

**chkconfig** *ServiceName* **off**
**sysv-rc-conf** *ServiceName* **off**

Ubuntu(2006-2019),CentOS(2011-2020)

Upstart

**update-rc.d** *ServiceName* **remove**

ubuntu(2015-????),CentOS(2014-????)

systemd

**systemctl disable** *ServiceName*

Please note that these commands prevent the service from starting on system boot. But the package is still installed on the machine and we can run it if we need.

### super servers

In most other Unix systems, networking services are implemented as daemons. Each networking daemon responds to requests on a particular port. The Telnet service, for example, operates on port 23. For networking services to function properly, some process must be alive and listening on each corresponding port. There are two ways to offer TCP/IP services:

* by running server applications standalone as a daemon
* or by using the Internet **super server**

This **super-server** is a special daemon that listens to the ports of all the enabled networking services. When a request comes in from a particular port, the corresponding networking daemon is started, and the request is passed on to it for service.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3B2G8hHP2iOKY0VvNI%252F-M3BzB2syPqQcYq_RWMf%252Fsecurehost-superserver.jpg%3Falt%3Dmedia%26token%3D723902ab-8d7b-42b6-9a54-f9e0fbdae62c&width=768&dpr=4&quality=100&sign=579dc923&sv=2)

There are two main benefits to this scheme. First, only the minimal set of needed daemons is active at all times, and therefore, no system resources are wasted. Second, there is a centralized mechanism for managing and monitoring network services.

The Disadvantages of Super Server is that Starting of the super server is time consuming, which increases the reaction time according to the availability of network service.

super servers are not being used anymore and most distributions use standalone services running on them.

### inetd , xinetd

There are two main internet super-servers available for Linux, inetd and xinetd. Though inetd used to be the standard super-server for most Linux distributions, it is gradually being replaced by xinetd, which contains more features. But because inetd contains fewer features than xinetd, it is also smaller and may be better for an embedded Linux system.

#### inetd configuration files

### /etc/inetd.conf

The **/etc/inetd.conf** file is the default configuration file for the inetd daemon. This file enables you to specify the daemons to start by default and supply the arguments that correspond to the desired style of functioning for each daemon. Let's have a look at an example line from inetd.conf:

### /etc/inetd.d/

/etc/inet.d directory contains the configuration files for each service managed by `inetd` and the names of the files correlate to the service.

#### xinetd configuration files

### /etc/xinetd.conf

The `/etc/xinetd.conf` file contains general configuration settings which effect every service under `xinetd`'s control. It is read once when the `xinetd` service is started, so for configuration changes to take effect, the administrator must restart the `xinetd` service. The following is a sample `/etc/xinetd.conf` file:

### /etc/xinetd.d/

The `/etc/xinetd.d/` directory contains the configuration files for each service managed by `xinetd` and the names of the files correlate to the service. As with `xinetd.conf`, this directory is read only when the `xinetd` service is started. To gain an understanding of how these files are structured, consider the `/etc/xinetd.d/telnet` file:

For any changes to take effect, the administrator must restart the `xinetd` service.

`/etc/services` file contains list of network services and ports mapped to them. `inetd` or `xinetd` looks at these details so that it can call particular program when packet hits respective port and demand for service.

### tcp wrappers

As you can see in /etc/inetd.conf connections for most protocols are made through **tcpd**, instead of directly passing the connection to a service program. For example:

In this example ftp connections are passed through **tcpd**. **tcpd** logs the connection through syslog and allows for additional checks. One of the most used features of **tcpd** is host-based access control. A TCP Wrapper is a host-based networking access control list (ACL) system and used to filter network access to Internet.

### /etc/host.allow , /etc/host.deny

When a network request reaches your server, TCP wrappers uses `hosts.allow` and `hosts.deny` (in that order) to determine if the client should be allowed to use a given service.

By default, these files are empty, all commented out, or do not exist. Thus, everything is allowed through the TCP wrappers layer and your system is left to rely on the firewall for full protection.

Both files have one rule on each line of the following form:`service: hosts`

Hosts can be specified by hostname or IP address. The ALL keyword specifies all hosts or all services.

For example, adding  `telnet 192.168.` to `/etc/hosts.allow` causes only telnet connections from 192.168.x.x ip range accepted.

Adding the same line to `/etc/hosts.deny` causes telnet connections from 192.168.x.x ip range denied , but telnet connetions would be accepted from any other addresses.

> after changing these files, xinetd should be restarted

that's all.

.

.

.

.

<https://www.cyberciti.biz/faq/understanding-etcpasswd-file-format/>

<https://www.computernetworkingnotes.com/rhce-study-guide/etc-passwd-file-in-linux-explained-with-examples.html>

<https://www.cyberciti.biz/faq/understanding-etcshadow-file/>

<https://www.computernetworkingnotes.com/rhce-study-guide/etc-shadow-file-in-linux-explained-with-examples.html>

<https://linux.die.net/man/5/nologin>

<https://jadi.gitbooks.io/lpic1/content/1102_setup_host_security.html>

<http://etutorials.org/Linux+systems/embedded+linux+systems/Chapter+10.+Setting+Up+Networking+Services/10.1+The+Internet+Super-Server/>

<https://en.wikipedia.org/wiki/Super-server>

<https://thecustomizewindows.com/2011/11/super-server-what-is-it-how-it-works/>

<https://www.ibm.com/support/knowledgecenter/ssw_aix_72/filesreference/inetd.conf.html>

<https://book.huihoo.com/slackware-linux-basics/html/inetd.html>

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/reference_guide/s1-tcpwrappers-xinetd-config>

<https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/reference_guide/s2-tcpwrappers-xinetd-config-files>

<https://kerneltalks.com/linux/understanding-etc-services-file-in-linux/>

<https://www.tecmint.com/secure-linux-tcp-wrappers-hosts-allow-deny-restrict-access/>

.

Copy

# 110.3. Securing data with encryption

**Weight:** 3

**Description:** The candidate should be able to use public key techniques to secure data and communication.

**Key Knowledge Areas:**

* Perform basic OpenSSH 2 client configuration and usage
* Understand the role of OpenSSH 2 server host keys
* Perform basic GnuPG configuration, usage and revocation
* Understand SSH port tunnels (including X11 tunnels)

**Terms and Utilities:**

* ssh
* ssh-keygen
* ssh-agent
* ssh-add
* ~/.ssh/id\_rsa and id\_rsa.pub
* ~/.ssh/id\_dsa and id\_dsa.pub
* /etc/ssh/ssh\_host\_rsa\_key and ssh\_host\_rsa\_key.pub
* /etc/ssh/ssh\_host\_dsa\_key and ssh\_host\_dsa\_key.pub
* ~/.ssh/authorized\_keys
* ssh\_known\_hosts
* gpg
* ~/.gnupg/

First lets start about some concepts.

## Cryptography

Cryptography is a method of using advanced mathematical principles in storing and transmitting data in a particular form so that only those whom it is intended can read and process it. Encryption is a key concept in cryptography

* **Encryption** :In cryptography, encryption is the process of encoding a message or information in such a way that only authorized parties can access it and those who are not authorized cannot.
* **Decryption**: The conversion of encrypted data into its original form is called Decryption. It is generally a reverse process of encryption.

### Symmetric vs. asymmetric encryption

Encryption algorithms are often divided into two categories, known as symmetric and asymmetric encryption.

#### Symmetric Encryption

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3MvsU-g_yO57PEazbP%252F-M3NCqjPHY7XbzTLz4PX%252Fsecuredata-symetric.jpg%3Falt%3Dmedia%26token%3D6203cabc-5413-4b3f-bd12-19e8bf4c0621&width=768&dpr=4&quality=100&sign=2e8b6efc&sv=2)

Symmetric encryption is the oldest and best-known technique. A secret key, which can be a number, a word, or just a string of random letters, is applied to the text of a message to change the content in a particular way. This might be as simple as shifting each letter by a number of places in the alphabet. As long as both sender and recipient know the secret key, they can encrypt and decrypt all messages that use this key.

#### Asymmetric Encryption

The problem with secret keys is exchanging them over the Internet or a large network while preventing them from falling into the wrong hands. Anyone who knows the secret key can decrypt the message. One answer is asymmetric encryption, in which there are two related keys--a key pair. A public key is made freely available to anyone who might want to send you a message. A second, private key is kept secret, so that only you know it.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3MvsU-g_yO57PEazbP%252F-M3NDYrgJJZ1hp__5u76%252Fsecuredata-asymetric.jpg%3Falt%3Dmedia%26token%3Dd3e7d1d4-c359-481b-a248-e10c525abdb7&width=768&dpr=4&quality=100&sign=3b6c27ac&sv=2)

Any message (text, binary files, or documents) that are encrypted by using the public key can only be decrypted by applying the same algorithm, but by using the matching private key. Any message that is encrypted by using the private key can only be decrypted by using the matching public key.
This means that you do not have to worry about passing public keys over the Internet (the keys are supposed to be public).

> A problem with asymmetric encryption, however, is that it is slower than symmetric encryption. It requires far more processing power to both encrypt and decrypt the content of the message.

**encryption vs signing**

When encrypting, you use **their public key** to write a message and they use **their private key** to read it.

When signing, you use **your private key** to write message's signature, and they use **your public key** to check if it's really yours.

#### Whats is a key server?

Key server (cryptographic), a server on which public keys are stored for others to use

With that introduction lets talk about SSH.

## Whats is SSH?

The SSH protocol (also referred to as Secure Shell) is a method for secure remote login from one computer to another. It provides several alternative options for strong authentication, and it protects the communications security and integrity with strong encryption. It is a secure alternative to the non-protected login protocols (such as telnet, rlogin) and insecure file transfer methods (such as FTP).

Typical uses of the SSH protocol are:

* providing secure access for users and automated processes
* interactive and automated file transfers
* issuing remote commands
* managing network infrastructure and other mission-critical system components.

### How does the ssh protocol work?

The way SSH works is by making use of a client-server model to allow for authentication of two remote systems and encryption of the data that passes between them.

SSH operates on TCP port 22 by default (though this can be changed if needed). The host (server) listens on port 22 (or any other SSH assigned port) for incoming connections.

SSH provides multiple mechanisms for authenticating the server and the client. Two of the commonly used authentication mechanism are password based, and key based authentication. Although password based authentication is also secure, its advisable to use key based authentication instead.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3NDuIrJcPpMPasqI7X%252F-M3NIyfGubwUShl1jMiO%252Fssh-howitworks.jpg%3Falt%3Dmedia%26token%3Df9f9d4b4-3346-4282-b65d-8be8caecd8c9&width=768&dpr=4&quality=100&sign=da5f2540&sv=2)

the connection is established by the SSH client connecting to the SSH server. The SSH client drives the connection setup process and uses public key cryptography to verify the identity of the SSH server. After the setup phase the SSH protocol uses strong symmetric encryption and hashing algorithms to ensure the privacy and integrity of the data that is exchanged between the client and server.

### What is OpenSSH?

OpenSSH is a free, open source implementation of the SSH (Secure Shell) protocols. Open OpenSSH is so popular among system administrators because of its multi-platform capability and very useful nice features.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3NDuIrJcPpMPasqI7X%252F-M3NKaYlvMjlZs3Os5FA%252Fopenssh-logo.png%3Falt%3Dmedia%26token%3D2766a4fa-03b8-4721-ae60-dc4c17293816&width=768&dpr=4&quality=100&sign=5a185ff8&sv=2)

All communications and user credentials using OpenSSH are encrypted, they are also protected from man in the middle attacks. If a third party tries to intercept our connection, OpenSSH detects it and informs us about that.

We use Ubuntu16-1 as ssh server and Ubuntu16-2 as client.

#### /etc/ssh

OpenSSH has two different sets of configuration files: one for client programs (ssh, scp, and sftp) and one for the server daemon (sshd).

The`sshd_config`is the ssh  **daemon**(or ssh server process) configuration file, Whereas, the `ssh_config` file is the ssh client configuration file. The client configuration file only has bearing on when you use the ssh command to connect to another ssh host . As you can see there are public keys and private keys here with different algorithems and they can be used by SSH to encrypt the session.

## ssh client configurations

Till now we have understood how ssh works. As we mentioned when ssh connection is started, the public key of ssh server is tranfered to the client(stored in ./ssh/known\_hosts) and the client will use it to continue negotiation with the server and user will be required to get authenticated by sending username and password.

Lets start by connecting toUbuntu16-1 from Ubuntu16-2 and see the keys:

**What is fingerprint ?** a public key fingerprint is a short sequence of bytes used to identify a longer public key. Fingerprints are created by applying a cryptographic hash function to a public key. Since fingerprints are shorter than the keys they refer to, they can be used to simplify certain key management tasks.

now lets compare the keys in server and client:

### Configuring SSH Key Based authentication

Its possible to omit entring user name and password and get connected to the ssh server using client public and private key.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3PzjTrQVOKE77UYYcy%252F-M3Q59QDJeG-JDRHtanw%252Fssh-keybasedauth.jpg%3Falt%3Dmedia%26token%3D8f4330c9-8cae-4d8f-9410-a62af7d9ae29&width=768&dpr=4&quality=100&sign=91fc89d5&sv=2)

Now lets generate public and private keys for client and copy client public key to the server.

### ssh-keygen

ssh-keygen - creates a key pair for public key authentication:

We haven't set passphrase in our demonstration but if we set we would be asked to enter it when we copy it to the server.

### ssh-copy-id

we use ssh-copy-id - configures a public key as authorized on a server

Now lets take a look the server side:

now lets check the result from the client:

and it seems okey.We can copy and paste the keys for other users if you like, but do not forget that these keys give power to users to login with out the password.

#### Why use passphrase? Why it is for?

We have configured a password less ssh connection using key based authentication. But what would happened if our system compromised? An evil hacker would be able to get connected to other servers using key based authentication without knowning the passwords.

Passphrase can help us to avoid this kinds of security issues by requiring a passphrase at the beginning of every ssh key-based authentication. So let clear previous authorized\_key, and start:

Now generate a new key pairs with passphrase on the client (Let it over write current private and public key):

Now lets tranfer our new public key to the server:

Lets check the key we have copied on the server:

Now when we ssh to the remote server (ubuntu16-1) from our client(ubuntu16-2), we are asked to enter our local key passphrase intead of remote user account password:

lets exit and ssh again and again:

as you can see each time we are asked to enter passphrase and that was what we were seeking for inorder to stop a hacker if our system get compromised. There is way to stick passphrase to the current user session and keept if for next ssh connections inorder to avoid entering passphrase again and again.

### ssh-agent

The **ssh**-**agent** is a helper program that keeps track of user's identity keys and their passphrases. The **agent** can then use the keys to log into other servers without having the user type in a password or passphrase again. This implements a form of single sign-on (SSO). The SSH agent is used for SSH public key authentication.

> if you got an error try ssh-agent /bin/bash first.

### ssh-add

By default, the agent uses SSH keys stored in the `.ssh` directory under the user's home directory. The **ssh-add** command is used for adding identities to the agent. In the simplest form, just run if without argument to add the default files `~/.ssh/id_rsa`, `.ssh/id_dsa`, `~/.ssh/id_ecdsa`, `~/.ssh/id_ed25519`, and `~/.ssh/identity`. Otherwise, give it the name of the private key file to add as an argument.

`-l` will list private keys currently accessible to the agent,

`-D`Deletes all identities from the agent, if you like!

And then we can login to OpenSSH server (ubuntu16-1) without any password or passphrase again and again:

Until we exit from the bash that uses associated key with that, then we would need to enter passphrase again.

#### What is SSH Tunneling ?

SSH tunneling is a method of transporting arbitrary networking data over an encrypted SSH connection. It can be used to add encryption to legacy applications. It can also be used to implement VPNs (Virtual Private Networks) and access intranet services across firewalls.

SSH is a standard for secure remote logins and file transfers over untrusted networks. It also provides a way to secure the data traffic of any given application using port forwarding, basically tunneling any TCP/IP port over SSH. This means that the application data traffic is directed to flow inside an encrypted SSH connection so that it cannot be eavesdropped or intercepted while it is in transit. SSH tunneling enables adding network security to legacy applications that do not natively support encryption.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3R21NVTIOFkHxwf2-n%252F-M3R5j-31MGdsikzhaVn%252Fssh-tunneling.jpg%3Falt%3Dmedia%26token%3D4a051d46-cff4-4c2b-b4c8-a9b95856686a&width=768&dpr=4&quality=100&sign=2aa73257&sv=2)

#### what is ssh port forwarding?

SSH port forwarding is a mechanism in SSH for tunneling application ports from the client machine to the server machine, or vice versa. some system administrators and IT professionals use it for opening backdoors into the internal network from their home machines. It can also be abused by hackers and malware to open access from the Internet to the internal network.

There are three types of SSH port forwarding:

* **Local port forwarding** - connections from an SSH client are forwarded, via the SSH server, to a destination server.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3R21NVTIOFkHxwf2-n%252F-M3RF8CY1r_iQ2NTTl0a%252Fssh-portfwl1.jpg%3Falt%3Dmedia%26token%3Dd94635d2-b146-4c5f-a68c-004debaa8f72&width=768&dpr=4&quality=100&sign=c1549c59&sv=2)

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3R21NVTIOFkHxwf2-n%252F-M3RFDJDPAB5o-demnZw%252Fssh-portfwl2.jpg%3Falt%3Dmedia%26token%3D04ebcdcd-cf3f-431e-b5a4-446747c01438&width=768&dpr=4&quality=100&sign=72db62e7&sv=2)

* **Remote port forwarding** - connections from an SSH server are forwarded, via the SSH client, to a destination server

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3R21NVTIOFkHxwf2-n%252F-M3RG2W_5COqtSWmMvX-%252Fssh-portfwlr1.jpg%3Falt%3Dmedia%26token%3Dde614dc7-bbee-4799-a74d-6631f8e23450&width=768&dpr=4&quality=100&sign=c15d7734&sv=2)

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3R21NVTIOFkHxwf2-n%252F-M3RG72_oD72A_SGJzPV%252Fssh-portfwlr2.jpg%3Falt%3Dmedia%26token%3Dc5cf44c8-5e7f-44dc-9506-650d24639430&width=768&dpr=4&quality=100&sign=823c270a&sv=2)

* **Dynamic port forwarding** - connections from various programs are forwarded, via the SSH client to an SSH server, and finally to several destination servers.

### ssh

Like other command ssh has also some options.Lets take a look at most usefull switches:

SSH commands

Description

ssh -V

Shows ssh client version

ssh user1@server1.example.com

Connect to the remote host, add "-v" for verbose mode

ssh -l login\_name server1.example.com

Specifies the user to log in as on the remote machine.

ssh user1@server1.example.com

Running  on the remote host over ssh

ssh -X user@server1.example.com

Enable Xforwarding on the clients side, X11Forwarding should be enabled on the server side in sshd\_config file.

## data encryption

Encryption **is important** because it allows you to securely protect data that you don't want anyone else to have access to.

### gpg

GnuPG (more commonly known as GPG) is an implementation of a standard known as PGP (Pretty Good Privacy). It uses a system of "public" and "private" keys for the encryption and signing of messages or data.

for demonstration, we use two users on ubuntu16, user1 and user2.

![](https://borosan.gitbook.io/lpic1-exam-guide/~gitbook/image?url=https%3A%2F%2F588171885-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-LqAGY8muYlSuaVSKvqr%252F-M3RGfp8LjTfRBkmRd_S%252F-M3V_KZh07V7RXxR3U3g%252Fsecuredata-gpgencrypt.jpg%3Falt%3Dmedia%26token%3D1053e773-6587-4dea-8c49-4b5e13b6db38&width=768&dpr=4&quality=100&sign=8900428&sv=2)

okey, lets login via user1 and start creating keypairs using `gpg --gen-key` command:

> it create keys inside ~/.gupg directory.

lets see the created key-pair using `gpg --list-key` commmand:

Then we need to share our public key to other people. To export our public key file we need to run:

lets put in /tmp directory for user2:

now login as user2 and import user1 public key via `gpg --import` :

next create a sample file for encrypting:

every thing is ready for encrypting user2 file:

time to send user 2 secret to user1:

Log in as user1 and try to decrypt user2 secret:

lets see what is user2 secret information?

### Generating a Revocation Certificate

If your private key becomes known to others, you will need to disassociate the old keys from your identity, so that you can generate new ones. To do this, you will require a revocation certificate. We’ll do this now and store it somewhere safe.

The `--output` option must be followed by the filename of the certificate you wish to create. The `--gen-revoke` option causes `gpg` to generate a revocation certificate. You must provide the email address that you used when the keys were generated.

## signing

By encrypting a document using your private key, you let everyone to try to open it using your public key and if they succeed, they will be sure that you have signed it using YOUR private key! `gpg` has a specific command to sign documents:

here the --clearsign tells the gpg to include the clear text message in the output file too. The output file will be `originalfile.asc` :

copy notice.asc file to /tmp and other users can verify that a document is singed correctly:

and that's all folks!

## Congratulation we have done lpic1-102 !!! do not forget to give a [star](https://github.com/Borosan) and [donate](http://linuxcert.ir/donation.html) :-)

## You can start studying my LPIC-2 book: <https://borosan.gitbook.io/lpic2-exam-guide/>

.

.

.

<https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences>

<https://hackernoon.com/symmetric-and-asymmetric-encryption-5122f9ec65b1>

<https://economictimes.indiatimes.com/definition/decryption>

<https://support.microsoft.com/en-us/help/246071/description-of-symmetric-and-asymmetric-encryption>

<https://stackoverflow.com/questions/454048/what-is-the-difference-between-encrypting-and-signing-in-asymmetric-encryption>

<https://en.wikipedia.org/wiki/Key_server>

<https://www.ssh.com/ssh/protocol>

<https://www.hivelocity.net/kb/what-is-openssh/>

<https://www.ssh.com/ssh/agent>

<https://www.ssh.com/ssh/tunneling>

<https://www.ssh.com/ssh/tunneling/example>

<https://unix.stackexchange.com/questions/115897/whats-ssh-port-forwarding-and-whats-the-difference-between-ssh-local-and-remot>

<https://www.ssh.com/ssh/command>

<https://www.taoeffect.com/espionage/EspionageHelp/pages/faq-encryption.html>

<https://www.privex.io/articles/what-is-gpg/>

<https://www.howtogeek.com/427982/how-to-encrypt-and-decrypt-files-with-gpg-on-linux/>

<https://jadi.gitbooks.io/lpic1/content/1103_securing_data_with_encryption.html>

.
