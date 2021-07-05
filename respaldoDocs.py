import shutil
import os

# se convierte a una lista el resultado de buscar dentro de la carpeta
count = list(os.walk("C:\\projects\\back\horizonte\\horizonte\\contratos\\img"))
# print(count)

def respaldoFiles():
    #itero cada uno de los resultados
    for img in count:
        files = img[2]
        for file in files:
            print(file)
            shutil.copy( os.path.join("C:\\projects\\back\horizonte\\horizonte\\contratos\\img\\", file) ,  "C:\\Users\\juanp\\OneDrive\\Escritorio\\respaldo")
            # la funcion que se encarga de copiar cada uno de los archivos


respaldoFiles()