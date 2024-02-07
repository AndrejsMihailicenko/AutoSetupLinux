# AutoSetupLinux
*Lasīt latviešu valodā: [Latvian](README.md).*<br>
*Read this in other languages: [Latviešu](README.md).*

## What is AutoSetupLinux?
AutoSetupLinux is a simple Python script. It makes setting up your Linux system easy. It automatically installs software and updates your system. I Developed this for my Tehnical University course DIP225.  

## What You Need
- Python 3.
- Internet connection.
- Ability to use sudo commands or have root access.

## How to Set Up and Use
1. Clone GitHub repository to machine
2. **Run the Script**

```bash
git clone https://github.com/AndrejsMihailicenko/AutoSetupLinux.git
cd AutoSetupLinux/
python3 setup.py
```

## How It Works
- **Detects System Type**: The script first finds out what Linux system you're using. At this moment script works with RHEL and Debian based distro.
- **Updates System**: The script updates your Linux system.
- **Installs Software**: It installs the software you listed in `packages.csv`.
