import requests

# url = "https://blooming-sea-53514.herokuapp.com/agregar/modulo"
url = "http://localhost:3200/flebotomia/prueba/algo"

responseServer = requests.get( url )
data = responseServer.json()
print( data )