from importlib.machinery import ExtensionFileLoader
import os
from asyncio.log import logger
from OpenSSL import crypto
from tabulate import tabulate
from termcolor import colored
import subprocess

def set_time_stamp(file_path, tsr_path, tsq_path):
    command = "./time_stamp.sh " + file_path + " " + tsr_path + " " + tsq_path
    os.system(command)    

def verify_cert_ocsp(folder_path, cert_name):
    command = "./ocsp_validator.sh " + folder_path + cert_name    
    os.system(command)

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

    print("La firma digital del archivo fue realizada con éxito.")

def verify_sign(folder_path, cert_name, file_name, signature_name):      
    crt_file = open(folder_path + cert_name, "r")   
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, crt_file.read())
    verify_cert_ocsp(folder_path, cert_name)         
    sign_file = open(folder_path + signature_name, 'rb')    
    sign = sign_file.read()    
    file = open(folder_path + file_name, 'r')    
    try:
        crypto.verify(cert, sign, file.read().encode(), "sha512")      
        print(colored("La firma es válida.", 'green', attrs=['bold']))     
    except:
        print(colored("La firma no es válida.\n", 'red', attrs=['bold']))     

def main():       
    p = subprocess.Popen("./ocsp_validator.sh " + "/home/admin/facultaddemate/facultaddemate.pem", stdout=subprocess.PIPE, shell=True)
    print(p.communicate())
    while(True):    
        try:                  
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
                sign_name = input(colored( '  Nombre del archivo de firma digital: ', 'green', attrs=['bold'])) 
                verify_sign(folder_path, cert_name, file_name, sign_name)
            elif(option == "3"):            
                break
            else:
                print("La opción seleccionada es incorrecta. Inténtelo de nuevo.\n")
        except BaseException as exception:
            logger.error('Disculpe, hay un error. Comuníquese con el equipo de TI de la organización.\n'+ str(exception))
            break

if __name__ == "__main__":    
    main()
    
