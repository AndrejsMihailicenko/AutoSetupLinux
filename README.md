# AutoSetupLinux

## What is AutoSetupLinux?
AutoSetupLinux is a simple Python script. It makes setting up your Linux system easy. It automatically installs software and updates your system. I Developed this for my Tehnical University course DIP225.  

## What You Need
- Python 3.
- Python 3 `pip`.
- `bs4` (BeautifulSoup), `distro`, `requests` libraries.
- Internet connection.
- Ability to use sudo commands or have root access.

## How to Set Up and Use
'$ git clone https://github.com/AndrejsMihailicenko/AutoSetupLinux.git'
'$ python3 setup.py'

## How It Works
- **Detects System Type**: The script first finds out what Linux system you're using. At this moment script works with RHEL and Debian based distro.
- **Installs Python Libraries**: It installs any Python libraries listed in `requirements.txt`.
- **Updates System**: The script updates your Linux system.
- **Installs Software**: It installs the software you listed in `packages.csv`.
- **Installs JDK**: Finally, the script downloads and installs the latest Java Development Kit from Oracle's website.