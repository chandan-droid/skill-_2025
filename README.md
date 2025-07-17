# Python Port Scanner Tool

A simple Python script to scan all **TCP ports (1–65535)** on a given host or domain to find open ports.

---

## Features

- Scans full TCP port range (1–65535)
- Accepts IP address or domain name (resolves automatically)
- Adjustable timeout
- CLI-friendly and beginner-readable

---

## Requirements

- Python 3.x
- Network connectivity to the target host

---

## 🧾 Usage

### 1. Clone or copy the script

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

### 2. Create a Test Environment

```bash
python3 -m http.server 2000
```
This starts a web server on port 2000 of your machine (localhost).

### 3. Run the Port Scanner

```bash
python3 port_scanner.py localhost
```
scan any host/IP:
```
python3 port_scanner.py 127.0.0.1
python3 port_scanner.py google.com
```

### 4. Understand the Output
```bash
Resolving host: localhost
Scanning localhost (127.0.0.1)...

Port 2000 is OPEN
```
