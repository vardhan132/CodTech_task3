import socket

def port_scanner(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open.")
        s.close()

def brute_force_login(target, port, usernames, passwords):
    print(f"Attempting brute force on {target}:{port}...")
    for username in usernames:
        for password in passwords:
            print(f"Trying {username}:{password}")
