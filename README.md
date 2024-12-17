# LAN-Health

This Python program leverages `python-nmap` to scan your network for devices sharing the same IP address, monitors their uptime, and retrieves their MAC addresses. It utilizes the `python-nmap` and `openpyxl` libraries for network scanning and data output, respectively.

## Requirements

Python 3.6 or later (for f-string support)  
python-nmap library: pip install python-nmap  
openpyxl library: pip install openpyxl  

## Installation
Clone this repository: git clone https://github.com/ErikDio/LAN-Health.git  
Install the required libraries: pip install -r requirements.txt (if you have a requirements.txt file) or individually using pip install python-nmap openpyxl  
Usage

(Optional) Run the program with debug as a arg so it can print information useful for troubleshooting.  
Run the program: python network_scanner.py  

The program generates a spreadsheet named plan.xlsx in the same directory, containing the following information:  

Status  
IP Address  
Uptime  
MAC Address (if available)  

This program requires root or administrative privileges to perform ARP scans for MAC addresses.  
Be cautious when scanning networks you don't own or have permission to access. Respect network security policies.  

### Disclaimer

This program is designed for educational purposes only. Use it responsibly and ethically.  

We welcome contributions to this project! Feel free to fork the repository, make changes, and submit pull requests.  
