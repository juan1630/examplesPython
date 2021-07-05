import shutil
import os


# se convierte a una lista el resultado de buscar dentro de la carpeta
count = list(os.walk("C:\\projects\\back\horizonte\\horizonte\\contratos\\img"))
print(len(count))
# Sirve para escribir en la consola

list1 = []  
def respaldoFiles():
    conta1 = 0
    #itero cada uno de los resultados
    for img in count:
        files = img[2]
        conta2 = len(files)

        for file in files:
            conta1 += 1
            number = ( 100 * conta1)/conta2
            numerberRound = round( number, 2 )
            shutil.copy( os.path.join("C:\\projects\\back\horizonte\\horizonte\\contratos\\img\\", file) ,  "C:\\Users\\juanp\\OneDrive\\Escritorio\\respaldo")
            print(numerberRound)

            # la funcion que se encarga de copiar cada uno de los archivos


respaldoFiles()