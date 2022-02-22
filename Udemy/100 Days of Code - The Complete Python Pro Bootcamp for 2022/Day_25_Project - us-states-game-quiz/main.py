import turtle
from map import Map
from closing_instructions import Instructions

# # Obtendo as coordenadas da screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()  # Forma alternativa de deixar a screen aberta mesmo depois do código ter terminado.

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Aqui é adicionado um novo formato para a tartaruga. Obs: Pode ser uma imagem no formato .gif
turtle.shape(image)  # Naturalmente, podemos escolher esse novo formato.

my_map = Map()
instructions = Instructions()

try:
    while len(my_map.correct_answers) < 50:
        answer_state = screen.textinput(title=f"{len(my_map.correct_answers)}/{my_map.num_states} States Correct",
                                        prompt="What's another state's name?").title()
        if answer_state == "Exit":
            break
        my_map.checking_answer(answer_state)
except AttributeError:
    print("Quiz closed")

my_map.new_csv()

