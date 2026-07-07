from socket import socket, gethostbyname



def scan(target,portInit,portEnd):
    
    ###
        #En este caso, solo puse sock = socket por como puse el import 
        #"from socket import socket" ya que aqui lo quye hice no fue importar el modulo, si no la clase en si.
        #Si solo hubiera hecho "import socket"  tendria qu3e haber inicialiado y llamar a la clase socket
        
        #Otra cosa a destacar, es que este socket() por debajo corre como 'sock = socket(AF_INET, SOCK_STREAM)'
        #El primer parametro es que tipo de familia o tipo de IP vas a usar 'socket.AF_INET' es ipv4 y 'socket.AF_INET6' es ipv6
        #El segundo parametro es el tipo de comunicacion 'socket.SOCK_STREAM' es el TCP y 'socket.SOCK_DGRAM' es el UDP
    ###
    
    for p in range (portInit,portEnd+1):
        sock = socket()
        try:
            print(f"Escanenado el puerto {p}")
            sock.connect((target, p))
            print(f"Port {p} is open")
        except Exception:
            print(f"Port {p} is closed")
        sock.close()
    print("Scan complete.")
def main():
    #Scanner for open ports based in IP
    ip = input("Enter the IP address to scan: ")
    if gethostbyname(ip) != ip:
        print(f"La ip de {ip} es {gethostbyname(ip)}")
        ip=gethostbyname(ip)
    portInit = int(input("Enter the initial port number to scan: "))
    portEnd = int(input("Enter the end port number to scan: "))
    print(f"Scanning IP: {ip}")
    # print(f"Scanning port {port}...")
    scan(ip,portInit, portEnd)
if __name__ == "__main__":
    main()