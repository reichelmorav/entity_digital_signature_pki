from OpenSSL import crypto
#from termcolor import colored 
import os, socket

PORT = 9225
HOST = '192.168.133.133'
TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA
HOME = os.getenv("HOME")

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

def generate_CRS(key, csrpath, entity):
    req = crypto.X509Req()
    req.get_subject().C = C     
    req.get_subject().ST = ST
    req.get_subject().L = L
    req.get_subject().O = O     
    req.get_subject().OU = OU
    req.get_subject().CN = entity.upper()
    req.get_subject().emailAddress = entity + '@ucr.ac.cr'    
    req.set_pubkey(key)
    req.sign(key, "sha512")        
   
    ca_file = open(csrpath, 'wb')
    ca_file.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))
    ca_file.close()  

def send_to_sign(csrpath):
    file = open(csrpath, 'rb')
    certificate = file.read() 
    sock.sendall(certificate)    
    file.close()

def main():
    global sock       
    while(True):    
        try:
            sock = socket.socket()
            sock.connect((HOST, PORT))
            option = input("Bienvenido. \n 1. Generar certificado para unidad \n 2. Salir \n¿Cuál opción desea?: ")
            if(option == "1"):       
                entity = input("Ingrese el nombre de la unidad: ").replace(" ", "")          
                keypath = HOME + "/" + entity + '.key'
                csrpath = HOME + "/" + entity + '.csr'
                crtpath = HOME + "/" + entity + '.pem'               
                generate_CRS(generate_key(keypath), csrpath, entity)
                send_to_sign(csrpath)
                crt_file = open(crtpath, 'wb')
                crt_file.write(sock.recv(4096))                
                print ("La llave privada se encuentra en: " + keypath)
                print ("El CSR se encuentra en: " + csrpath)
                print ("El certificado se encuentra en: " + crtpath)
                sock.close()
                break
            elif(option == "2"):            
                break
            else:
                print("La opción seleccionada no es correcta. Intentelo de nuevo\n")
        except:
            print("An exception occurred")
            break

if __name__ == "__main__":
    main()
    
