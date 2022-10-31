from asyncio.log import logger
import tabulate
from termcolor import colored

def main():       
    while(True):    
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
   

if __name__ == "__main__":    
    main()
    
