import requests

url = "https://backend-laboratorios.herokuapp.com/api/register/product"
#url = "http://localhost:3200/flebotomia/prueba/algo"

def sendData(i):
    dataJosn = {
        "ESTUDIO":"Prueba",
        "PRECIO_PUBLICO":200
    }

    responseServer = requests.post( url ,dataJosn )
    dataResp = responseServer.json()

    print( responseServer)
    print (i)
    print (dataResp)

for i in range(100):
    sendData(i);
