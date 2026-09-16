import subprocess
import os
import sys
packages = [
    "discord.py-self",
    "requests",
    "pynacl",
    "python-dateutil",
    "instaloader",
    "psutil",
    "pytz",
    "protobuf==3.20.3",
    "pyinstaller",
    "colour"
]
def install_package(package):
    try:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi cài đặt {package}: {str(e)}")


def install_all_packages(packages):
    for package in packages:
        install_package(package)


def run_czic():
    try:
        print("Running..")
        subprocess.check_call(["python", "antigore.py"])
        print("czic.py executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running : {e}")
def main():
    install_all_packages(packages)
    

    run_czic()

if __name__ == "__main__":
    main()
