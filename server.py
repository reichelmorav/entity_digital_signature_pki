import datetime, socket, os
from OpenSSL import crypto

PORT = 9225
HOST = ''

def main():  
    sock = socket.socket()      
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(4)       

    while True:                 
        connection, direcction = sock.accept()                     
        entity_csr = connection.recv(2048)
        request = crypto.load_certificate_request(crypto.FILETYPE_PEM, entity_csr)  
        common_name = request.get_subject().commonName      
        
        csr_file = open(common_name + '.csr', 'wb')
        csr_file.write(entity_csr)
        csr_file.close()  
        
        command = 'echo 1234 | sudo -S openssl ca -config /home/reich/root/ca/issuing_ca/openssl.cnf -batch \
        -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -passin pass:1234 \
        -in ' + common_name + '.csr -out /home/reich/root/ca/issuing_ca/certs/' + common_name + '.pem'

        os.system(command) 

        crt_file = open('/home/reich/root/ca/issuing_ca/certs/' + common_name + '.pem', 'rb')         
        connection.sendall(crt_file.read())      
        
        connection.close()        


if __name__ == "__main__":
    main()