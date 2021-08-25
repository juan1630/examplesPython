import pandas as pd 
#importamos pandas 

# hacemos uso de la columna 3 para ahorrar tiempo de ejecución
data = pd.read_excel('./pruebaProveedores.xlsx', header=None, names=['Proveedor', 'Producto' ,'Precio'] )

# print(data[['Precio']])
productos = data['Producto']
proveedores = data['Proveedor']

print( productos )
# print( type(productos) )

# for col in productos:
#     print(productos)

# data.head()

# for col in data:

#     if( type(col) == int ):
#             num1 = data[col]
#             print(num1)

