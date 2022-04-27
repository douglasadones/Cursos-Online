# Esse programa enviará um email de feliz aniversário para os aniversariantes no dia de seus aniversários.
# As informações dos aniversariantes devem estar no arquivo "birthdays.csv"
from random import randint
import datetime as dt
import pandas
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# TODO  - 1 Obtendo a data atual
data_atual = dt.datetime.now()
dia_atual = data_atual.day
mes_atual = data_atual.month

# TODO  - 2 Lendo o arquivo contendo as datas de aniversários
birthdays = pandas.read_csv('birthdays.csv')
pronto_para_envio = {}
for (index, row) in birthdays.iterrows():
    if row.day == dia_atual and row.month == mes_atual:  # Verificando se existe algum aniversário hoje no arquivo .csv
        # TODO - 3 pegue uma carta aleatória e substitua o nome nela contida pelo nome do(a) aniversariante.
        modelo_de_carta = randint(1, 3)
        with open(f"letter_templates/letter_{modelo_de_carta}.txt") as arquivo:  # Pegando carta aleatória
            carta = arquivo.read()
            nome_modificado = carta.replace("[NAME]", row["name"])  # Pondo o nome do aniversariante na carta

        # Adicionando as informações do(a) aniversariante em um dicionário
        aniversariante = {
            row["name"]: {
                "email": row["email"],
                "carta": nome_modificado,
            }
        }
        pronto_para_envio.update(aniversariante)
        aniversariante.clear()  # Limpando a variável para os casos de aniversariantes simultâneos

# TODO 4 - Mandando a carta gerada no TODO 3 para o email do(a) aniversariante contido no arquivo .csv
# Informações necessárias para o envio do email
for pessoa, informacao in pronto_para_envio.items():
    HOST = "Host do seu provedor"  # ex: "smtp.live.com" para o hotmail.com
    PORTA = 'Porta do seu provedor'
    MEU_EMAIL = "Email que vc deseja enviar as mensagens"
    MINHA_SENHA = "senha do seu email"
    EMAIL_REMETENTE = informacao["email"]

    # Iniciando o servidor
    with smtplib.SMTP(HOST, PORTA) as connection:  # Servidor do nosso email (cada provedor de email tem o seu)
        connection.starttls()  # Transport Layer Security (Mensagens Encriptadas)
        connection.login(user=MEU_EMAIL, password=MINHA_SENHA)

        # Motando o e-mail
        corpo = informacao["carta"]

        email_msg = MIMEMultipart()
        email_msg["From"] = MEU_EMAIL
        email_msg["To"] = EMAIL_REMETENTE
        email_msg["Subject"] = "Happy Birthday!"
        email_msg.attach(MIMEText(corpo, "plain"))

        # Enviar o email tipo MIME no servidor SMTP
        connection.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
