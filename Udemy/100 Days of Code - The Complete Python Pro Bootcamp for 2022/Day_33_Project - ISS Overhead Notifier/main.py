import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

MEU_EMAIL = "Seu email"
MINHA_SENHA = "Senha do seu Email"
MY_LAT = int  # Sua latitude
MY_LONG = int  # Sua longitude


def iss_proxima():
    """Verifica se a posição atual da iss está entre -5 e 5 graus da sua posição atual. Se sim, retorna True"""
    # Obtendo informações da posição atual da ISS a partir da API.
    response = requests.get(url="http://api.open-notify.org/iss-now.json#")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Sua posição está dentro de +5 ou -5 graus da posição do ISS.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
        return True


def esta_de_noite():
    """Verifica se está a noite. No caso afirmativo, retorna True"""
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

    hora_atual = int(datetime.now().hour)
    if por_do_sol <= hora_atual < nascer_do_sol:
        return True


while True:
    sleep(60)
    # Verifica se a ISS está perto da minha posição atual e é noite. Se sim, envia um email pedindo para olhar para cima
    if iss_proxima() and esta_de_noite():
        # Informações necessárias para o envio do email
        host = "host do seu provedor"
        port = "Número da porta do seu provedor"
        target_email = "email que vai receber a msg"

        # Iniciando o servidor
        with smtplib.SMTP(host, port) as connection:  # Servidor do nosso email (cada provedor de email tem o seu)
            connection.starttls()  # Transport Layer Security (Mensagens Encriptadas)
            connection.login(user=MEU_EMAIL, password=MINHA_SENHA)

            # Motando o e-mail
            corpo = f"ISS Logo acima! :)"

            email_msg = MIMEMultipart()
            email_msg["From"] = MEU_EMAIL
            email_msg["To"] = target_email
            email_msg["Subject"] = "Ei! Parece um bom momento para olhar para o céu!"
            email_msg.attach(MIMEText(corpo, "plain"))  # O método pode ser "plain" ou "html"

            # Enviar o email tipo MIME no servidor SMTP
            connection.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
