import subprocess
from bs4 import BeautifulSoup
import distro
import sys

def os_detector():
    name = distro.name() 
    if (name == 'Fedora Linux'):
        return 'dnf'
    elif (name == 'Debian GNU/Linux' or name == 'Ubuntu'):
        return 'apt'
    else:
        sys.exit()  
    
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

def get_last_version(package_manager):
    pass 

def apps_installation(package_manager, apps_list):
    for app in apps_list:
        subprocess.run(f'sudo {package_manager} install -y {app}', shell=True, check=True)

if __name__ == "__main__":
    package_manager = os_detector()
    system_update()
    apps_list = read_packages() 
    apps_installation(apps_list) 