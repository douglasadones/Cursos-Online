import requests
MY_LAT = -2.919150  # Sua latitude
MY_LONG = -41.752270  # Sua longitude
parametros = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parametros)
response.raise_for_status()
data = response.json()
nascer_do_sol = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # Apenas a hora do nascer do sol
por_do_sol = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # Apenas a hora do por do sol
print(nascer_do_sol)