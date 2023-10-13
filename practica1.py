import requests

# URL del archivo CSV que deseas descargar
url = "https://cdn.discordapp.com/attachments/1162177045816688773/1162177784853037127/2016-2022_liga_mx.csv?ex=653afd68&is=65288868&hm=655620cee73312879475da739e69f5fa262331638e34a92d8b820640ae3d5868&"

# Nombre de archivo local para guardar el archivo descargado
nombre_archivo_local = "archivo.csv"

# Realiza la solicitud GET para descargar el archivo
respuesta = requests.get(url)

# Verifica si la descarga fue exitosa (código de respuesta 200)
if respuesta.status_code == 200:
    # Abre el archivo local en modo binario y escribe los datos descargados
    with open(nombre_archivo_local, 'wb') as archivo_local:
        archivo_local.write(respuesta.content)
    print("Descarga exitosa")
else:
    print("Error al descargar el archivo:", respuesta.status_code)