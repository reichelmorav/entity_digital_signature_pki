from OpenSSL import crypto
import os

TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA
HOME = os.getenv("HOME")

C = "CR"
ST = "San Jose"
L = "San Pedro"
O = "UCR ECCI ITI"
OU = "II 2022"

def generatekey(keypath):
    key = crypto.PKey()
    key.generate_key(TYPE_RSA, 4096)
    key_file = open(keypath, "wb")
    key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    key_file.close()
    return key

def generateCRS(key, csrpath, entity):
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


def main():
    while(True):    
        option = input("Bienvenido. \n 1. Generar certificado para unidad \n 2. Salir \n¿Cuál opción desea?: ")
        if(option == "1"):       
            entity = input("Ingrese el nombre de la unidad: ")
            #email = input("Ingrese el correo:")
            keypath = HOME + "/" + entity + '.key'
            csrpath = HOME + "/" + entity + '.csr'
            crtpath = HOME + "/" + entity + '.crt'
            key = generatekey("hola")
            generateCRS(key, "csrpath", entity)
            print ("La llave privada se encuentra en:" + keypath)
            print ("El CSR se encuentra en:" + csrpath)
            break
        elif(option == "2"):            
            break
        else:
            print("La opción seleccionada no es correcta. Intentelo de nuevo\n")

if __name__ == "__main__":
    main()
    
