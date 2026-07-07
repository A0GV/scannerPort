from socket import socket

def main():
    #Scanner for open ports based in IP
    ip = input("Enter the IP address to scan: ")
    port = int(input("Enter the port number to scan: "))
    print(f"Scanning IP: {ip}")
    print(f"Scanning port {port}...")
    try:
        
        #Cosas a destacar del sock = socket()
        '''
        En este caso, solo puse sock = socket por como puse el import 
        "from socket import socket" ya que aqui lo quye hice no fue importar el modulo, si no la clase en si.
        Si solo hubiera hecho "import socket"  tendria qu3e haber inicialiado y llamar a la clase socket
        
        Otra cosa a destacar, es que este socket() por debajo corre como 'sock = socket(AF_INET, SOCK_STREAM)'
        El primer parametro es que tipo de familia o tipo de IP vas a usar 'socket.AF_INET' es ipv4 y 'socket.AF_INET6' es ipv6
        El segundo parametro es el tipo de comunicacion 'socket.SOCK_STREAM' es el TCP y 'socket.SOCK_DGRAM' es el UDP
        '''
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