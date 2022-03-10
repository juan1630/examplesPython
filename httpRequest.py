import requests

#url = "https://backend-laboratorios.herokuapp.com/api/register/pacientes"
#url = "http://localhost:3200/flebotomia/prueba/algo"
#url = "http://localhost:3000/api/list/pacientes"
#url = "https://backend-laboratorios.herokuapp.com/api/list/pacientes"
#url = "https://backend-laboratorios.herokuapp.com/api/register/pacientes"
url = "http://localhost:3000/api/register/pacientes"

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


for i in range(100):
    #sendData(i)
    registerPacientes(i)
    #getPacientes(i)
