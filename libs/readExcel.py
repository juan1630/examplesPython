import pandas as pd 
#importamos pandas 

data = pd.read_excel('./pruebaProveedores.xlsx', header=None );

data.head()

for col in data[3]:
    if( type(col) == int ):
        num1 = col
