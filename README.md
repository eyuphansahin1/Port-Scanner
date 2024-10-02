# Port-Scanner
This Python script scans an IP address for open ports within a specified range. The script uses the socket library to attempt connections to each port and reports back if the port is open and the banner it receives.

#Features 
IP address validation.
Customizable port range (default: 1-1023).
Displays open ports and their banners (if any).

#Requirements
Python 3.x
socket and argparse libraries (built-in in Python).

#Example 
python port_scanner.py -i 192.168.1.1 -p 20-80
