import subprocess
import bs4
import distro
import sys
import requests


def os_detector():
    name = distro.name() 
    if (name == 'Fedora Linux'):
        return 'dnf'
    elif (name == 'Debian GNU/Linux' or name == 'Ubuntu'):
        return 'apt'
    else:
        sys.exit('Unsupported operating system')  

def install_libraries(package_manager):
    if (package_manager == 'dnf'):
        subprocess.run('sudo dnf install -y python3-pip', shell=True)
    if (package_manager == 'apt'):
        subprocess.run('sudo apt install -y python3-pip', shell=True)
    subprocess.run('pip install -r requirements.txt', shell=True, check=True)

def read_packages():
    apps_list = []
    with open("packages.csv", "r") as f:
        next(f)
        for line in f:
            if line:
                apps_list.append(line.strip())
    return apps_list
            
def system_update(package_manager):
    subprocess.run(f'sudo {package_manager} update -y && sudo {package_manager} upgrade -y', shell=True, check=True)

def install_jdk(package_manager):
    url = 'https://www.oracle.com/java/technologies/downloads/'
    r = requests.get(url)
    if r.status_code == 200:
        page_content = bs4.BeautifulSoup(r.content, 'html.parser')

        if package_manager == 'dnf':
            download_link = page_content.find('a', href=lambda href: href and "jdk-21_linux-x64_bin.rpm" in href)
            if download_link:
                download_url = download_link['href']
                subprocess.run(f'wget {download_url}', shell=True)
                subprocess.run(f'sudo dnf install -y {download_url.split('/')[-1]}', shell=True)
        elif package_manager == 'apt':
            download_link = page_content.find('a', href=lambda href: href and "jdk-21_linux-x64_bin.deb" in href)
            if download_link:
                download_url = download_link['href']
                subprocess.run(f'wget {download_url}', shell=True)
                subprocess.run(f'sudo dpkg -i {download_url.split('/')[-1]}', shell=True)

def apps_installation(package_manager, apps_list):
    for app in apps_list:
        subprocess.run(f'sudo {package_manager} install -y {app}', shell=True, check=True)

if __name__ == "__main__":
    package_manager = os_detector()
    install_libraries(package_manager)
    system_update(package_manager)
    apps_list = read_packages() 
    apps_installation(apps_list)
    install_jdk(package_manager)