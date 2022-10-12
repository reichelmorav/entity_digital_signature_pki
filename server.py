import socket
import os 
import subprocess
from subprocess import Popen, PIPE

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
        
        file = open('csr.csr', 'wb')
        file.write(certificate)
        file.close() 
      
        os.system('echo 1234 | sudo -S openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -batch -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -passin pass:1234 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem')   
       
        connection.close()

if __name__ == "__main__":
    main()