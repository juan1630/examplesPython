import requests

#url = "https://backend-laboratorios.herokuapp.com/api/register/pacientes"
#url = "http://localhost:3200/flebotomia/prueba/algo"
#url = "http://localhost:3000/api/list/pacientes"
#url = "https://backend-laboratorios.herokuapp.com/api/list/pacientes"
#url = "https://backend-laboratorios.herokuapp.com/api/register/pacientes"
#url = "http://localhost:3000/api/register/pacientes"
#url = "http://localhost:3000/api/register/product"
#url = "http://localhost:3000/api/new/venta"
#url = "http://localhost:3000/api/new/pedido"
url = "http://localhost:3000/auth/register/personal"

def getPacientes(i):
    responseServerPacientes = requests.get( url )
    dataPacientesJson = responseServerPacientes.json()
    print(dataPacientesJson)
    print(i)



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

def registerVentas(i):
    dataVentas = {
    "paciente":"622564b5c952ca425f3b3869",
    "vendedor":"622d0ad4ed2c996f1a6f6f84",
    "estudios":[
        "622838a1d657074f764c33e4"
    ],
    "totalCompra":500,
    "folio":1
    }
    responseServervetnas = requests.post( url ,dataVentas )
    dataRespPacientes = responseServervetnas.json()

    print( responseServervetnas)
    print (i)
    print (dataRespPacientes)



def registerPacientes(i):
    dataJosnPaciente = {
    "nombrePaciente":"Juan Prueba 1",
    "genero":"masculino",
    "edad":25,
    "curp":"xxxxxxxxxxxxxxxxxxxxxxxx",
    "correoPaciente":"juan@gmail.com    ",
    "estadoPaciente":"Morelos",
    "tipoDeSangre":"A+"
}

    responseServerPacientes = requests.post( url ,dataJosnPaciente )
    dataRespPacientes = responseServerPacientes.json()

    print( responseServerPacientes)
    print (i)
    print (dataRespPacientes)


def registerPedido(i):
    dataJosnPaciente = {
    "idPaciente":"622564b5c952ca425f3b3869",
    "idServicio":"622838a1d657074f764c33e4",
    "doctorQueSolicito":"David Reyes",
    "nombreServicio":"PRUEBA",
    "idVenta":"622d0c9ee985bec9065c6eb8"
}
    responseServerVentas = requests.post( url ,dataJosnPaciente )
    dataRespPacientes = responseServerVentas.json()

    print( responseServerVentas)
    print (i)
    print (dataRespPacientes)

def registerPersonal(i):
    dataJosnPersonal = {
    "nombre":"Juan Patron",
    "password":"primerAcceso"
    }

    responseServerVentas = requests.post( url ,dataJosnPersonal )
    dataRespPacientes = responseServerVentas.json()

    print( responseServerVentas)
    print (i)
    print (dataRespPacientes)


for i in range(100):
    #sendData(i)
    #registerPacientes(i)
    #getPacientes(i)
    #registerVentas(i)
    #registerPedido(i)
    registerPersonal(i)
