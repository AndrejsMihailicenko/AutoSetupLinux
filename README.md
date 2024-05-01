# AutoSetupLinux
*Lasīt latviešu valodā:* [Latviešu](README.lv.md)<br>
*Read this in other languages:* [Latvian](README.lv.md)

## Overview
I frequently reinstall my Linux system. To streamline the process, I developed a simple but effective Python script that automatically downloads and installs my essential software. This saves me time and ensures I always have the tools I need after a fresh installation
## Features
OS Detection: The script intelligently detects your Linux distribution to utilize the appropriate package manager.
System Updates: Keeps your system up-to-date with the latest packages and security fixes.
Software Installation: Automates the installation of software listed in the config.json file.
Flatpak Support: Installs Flatpak applications conveniently from Flathub.

## Prerequisites
- Python 3
- An internet connection
- Ability to use sudo commands or root access

## Installation
Clone the repository:

```Bash 
git clone https://github.com/AndrejsMihailicenko/AutoSetupLinux.git
```
Navigate to the directory:
```Bash
cd AutoSetupLinux/
```
Run the script:
```Bash
python3 setup.py
```
Use code with caution.

## Customize config.json:

Set systemUpdates to true or false to control automatic system updates. <br>
Set systemRestart to true or false to determine if a reboot is required after the process. <br>
Modify the packages list to include the software you want to install. <br>
Add Flatpak applications you want to install to the flatpaks list. <br>
Run the script: Follow the instructions in the "Installation" section.
