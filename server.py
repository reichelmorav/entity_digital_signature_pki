import datetime, socket, os
from OpenSSL import crypto

PORT = 9225
HOST = ''
HOME = os.getenv("HOME")

def save_csr(csr, entity_name):
    csr_file = open(HOME + '/' + entity_name + '.csr', 'wb')
    csr_file.write(csr)
    csr_file.close()    

def sign_csr(entity_name):
    command = 'echo ecciadm | sudo -S openssl ca -config /etc/pki/ca/issuing_ca/openssl.cnf -batch \
        -engine pkcs11 -keyform engine -keyfile 02 -extensions v3_ca -days 365 -notext -md sha256 -passin pass:2728 \
        -in ' + HOME + '/' + entity_name + '.csr -out /etc/pki/ca/issuing_ca/certs/' + entity_name + '.pem'
    os.system(command) 

def main():      
    sock = socket.socket()      
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(2)       

    while True:                 
        conn, dir = sock.accept()

        entity_csr = conn.recv(4096)
        csr = crypto.load_certificate_request(crypto.FILETYPE_PEM, entity_csr)  
        entity_name = csr.get_subject().commonName.replace(" ", "")       
        save_csr(entity_csr, entity_name)
        sign_csr(entity_name)      

        crt_file = open('/etc/pki/ca/issuing_ca/certs/' + entity_name + '.pem', 'rb')         
        conn.sendall(crt_file.read())      
        crt_file.close()
        
        conn.close()        

if __name__ == "__main__":
    main()