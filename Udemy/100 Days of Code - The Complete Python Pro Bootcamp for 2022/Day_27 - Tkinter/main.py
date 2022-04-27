# Documentação: https://docs.python.org/3/library/tkinter.html ou http://tcl.tk/man/tcl8.6/TkCmd/contents.htm
# ou https://dafarry-github-io.translate.goog/tkinterbook/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc
from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I Got Clicked")


def new_button():
    new_text = input.get()
    print("Ho! I Got Clicked!")


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "normal"))
my_label.grid(column=0, row=0)  # pack() põe o objeto no ecrã. Argumentos vistos: side="left", expand="True" (Centro da tela)
my_label.config(padx=50, pady=30)

my_label["text"] = "New Text"  # Assim alteramos / atualizamos as propriedades de um determinado componente.
my_label.config(text="New Text")  # ou assim.

# Button
bottun = Button(text="Click Me", command=button_clicked)
bottun.grid(column=1, row=1)

bottun2 = Button(text="Click Me²", command=new_button)
bottun2.grid(column=2, row=0)

# Entrada de dados
input = Entry(width=10)
new_text = input.get()
input.grid(column=3, row=2)

print(new_text)

window.mainloop()  # Isso sempre pode ficar no fim do programa (O que matém a tela aberta)
