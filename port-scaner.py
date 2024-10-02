import socket
import argparse
import re

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def validate_ip(ip):
    ip_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\."
                            r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$")

    if not ip_pattern.match(ip):
        print("Error: IP address must be in the format x.x.x.x where x is between 0 and 255 (e.g., 192.168.1.10)")
        exit(1)

def validate_ports(port_range):
    try:
        port_min, port_max = map(int, port_range.split('-'))
        return port_min, port_max 
    except ValueError:
        print("Invalid port range! Correct format: min-max (e.g., 1-50)")
        exit(1)


def get_information():
    parser = argparse.ArgumentParser(description="Receive an IP address and port range.")
    parser.add_argument("-i","--ip", type=str, help="IP address")
    parser.add_argument("-p", "--port", type=str, default="1-1023", help="Port range (Default: 1-1023)")
    args = parser.parse_args()

    ip_address = args.ip
    port_range = args.port

    validate_ip(ip_address)

    port_min,port_max = validate_ports(port_range)

    
    return ip_address, port_min, port_max

def getOpenPorts():
    open_ports = []
    for port in range(port_min,(port_max + 1)):
        try:
            client_socket.connect((ip_address,port))
            client_socket.settimeout(1.0)
            response = client_socket.recv(1024).decode()
            open_ports.append({
                "port":port,
                "banner":response
            })
        except Exception as e:
            print(f"{ip_address}:{port} closed")

    return open_ports



ip_address, port_min, port_max = get_information()


print(f"IP Address: {ip_address}")
print(f"Port Range: {port_min}-{port_max}")
open_ports = getOpenPorts()


print(f"open ports {open_ports}")





