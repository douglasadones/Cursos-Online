from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # Tirado do site colorhunt.co
RED = "#e7305b"  # Tirado do site colorhunt.co
GREEN = "#9bdeac"  # Tirado do site colorhunt.co
YELLOW = "#f7f5dd"  # Tirado do site colorhunt.co
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    if reps != 0:
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f"00:00")
        text_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
        check_label.config(text="")
        reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_min)
        text_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        text_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK)
    else:
        count_down(work_sec)
        text_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:0>2}:{count_sec:0>2}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # O último argumento retira a borda da imagem.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # 102 e 112 são a posição "x e y".
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Texto Timer
text_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
text_label.grid(row=1, column=2)

# Texto Check
check_label = Label(font=(FONT_NAME, 12, "normal"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(row=4, column=2)

# Botões Start e Reset
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)

window.mainloop()
