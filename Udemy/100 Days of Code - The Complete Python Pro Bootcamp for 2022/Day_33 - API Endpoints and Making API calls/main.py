# Local na terra através da latitude e da longitude: https://www.latlong.net/Show-Latitude-Longitude.html
import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json#")
# print(response.status_code)  # Irá retornar a resposta numérica
# print(response.raise_for_status())  # Mostrará mais informações sobre a resposta numérica
# data = response.json()  # Dados no formato Json tbm poderiamos especificar: response.json()["iss_position"]
# print(data)
# print(data["iss_position"])
# print(data["iss_position"]["longitude"])
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# Usando parâmetros nas API's
MY_LAT = -2.919150
MY_LONG = -41.752270
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # Apenas a hora do nascer do sol
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]  # Apenas a hora do por do sol

print(sunrise)

time_now = dt.datetime.now()

print(f"{time_now.hour:0>2}")  # Hora atual
