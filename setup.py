import subprocess
from bs4 import BeautifulSoup

def read_packages():
    apps_list = []
    with open("packages.csv", "r") as f:
        next(f)
        for line in f:
            if line:
                apps_list.append(line[0])
    return apps_list
            
def system_update():
    subprocess.run('sudo dnf update -y && sudo dnf upgrade -y', shell=True, check=True)

def get_last_version():
    pass #web scr. to get latest packages

def apps_installation(apps_list):
    for app in apps_list:
        subprocess.run(f'sudo dnf install -y {app}', shell=True, check=True)

if __name__ == "__main__":
    system_update()
    apps_list = read_packages() 
    apps_installation(apps_list) 