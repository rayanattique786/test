import os
import subprocess
import socket
import time
import urllib.request

# Function to download the TigerVNC installer
def download_tigervnc_installer():
    print("Downloading TigerVNC installer...")
    url = "https://github.com/rayanattique786/test/releases/download/m/tigervnc64-winvnc-1.15.0.exe"
    installer_path = os.path.join(os.getenv('TEMP'), "tigervnc_installer.exe")

    try:
        urllib.request.urlretrieve(url, installer_path)
        print("Download complete.")
    except Exception as e:
        print(f"Error downloading TigerVNC installer: {e}")
        return None

    return installer_path

# Function to install TigerVNC server silently
def install_tigervnc(installer_path):
    print("Installing TigerVNC silently...")
    try:
        # Using silent flags for installation: "/S" (silent) and "/quiet"
        subprocess.run([installer_path, "/S", "/quiet", "/components=server"], check=True)
        print("TigerVNC installation complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")
        return False
    return True

# Function to set the VNC password
def set_vnc_password():
    print("Setting TigerVNC server password...")

    # Path to the TigerVNC server executable (correct for x86 installation)
    vnc_exe = r"C:\Program Files\TigerVNC Server\winvnc4.exe"  # Update path if needed

    if not os.path.exists(vnc_exe):
        print(f"Error: TigerVNC not found at {vnc_exe}")
        return

    # Set VNC password
    password = "password123"  # Change this password if needed
    try:
        # Setting VNC password (this is the server-side configuration)
        subprocess.run(f'"{vnc_exe}" -password {password}', shell=True, check=True)
        print("VNC server password set successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting password: {e}")

# Function to log the IP and Hostname
def log_ip_and_hostname():
    print("Logging IP and Hostname...")
    ip_address = socket.gethostbyname(socket.gethostname())
    hostname = socket.gethostname()

    # Write the IP and Hostname to a file on the Desktop
    desktop_path = os.path.expanduser("~\\Desktop\\networkinfo.txt")
    with open(desktop_path, "w") as file:
        file.write(f"IP Address: {ip_address}\nHostname: {hostname}\n")
    
    print(f"IP and Hostname written to {desktop_path}")

# Main function to orchestrate the process
def main():
    installer_path = download_tigervnc_installer()
    if installer_path and install_tigervnc(installer_path):
        time.sleep(10)  # Wait for the installation to complete
        set_vnc_password()  # Set the VNC server password
        log_ip_and_hostname()  # Log IP and Hostname

if __name__ == "__main__":
    main()
