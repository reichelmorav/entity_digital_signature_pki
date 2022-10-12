import socket
from os import system 
import subprocess

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
        
        foo_proc = subprocess.Popen(['sudo openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        foo_proc.stdin.write(b"1234")


        #subprocess.run([""], capture_output=True, text=True, input="1234")

        #os.system()   

        #os.system("2728")

        connection.close()

if __name__ == "__main__":
    main()