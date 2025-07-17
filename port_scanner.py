import socket
import sys

def scan_ports(host):
    print(f"Resolving host: {host}")
    ip = socket.gethostbyname(host)
    print(f"Scanning {host} ({ip})...\n")

    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <host or domain>")
        sys.exit(1)

    host = sys.argv[1]

    try:
        scan_ports(host)
    except Exception as e:
        print(f"Error: {e}")
