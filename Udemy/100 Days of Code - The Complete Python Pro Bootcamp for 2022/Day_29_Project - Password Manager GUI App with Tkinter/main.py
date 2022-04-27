from tkinter import *
from tkinter import messagebox  # popups
from random import randint, choice, shuffle
import pyperclip  # adiciona um texto na área de transferência

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "_", "-", "<", ">", ".", "+"]


def password_generator():
    if len(password_entry.get()) == 0:
        new_password_list = [choice(letters) for _ in range(randint(8, 10))]
        new_password_list += [choice(numbers) for _ in range(randint(2, 4))]
        new_password_list += [choice(symbols) for _ in range(randint(2, 4))]

        shuffle(new_password_list)

        new_password = "".join(new_password_list)
        password_entry.insert(0, new_password)
        pyperclip.copy(text=new_password)  # adiciona a senha na área de transferência


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get().strip().capitalize()
    email = username_entry.get().strip()
    password = password_entry.get().strip()

    if len(website) != 0 and len(email) != 0 and len(password) != 0:
        popup = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if popup:
            with open("Senhas.txt", mode="a") as file:
                if len(website) != 0 and len(email) != 0 and len(password) != 0:
                    file.write(f"Website: {website}\nEmail: {email}\nPassword: {password}\n\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=20)

# Logo
img_logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=0, columnspan=2, sticky="e")  # "sticky" Posição do elemento na coluna (pontos cardeais)

# Labels
website_text = Label(text='Website:')
website_text.grid(row=1, column=0)
username_text = Label(text='Email/Username:')
username_text.grid(row=2, column=0)
password_text = Label(text='Password:')
password_text.grid(row=3, column=0)

# Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")  # columnspan: quantas colunas irá ocupar
website_entry.focus()  # Cursor ficará ativo de início.
username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
username_entry.insert(0, "adones12phb@hotmail.com")  # Texto padrão
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
password_generate_button = Button(text='Generate Password', width=14, command=password_generator)
password_generate_button.grid(row=3, column=1, columnspan=2, sticky="e")
add_button = Button(text='Add', width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="we")

window.mainloop()
