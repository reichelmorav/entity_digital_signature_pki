from asyncio.log import logger
import os
from tabulate import tabulate
from termcolor import colored
from OpenSSL import crypto

def set_time_stamp(file_path, tsr_path, tsq_path ):
    command = "./time_stamp.sh " + file_path + " " + tsr_path + " " + tsq_path
    os.system(command)    

def verify_cert_ocsp():
    pass

def sign_file(file_path, key_path, signature_path):    
    key_file = open(key_path, "rb")
    key = crypto.load_privatekey(crypto.FILETYPE_PEM, key_file.read())
    file = open(file_path, 'r')
    sign = crypto.sign(key, file.read(), "sha512")

    sign_file = open(signature_path, 'wb')
    sign_file.write(sign)
    sign_file.close()     

def verify_sign(cert_path, signature_path, file_path):    
    cert_file = open(cert_path, "rb")
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_file.read())    
    sign_file = open(signature_path, 'rb')
    sign = sign_file.read()
    file = open(file_path, 'r')
    crypto.verify(cert, sign, file.read(), "sha512")    

def main():       
    while(True):    
        try:                  
            table = [['BIENVENIDO(A) A LA APLICACIÓN DE FIRMA DIGITAL DE LA UCR'], ['1. Firmar documento'], ['2. Validar firma'], ['3. Salir']]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            option = input("Ingrese el número de la opción deseada: ")
            if(option == "1"):      
                print('Por favor, proporcione los siguientes datos:')  
                file_path = input(colored( '  Ubicación del archivo: ', 'green', attrs=['bold']))       
                key_path  = input(colored( '  Ubicación de su llave privada: ', 'green', attrs=['bold']))               
            elif(option == "2"):        
                print('Por favor, proporcione los siguientes datos:')  
                cert_path = input(colored( '  Ubicación de su certificado digital: ', 'green', attrs=['bold'])) 
                sign_path = input(colored( '  Ubicación de la firma digital: ', 'green', attrs=['bold'])) 
                file_path = input(colored( '  Ubicación del archivo: ', 'green', attrs=['bold']))        
            elif(option == "3"):            
                break
            else:
                print("La opción seleccionada es incorrecta. Inténtelo de nuevo.\n")
        except BaseException as exception:
            logger.error('Disculpe, hay un error. Comuníquese con el equipo de TI de la organización. '+ str(exception))
            break

if __name__ == "__main__":    
    main()
    
