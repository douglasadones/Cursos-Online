from random import choice
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# -------------------------------- CSV TO DICT --------------------------------- #
try:
    data = pandas.read_csv("data/words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --------------------------------- FUNCTIONS ---------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancela a antiga contagem para trocar o card
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="Inglês", fill="black")
    canvas.itemconfig(card_word, text=current_card["english"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)  # Inicia uma nova contagem para trocar o card


def flip_card():
    canvas.itemconfig(card_title, text="PT-BR", fill="white")
    canvas.itemconfig(card_word, text=current_card["pt_br"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_know():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ------------------------------ USER INTERFACE ------------------------------- #
window = Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_imagem = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_imagem, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button_imagem = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_imagem, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
