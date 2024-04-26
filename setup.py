import subprocess
import os
import json


with open("config.json") as f:
        data = json.load(f)


def os_detector():
    # Check if the OS is supported
    package_managers = {
        '/etc/apt/sources.list': 'apt', # Debian-based
        '/etc/yum.conf': 'yum', # Red Hat-based
        '/etc/dnf/dnf.conf': 'dnf', # Fedora-based
        '/etc/pacman.conf': 'pacman', # Arch-based
        '/etc/zypp/zypp.conf': 'zypper', # OpenSUSE-based
        '/etc/portage/make.conf': 'emerge', # Gentoo-based
        '/etc/apk/repositories': 'apk', # Alpine-based
        '/etc/pkg/pkg.conf': 'pkg' # FreeBSD-based
    }
    # Check if the file exists
    for file_path, pkg_manager in package_managers.items():
        if os.path.exists(file_path):
            return pkg_manager
    return 'unknown'


# Update the system
def system_update(pkg_manager):
    subprocess.run(['sudo', pkg_manager, 'update', '-y'])
    subprocess.run(['sudo', pkg_manager, 'upgrade', '-y'])


# Read the packages from the config file
def read_packages():
    packages = []

    for package in data['packages']:
        packages.append(package)
    return packages


def flatpak_install(): 
    try:
        subprocess.run(['flatpak',' --version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 
        # Check if flatpak is installed
        if True:
            with open("config.json") as f:
                data = json.load(f) 
            for flatpaks in data['flatpaks']:
                subprocess.run(['flatpak', 'install', 'flathub', flatpaks, '-y'])
        else:
            print("Flatpak is not installed")
    except Exception as e:
        print(f"Error: {e}")


def apps_installation(pkg_manager, apps_list):
    for app in apps_list:
        subprocess.run(['sudo', pkg_manager, 'install', '-y', app])


def system_reboot():
    if data['systemRestart'] == 'true':
        subprocess.run(['sudo', 'reboot', 'now'])
    else:
        os.exit(0)


if __name__ == "__main__":
    try:
        pkg_manager = os_detector()
        system_update(pkg_manager)
        apps_list = read_packages()
        apps_installation(pkg_manager, apps_list)
        flatpak_install()
        print("Successful! All software installed!")
        system_reboot()
    except Exception as e:
        print(f"Something goes wrong {e}")
