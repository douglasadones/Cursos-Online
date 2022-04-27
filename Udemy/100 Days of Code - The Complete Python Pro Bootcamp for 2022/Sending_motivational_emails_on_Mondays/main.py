import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice
import datetime as dt


def sundays_emails():
    # Usando o arquivo .txt das citações
    with open("quotes.txt", "r") as citacoes:
        quote_list = citacoes.readlines()

    # Informações necessárias para o envio do email
    host = "host do seu provedor"
    port = int  # Port do seu provedor
    my_email = "email que enviará a msg"
    my_password = "senha do seu email"
    target_email = "email que receberá a msg"

    # Iniciando o servidor
    with smtplib.SMTP(host, port) as connection:  # Servidor do nosso email (cada provedor de email tem o seu)
        connection.starttls()  # Transport Layer Security (Mensagens Encriptadas)
        connection.login(user=my_email, password=my_password)

        # Motando o e-mail
        corpo = f"<h2>{choice(quote_list)}</h2>"

        email_msg = MIMEMultipart()
        email_msg["From"] = my_email
        email_msg["To"] = target_email
        email_msg["Subject"] = "Mensagem Motivacional da Segunda-feira :D!"
        email_msg.attach(MIMEText(corpo, "html"))  # método de html (Sem ser o plain)

        # Enviar o email tipo MIME no servidor SMTP
        connection.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    sundays_emails()
