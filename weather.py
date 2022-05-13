'''
Se va a obtener los 3 eventos siguientes y su clima.
El problema está en que a veces entre el primer evento y el tercero es un més de diferencia.
Hay que buscar solución a eso.
'''
import requests
import json
from datetime import datetime
#FALTA IMPORTAR OPENPYXL

#Listas para almacenar las llaves, temperaturas y días
ListaClaves = []
ListaValores = []
ListaDias = []

#Coordenadas
Latitud = "51.5085"
Longitud = "-0.1257"

#AppID generada por openweather.org
appid = "a3a7114576a3b54a0a02aee0bb777dea"

#request a la pagina especificando ciertos puntos
page = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + Latitud + "&lon=" + Longitud + "&exclude=minutely,hourly&units=metric&appid=" + appid)

#Se generan los diccionarios con .json
weatherData = json.loads(page.content)

#
for x, y in weatherData.items():
    if x == "daily":
        for i in y[1:4]:
            fecha = int(i['dt'])
            dia = datetime.utcfromtimestamp(fecha).strftime("%d-%m-%Y")
            ListaDias.append(dia)

            for key in i['temp']:
                ListaClaves.append(key)
                ListaValores.append(i['temp']['day'])
                ListaValores.append(i['temp']['min'])
                ListaValores.append(i['temp']['max'])
                ListaValores.append(i['temp']['night'])
                ListaValores.append(i['temp']['eve'])
                ListaValores.append(i['temp']['morn'])

print(ListaClaves)
print(ListaValores)
print(ListaValores)
input()

                
