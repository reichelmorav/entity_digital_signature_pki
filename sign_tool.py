from asyncio.log import logger
from tabulate import tabulate
from termcolor import colored

def main():       
    while(True):    
        try:                  
            table = [['BIENVENIDO(A) A LA APLICACIÓN DE FIRMA DIGITAL DE LA UCR'], ['1. Firmar documento'], ['2. Validar firma'], ['3. Salir']]
            print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
            option = input("Ingrese el número de la opción deseada: ")
            if(option == "1"):      
                break                        
            elif(option == "2"):            
                break
            elif(option == "3"):            
                break
            else:
                print("La opción seleccionada es incorrecta. Inténtelo de nuevo.\n")
        except BaseException as exception:
            logger.error('Sorry, there is an exception: '+ str(exception))
            break

if __name__ == "__main__":    
    main()
    
