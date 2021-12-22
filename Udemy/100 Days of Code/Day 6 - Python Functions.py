# Site bom para aprender laços: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.
# json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Desafio nº 4 aqui: http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Código usado:
'''
def turn_around():
    turn_left()
    turn_left()
    turn_left()


y = 1
while not at_goal():
    if front_is_clear() and y == 1:
        move()
    elif is_facing_north() and right_is_clear():
        turn_around()
        move()
        turn_around()
    elif front_is_clear() and y != 1:
        while y != 1:
            move()
            y -= 1
        turn_left()
    else:
        turn_left()
        while wall_on_right():
            move()
            y += 1
'''
