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
        
        #foo_proc = subprocess.Popen(['sudo openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        #foo_proc.stdin.write(b"1234")

        #subprocess.run('sudo openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem', capture_output=True, text=True, input="y")
        #subprocess.run([""], capture_output=True, text=True, input="1234")

        #p = os.popen('sudo openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem')
        #p.write("1234")
        #os.system('echo 1234 | sudo openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem')   
        #os.system("2728")

        p = Popen('sudo openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -in csr.csr -out /home/reich/root/ca/issuing_ca/certs/prueba.pem', shell=True, stdin=PIPE)
        p.communicate(input='1234'.encode())

        connection.close()

if __name__ == "__main__":
    main()