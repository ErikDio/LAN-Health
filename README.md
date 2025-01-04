# LAN-Health

This Python program uses `python-nmap` to scan your network for devices sharing the same IP address, monitors their uptime, and retrieves their MAC addresses. It utilizes `python-nmap`, `speedtest.cli` and `openpyxl` libraries for network scanning, testing the network speed, and data output.

## Requirements

- Python 3.6 or later (for f-string support)  
- python-nmap library: pip install python-nmap  
- openpyxl library: pip install openpyxl
- speedtest-cli library: pip install speedtest-cli
- [Nmap (tool)](https://nmap.org/download)

## Installation
Clone this repository: git clone https://github.com/ErikDio/LAN-Health.git  
Install the required libraries: pip install -r requirements.txt (if you have a requirements.txt file) or individually using pip install python-nmap openpyxl  
Usage

(Optional) Run the program with `-debug` and/or `-log` as an arg so it can print information useful for troubleshooting.  

## Usage
- Install the dependencies
- Run the program: python scanner/main.py < args >
- Input the IP(default gateway) of the device you want to scan
- Input the scan range
- Input the delay (in minutes) between each scan
- Input the NMAP configuration args (optional)
- The program will scan the network, generates a spreadsheet named scan.xlsx, and after each scan it'll update it, with the following information:  
  - Status sheet: Status, (LAN)IP Address, Uptime, MAC Address
  - Grafico sheet: Various charts related to IP usage conflict and net speed.
  - Dados sheet: Data related to charts

This program requires root or administrative privileges to perform ARP scans for MAC addresses.
Be cautious when scanning networks you don't own or have permission to access. Respect network security policies.

### Disclaimer

This program is designed for educational purposes only. Use it responsibly and ethically.
We welcome contributions to this project! Feel free to fork the repository, make changes, and submit pull requests.
