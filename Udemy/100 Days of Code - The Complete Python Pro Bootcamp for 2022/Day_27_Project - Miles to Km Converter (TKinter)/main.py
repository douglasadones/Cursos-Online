from tkinter import *


def conversor():
    valor_em_km = float(dado.get()) * 1.609
    texto_resultado.config(text=round(valor_em_km))


# Ecrã
window = Tk()
window.title("Conversor Milhas para Km")
window.minsize(width=310, height=50)
window.config(padx=55, pady=20)

# Entrada de dados
dado = Entry(width=10)
dado.grid(row=0, column=1)

# Texto Milhas
texto_milhas = Label(text="Milhas", font=("Arial", 12))
texto_milhas.grid(row=0, column=2)

# Texto 2
texto_igual_a = Label(text="É igual a", font=("Arial", 12))
texto_igual_a.grid(row=1, column=0)

# Texto 3
texto_resultado = Label(text="0", font=("Arial", 12))
texto_resultado.grid(row=1, column=1)

# Texto 4
texto_km = Label(text="Km", font=("Arial", 12))
texto_km.grid(row=1, column=2)

# Botão
botao_calcule = Button(text="Calcule", command=conversor)
botao_calcule.config(width=7)
botao_calcule.grid(row=2, column=1)


window.mainloop()
