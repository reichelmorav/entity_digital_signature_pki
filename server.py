import socket, os

PORT = 8800
HOST = ''

def main():    
    sock = socket.socket()      
    sock .setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(4)   

    while True:
        connection, direction = sock.accept()                     
        certificate = connection.recv(2048)       
        
        file = open('crs.crs', 'wb')
        file.write(certificate)
        file.close()         

        connection.close()

if __name__ == "__main__":
    main()