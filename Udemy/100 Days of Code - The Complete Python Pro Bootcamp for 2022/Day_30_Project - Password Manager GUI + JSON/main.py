from tkinter import *  # GUI
from tkinter import messagebox  # popups
from random import randint, choice, shuffle
import pyperclip  # adiciona um texto na área de transferência
import json  # Usa e cria API's json

# ---------------------------- GERADOR DE SENHA ------------------------------- #
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
          "S", "T", "U", "V", "W", "X", "Y", "Z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "<", ">", ".", "+"]


def gerador_de_senha():
    """Gera uma senha aleatória com as listas acima, preenche na entrada da senha e a adiciona na
    área de transferência"""
    if len(entrada_para_senha.get()) == 0:
        lista_com_nova_senha = [choice(letras) for _ in range(randint(8, 10))]
        lista_com_nova_senha += [choice(numeros) for _ in range(randint(2, 4))]
        lista_com_nova_senha += [choice(simbolos) for _ in range(randint(2, 4))]

        shuffle(lista_com_nova_senha)

        nova_senha = "".join(lista_com_nova_senha)
        entrada_para_senha.insert(0, nova_senha)
        pyperclip.copy(text=nova_senha)  # adiciona a senha na área de transferência


# ---------------------------- SALVAR SENHA ------------------------------- #


def save_password():
    """Salva os dados num arquivo 'senhas.json' que será criado caso não exista."""
    website = entrada_para_website.get().strip().capitalize()
    email = entrada_para_username.get().strip()
    senha = entrada_para_senha.get().strip()
    novo_dado = {website: {
        "email": email,
        "senha": senha,
    }}

    if len(website) == 0 or len(senha) == 0:
        messagebox.showinfo(title="Oops", message="Por favor, não deixe nenhum campo vazio.")
    else:
        try:
            with open("senhas.json", mode="r") as file:
                # lê o dado antigo
                dado = json.load(file)
        except FileNotFoundError:
            with open("senhas.json", mode="w") as file:
                # Salvar dados atualizados
                json.dump(novo_dado, file, indent=4)
        else:
            # Atualizando dados antigos com novos dados
            dado.update(novo_dado)

            with open("senhas.json", mode="w") as file:
                # Salvar dados atualizados
                json.dump(dado, file, indent=4)
        finally:
            entrada_para_website.delete(0, END)  # Limpa o campo para o website
            entrada_para_senha.delete(0, END)  # Limpa o campo para a senha
            entrada_para_website.focus()  # Cursor fica no campo do website


# -------------------------- SAVE PASSWORD ----------------------------- #
def search():
    """Busca no arquivo 'senhas.json' pelo website informado e, caso encontre, mostrará em um popup o email e a
    senha armazenados e adicionará a senha na área de transferência."""
    try:
        with open("senhas.json", "r") as file:
            file = json.load(file)
            website_informado = entrada_para_website.get().capitalize()
            email_do_webiste_informado = file[website_informado]["email"]
            senha_do_webiste_informado = file[website_informado]["senha"]
    except KeyError:
        if len(website_informado) == 0:
            messagebox.showinfo(title="Oops", message="Campo 'Website' vazio.")
        else:
            messagebox.showinfo(title="Oops", message=f"Website '{website_informado}' não encontrado.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="Sem dados registrados.")
    else:
        pyperclip.copy(senha_do_webiste_informado)
        messagebox.showinfo(title=website_informado, message=f"Email: {email_do_webiste_informado}"
                                                             f"\nSenha: {senha_do_webiste_informado}\n"
                                                             f"Senha copiada.")


# ---------------------------- CONFIGURAÇÃO DA UI ------------------------------- #
window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=50, pady=20)

# Logo
img_logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(80, 100, image=img_logo)
canvas.grid(row=0, column=1, columnspan=2, sticky="we")  # "sticky" Posição do elemento na coluna (pontos cardeais)

# Textos
texto_website = Label(text="Website:")
texto_website.grid(row=1, column=0)
texto_username = Label(text="Email/Username:")
texto_username.grid(row=2, column=0)
texto_senha = Label(text="Senha:")
texto_senha.grid(row=3, column=0)

# Entradas
entrada_para_website = Entry(width=21)
entrada_para_website.grid(row=1, column=1, sticky="w")  # columnspan: quantas colunas irá ocupar
entrada_para_website.focus()  # Cursor ficará ativo de início.
entrada_para_username = Entry(width=40)
entrada_para_username.grid(row=2, column=1, columnspan=2, sticky="w")
entrada_para_username.insert(0, "Email usual")  # Texto padrão
entrada_para_senha = Entry(width=21)
entrada_para_senha.grid(row=3, column=1, sticky="w")

# Botões
botao_de_procura = Button(text="Procurar", width=14, command=search)
botao_de_procura.grid(row=1, column=1, columnspan=2, sticky="e")
botao_gerador_de_senha = Button(text="Gerar Senha", width=14, command=gerador_de_senha)
botao_gerador_de_senha.grid(row=3, column=1, columnspan=2, sticky="e")
botao_salvar = Button(text="Salvar", width=30, command=save_password)
botao_salvar.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
