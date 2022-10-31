from asyncio.log import logger
from tabulate import tabulate
from termcolor import colored
from OpenSSL import crypto

def verify_cert_ocsp():
    pass

def sign_file(file_path, private_key):
    file = open(file_path, 'r')
    sign = crypto.sign(private_key, file.read(), "sha512")
    return sign

def verify_sign(cert_path, signature_path, file_path):
    cert = cert_path
    signature = signature_path
    file = open(file_path, 'r')
    crypto.verify(cert, signature, file.read(), "sha512")    

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
    
