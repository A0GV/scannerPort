from socket import socket

def main():
    #Scanner for open ports based in IP
    ip = input("Enter the IP address to scan: ")
    port = int(input("Enter the port number to scan: "))
    print(f"Scanning IP: {ip}")
    print(f"Scanning port {port}...")
    try:
        sock = socket()
        sock.connect((ip, port))
        print(f"Port {port} is open")
    except:
        print(f"Port {port} is closed")
    finally:
        sock.close()
    print("Scan complete.")

if __name__ == "__main__":
    main()