from asyncio.log import logger
import os
from tabulate import tabulate
from termcolor import colored
from OpenSSL import crypto

def set_time_stamp(file_path, tsr_path, tsq_path):
    command = "./time_stamp.sh " + file_path + " " + tsr_path + " " + tsq_path
    os.system(command)    

def verify_cert_ocsp():
    pass

def sign_file(folder_path, file_name, key_name):   
    file_to_sign = folder_path + file_name
    key_file = open(folder_path + key_name, "rb")
    key = crypto.load_privatekey(crypto.FILETYPE_PEM, key_file.read())
    file = open(file_to_sign, 'r')
    sign = crypto.sign(key, file.read().encode(), "sha512")

    sign_file = open(file_to_sign + '.sign', 'wb')
    sign_file.write(sign)
    sign_file.close()     

    set_time_stamp(file_to_sign, file_to_sign + '.tsr', file_to_sign + '.tsq')

def verify_sign(folder_path, cert_name, signature_name, file_name):   
    print("Hola 1") 
    crt_file = open(folder_path + cert_name, "r").read()
    print("Hola 2")    
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, crt_file) 
    print("Hola 3") 
    sign_file = open(folder_path + signature_name, 'rb')
    print("Hola 4") 
    sign = sign_file.read()
    print("Hola 5") 
    file = open(folder_path + file_name, 'r')
    print("Hola 6") 
    crypto.verify(cert, sign, file.read(), "sha512")    

def main():       
    while(True):    
        # try:                  
        table = [['BIENVENIDO(A) A LA APLICACIÓN DE FIRMA DIGITAL DE LA UCR'], ['1. Firmar documento'], ['2. Validar firma'], ['3. Salir']]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
        option = input("Ingrese el número de la opción deseada: ")
        if(option == "1"):      
            print('Por favor, proporcione los siguientes datos:')  
            folder_path = input(colored( '  Ruta de la carpeta de archivos: ', 'green', attrs=['bold']))   
            file_name = input(colored( '  Nombre del archivo: ', 'green', attrs=['bold']))        
            key_name  = input(colored( '  Nombre de la llave privada: ', 'green', attrs=['bold']))                
            sign_file(folder_path, file_name, key_name)                               
        elif(option == "2"):        
            print('Por favor, proporcione los siguientes datos:')  
            folder_path = input(colored( '  Ruta de la carpeta de archivos: ', 'green', attrs=['bold']))                
            cert_name = input(colored( '  Nombre de su certificado digital: ', 'green', attrs=['bold']))                 
            file_name = input(colored( '  Nombre del archivo: ', 'green', attrs=['bold']))        
            sign_name = input(colored( '  Nombre del aehivo de firma digital: ', 'green', attrs=['bold'])) 
            verify_sign(folder_path, cert_name, sign_name, file_name)
        elif(option == "3"):            
            break
        else:
            print("La opción seleccionada es incorrecta. Inténtelo de nuevo.\n")
        # except BaseException as exception:
        #     logger.error('Disculpe, hay un error. Comuníquese con el equipo de TI de la organización.\n'+ str(exception))
        #     break

if __name__ == "__main__":    
    main()
    
