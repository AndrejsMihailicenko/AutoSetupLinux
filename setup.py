import subprocess
import distro
import sys
import os


def os_detector():
    name = distro.name()
    if name in ['Fedora Linux']:
        return 'dnf'
    elif name in ['Debian GNU/Linux' or name == 'Ubuntu']:
        return 'apt'
    else:
        sys.exit('Unsupported operating system, use Fedora or Ubuntu!')


def system_update(package_manager):
    subprocess.run(['sudo', package_manager, 'update', '-y'])
    subprocess.run(['sudo', package_manager, 'upgrade', '-y'])


def read_packages():
    if os.path.exists("packages.csv"):
        apps_list = []
        with open("packages.csv", "r") as f:
            next(f)
            for line in f:
                if line:
                    apps_list.append(line.strip())

    else:
        sys.exit('Package list file not found!')
    return apps_list


def flatpak_install():
    subprocess.run(['flatpak', 'install', 'flathub',
                   'org.telegram.desktop', '-y'])
    subprocess.run(['flatpak', 'install', 'flathub',
                   'com.mattjakeman.ExtensionManager', '-y'])


def apps_installation(package_manager, apps_list):
    for app in apps_list:
        subprocess.run(['sudo', package_manager, 'install', '-y', app])


if __name__ == "__main__":
    try:
        package_manager = os_detector()
        system_update(package_manager)
        apps_list = read_packages()
        apps_installation(package_manager, apps_list)
        flatpak_install()
        print("Successful! All software installed!")
        # subprocess.run(['sudo', 'reboot'])
    except Exception as e:
        print(f"Something goes wrong {e}")
