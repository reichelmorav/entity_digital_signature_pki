from OpenSSL import crypto
from tabulate import tabulate
import os, socket

PORT = 9225
HOST = '172.16.202.27'
TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA
ENTITIES_PATH = '/etc/pki/entities_issued/'

C = "CR"
ST = "San Jose"
L = "San Pedro"
O = "UCR ECCI ITI"
OU = "II 2022"

def generate_key(keypath):
    key = crypto.PKey()
    key.generate_key(TYPE_RSA, 4096)
    key_file = open(keypath, "wb")
    key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    key_file.close()
    return key

def generate_CSR(key, csrpath, entity_name, entity_email):
    req = crypto.X509Req()
    req.get_subject().C = C     
    req.get_subject().ST = ST
    req.get_subject().L = L
    req.get_subject().O = O     
    req.get_subject().OU = OU
    req.get_subject().CN = entity_name.upper()
    req.get_subject().emailAddress = entity_email.upper()    
    req.set_pubkey(key)
    req.sign(key, "sha512")        
   
    ca_file = open(csrpath, 'wb')
    ca_file.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))
    ca_file.close()  

def send_to_sign(csr_path, crt_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))   
        csr_file = open(csr_path, 'rb')
        certificate = csr_file.read() 
        sock.sendall(certificate)    
        csr_file.close()
        crt_file = open(crt_path, 'wb')
        crt_file.write(sock.recv(4096))
        sock.close()        

def create_PKCS12(key_path, crt_path, pfx_path):    
    entity_certificate = crypto.PKCS12()
    key_file = open(key_path,'rt')
    crt_file = open(crt_path,'rt')
    entity_certificate.set_privatekey(crypto.load_privatekey(crypto.FILETYPE_PEM, key_file.read()))
    entity_certificate.set_certificate(crypto.load_certificate(crypto.FILETYPE_PEM, crt_file.read()))
    key_file.close()
    crt_file.close() 
    pfx_file = open(pfx_path,'wb')
    pfx_file.write(entity_certificate.export()) 

def main():       
    while(True):    
        # try:                  
        table = [['BIENVENIDO(A) A LA AUTORIDAD DE REGISTRO DE ENTIDADES DE LA UCR'], ['1. Generar certificado para unidad'], ['2. Salir']]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        option = input("Ingrese el número de la opción deseada: ")
        if(option == "1"):       
            entity_name = input("Ingrese el nombre: ")
            entity_email = input("Ingrese el correo: ")
            entity = entity_name.replace(" ", "")
            entity_path = ENTITIES_PATH + entity
            os.mkdir(entity_path)
            file_path = entity_path + '/' + entity 
            key_path = file_path + '.key'
            csr_path = file_path + '.csr'
            crt_path = file_path + '.pem'
            pfx_path = file_path +  '.pfx'               
            generate_CSR(generate_key(key_path), csr_path, entity_name, entity_email)
            send_to_sign(csr_path, crt_path)
            create_PKCS12(key_path, crt_path, pfx_path)
            print ("El certificado solicitado se encuentra en: " + pfx_path + '\n')                                
        elif(option == "2"):            
            break
        else:
            print("La opción seleccionada no es correcta. Intentelo de nuevo.\n")
        # except BaseException as exception:
        #     print("An exception occurred \n")
        #     print(exception)
        #     break

if __name__ == "__main__":    
    main()
    
