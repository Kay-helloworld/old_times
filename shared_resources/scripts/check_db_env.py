import socket
import subprocess
import sys

def check_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        try:
            s.connect((host, port))
            return True
        except:
            return False

def check_mysql_command():
    try:
        result = subprocess.run(["mysql", "--version"], capture_output=True, text=True)
        return result.stdout.strip()
    except FileNotFoundError:
        return None

def main():
    print("=== Database Environment Check ===")
    
    # 1. Check Port 3306
    port_open = check_port("127.0.0.1", 3306)
    print(f"Port 3306 (MySQL default): {'OPEN' if port_open else 'CLOSED'}")
    
    if not port_open:
        print("  -> MySQL service might not be running or is running on a different port.")
        print("  -> If you installed MySQL Workbench, it might have stopped the background service.")
    else:
        print("  -> MySQL service appears to be running.")

    # 2. Check mysql command
    mysql_ver = check_mysql_command()
    if mysql_ver:
        print(f"MySQL Client: Found ({mysql_ver})")
    else:
        print("MySQL Client: Not found in PATH (You might need to add it or use full path)")

    print("\n=== Troubleshooting Tips ===")
    print("1. Conflict: If both DBeaver and Workbench try to start a local server, they might conflict.")
    print("2. DBeaver: Usually just a client. It connects to an existing server.")
    print("3. Workbench: Can manage server instances. Check 'Server Status' in Workbench.")
    print("4. Recommendation: Stick to ONE server instance (System Service). Use DBeaver as client.")

if __name__ == "__main__":
    main()
