import requests

#url = "https://backend-laboratorios.herokuapp.com/api/register/pacientes"
#url = "http://localhost:3200/flebotomia/prueba/algo"
#url = "http://localhost:3000/api/list/pacientes"
#url = "https://backend-laboratorios.herokuapp.com/api/list/pacientes"
#url = "https://backend-laboratorios.herokuapp.com/api/register/pacientes"
# url = "http://localhost:3000/api/register/pacientes"
#url = "http://localhost:3000/api/register/product"
# url = "http://localhost:3000/api/new/venta"
# url = "http://localhost:3000/api/new/pedido"
# url = "http://localhost:3000/auth/register/personal"
#url = "http://localhost:3000/api/new/pedido"
#url = "https://backend-laboratorios.herokuapp.com/api/new/venta"
#url = "https://backend-laboratorios.herokuapp.com/api/new/pedido"
# url = "http://localhost:3200/register/nota/indicaciones"
# url = "http://localhost:3000/api/list/paciente/626dab5ee648bb1faac74756"
# url = "http://localhost:3000/api/list/estudios/activos/6270b26d1c706aed7e2ed179"
#url = "http://tecgramapi.southcentralus.cloudapp.azure.com:5000/#portfolio"
url = 'http://localhost:3200'
#url = 'Se debe agregar la url PRD'
endPoint = '/ingreso/hospitalizacion'
urlEndpoint = url + endPoint

print(urlEndpoint)


jsonTest = {}

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
    "tipoDeSangre":"A+",
}

    responseServerPacientes = requests.post( url ,dataJosnPaciente )
    dataRespPacientes = responseServerPacientes.json()

    print( responseServerPacientes)
    print (i)
    print (dataRespPacientes)


    responseServerVentas = requests.post( url ,dataJosnPaciente )
    dataRespPacientes = responseServerVentas.json()

    print( responseServerVentas)
    print (i)
    print (dataRespPacientes)

def registerPersonal(i):
    dataJosnPersonal = {
    "nombre":"Juan Patron",
    "password":"primerAcceso",
    "role":"recepcion"
    }

    responseServerVentas = requests.post( url ,dataJosnPersonal )
    dataRespPacientes = responseServerVentas.json()
    print( responseServerVentas)
    print (i)
    print (dataRespPacientes)

def registerPedidoNew(i):
    dataJsonPedido = {
    "idPaciente":"626dab5ee648bb1faac74756",
    "idServicio":"622838a1d657074f764c33e4",
    "doctorQueSolicito":"David Reyes",
    "nombreServicio":"PRUEBA",
    "idVenta":"626dad2be648bb1faac74e61"
    }

    responsePedidoRequest = requests.post( url ,dataJsonPedido)
    dataPedidoResonse = responsePedidoRequest.json()
    print( responsePedidoRequest )
    print( i )
    print( dataPedidoResonse )


def registerNotasMedicas(i):
    dataNotas = {
    "paciente":"5fcfebe70b82bb00175f2ffa",
    "indicaciones" :[
        "Comer menos", "DR reyes"
    ],
        "hora":"10:40"
    }
    
    reponseRequestNotas = requests.post(url, dataNotas)
    dataNotasMedicas = reponseRequestNotas.json()
    print( reponseRequestNotas )
    print(i)
    print(  dataNotasMedicas )


def registerNewVenta(i):
    dataVentaNew = {
    "paciente":"626dab5ee648bb1faac74756",
    "vendedor":"6223d19dcb2c563bf0f959e7",
    "estudios":[
        "622838a1d657074f764c33e4"
    ],
    "totalCompra":200,
    "folio":i
    }

    responseVentaRequest = requests.post( url ,dataVentaNew)
    dataVentaResonse = responseVentaRequest.json()
    print( responseVentaRequest )
    print( i )
    print( dataVentaResonse )


def getPacienteById(i):
    responseVentaRequest = requests.get( url)
    dataResonse = responseVentaRequest.json()
    print(dataResonse)
    print( i )

def getEstudiosActivos(i):
    responseGetEstudio =  requests.get(url)
    dataResponseEstudios =responseGetEstudio.json()
    print( dataResponseEstudios )
    print(i)

def registerEstudiosNuevos(i):
    dataRegister = {
        "ESTUDIO":"Prueba",
        "PRECIO_PUBLICO":200
    }
    responseRegister = requests.post( url, dataRegister)
    dataResponseRegister = responseRegister.json()
    print( dataResponseRegister )

def getData():
    responseRegister = requests.get( url)
    print( responseRegister )
        

def ingresoHospitalizacion():
    hospi =  {
        "iagnosticoInicial": "Algo muy malo para operar",
        "interrogatorio":"Si",
        "plan": "Algo de lo que sea",
        "enfermeraAtendio": "5e83a3881be2ff1b28408e9c",
        "idPaciente": "5fcfebf40b82bb00175f2ffb",
        "medicoIngreso": "61ba38936722ff03e6aa68f0",
        "medicoTratante": "61ba38936722ff03e6aa68eb"
        }
    responseGetHospi =  requests.post(urlEndpoint, hospi)
    dataHospiResonse = responseGetHospi.json()
    print( dataHospiResonse )


#TODO! NUEVAS FUCIONES PARA PODER CREAR PRUEBAS DE MANERA MAS RAPIDS, SE AGREGO LA FUNCION REGISTEFILEDS Y LA GETDATOS
# ? PARA CREAR LAS PRUEBAS ES NECESARIO QUE SE MODIFIQUE EL JOSNTEST POR EL QUE SE QDEBE ENVIAR AL API

def registerFileds():
    responsePost =  requests.post(urlEndpoint, jsonTest)
    dataHospiResonse = responsePost.json()
    print( dataHospiResonse )



def getDatos():

    responseServer = requests.get( urlEndpoint )
    dataPacientesJson = responseServer.json()
    print(dataPacientesJson)

for i in range(1000):
    # sendData(i)
    # registerPacientes(i)
    #getPacientes(i)
    # registerVentas(i)
    # registerPersonal(i)
    # registerPedidoNew( i )
    # registerNewVenta(i)
    # registerNotasMedicas(i)
    # getPacienteById(i)
    # getEstudiosActivos(i)
    #registerEstudiosNuevos(i)
    # getData()
    ingresoHospitalizacion()