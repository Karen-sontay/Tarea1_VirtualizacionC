#KAREN SONTAY
#XIMENA ELIZARDI    

import requests
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = "credenciales1.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

url = 'http://www.randomnumberapi.com/api/v1.0/random?min=1&max=1000&count=1'
response = requests.get(url)
numero = response.text

nombre = numero.strip()  + '.txt'
with open(nombre, 'w') as archivo:
    # Escribir contenido en el archivo
    archivo.write('1026820, 1101720.\n')


folder_id = "1t3Z3CxgA5yfrc4f88_418Wh33lILBScM"
file_names = [nombre]
mime_types = ["text/plain"]

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name" : file_name,
        "parents" : [folder_id]
    }

    media = MediaFileUpload("./{0}".format(file_name), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body = media,
        fields = "id"
    ).execute()
    