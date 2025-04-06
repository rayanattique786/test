# install_vnc.py

import os
import subprocess
import socket
import time

# Function to install TigerVNC silently
def install_vnc():
    print("Downloading and Installing TigerVNC Server...")
    subprocess.run("bitsadmin /transfer tigervnc https://github.com/TigerVNC/tigervnc/releases/download/v1.13.1/tigervnc-1.13.1.exe %TEMP%\\tigervnc.exe", shell=True)
    subprocess.run("%TEMP%\\tigervnc.exe /silent", shell=True)
    print("VNC Server Installed.")

# Function to set the VNC password
def set_vnc_password():
    password = "secret123"  # You can change this
    print("Setting up VNC password...")
    subprocess.run(f'"C:\\Program Files\\TightVNC\\tvnserver.exe" -password {password}', shell=True)

# Function to log the IP and hostname
def log_ip_and_hostname():
    ip_address = socket.gethostbyname(socket.gethostname())
    hostname = socket.gethostname()
    with open(os.path.expanduser('~') + "\\Desktop\\networkinfo.txt", "w") as f:
        f.write(f"IP Address: {ip_address}\nHostname: {hostname}\n")
    print(f"IP and Hostname saved to Desktop as networkinfo.txt.")

if __name__ == "__main__":
    install_vnc()
    time.sleep(10)  # wait for installation to complete
    set_vnc_password()
    log_ip_and_hostname()