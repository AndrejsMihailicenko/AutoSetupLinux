import subprocess

def system_update():
    subprocess.run('sudo dnf update && sudo dnf upgrade', shell=True, check=True)

def apps_installation():
    pass

if __name__ == "__main__":
    system_update()