from Day13.art import logo, vs
from Day13.game_data import data
from random import choice


def competitors():
    return choice(data)


def checking_game_over(a, b):
    """Asks for the player's choice and Returns True or False for game_over variable"""
    # handling exceptions
    while True:
        try:
            player = str(input('Who has more followers? Type "A" or "B": ')).strip().lower()[0]
        except (ValueError, IndexError):
            print(f'please type "A" or "B". Try again')
        else:
            if player == 'a' or player == 'b':
                break
            else:
                print('please type "A" or "B". Try again')

    # Checking if the player got it right
    if a['follower_count'] > b['follower_count'] and player == 'a':
        return False
    elif a['follower_count'] < b['follower_count'] and player == 'b':
        return False
    else:
        return True


def game():
    a = competitors()
    b = competitors()
    while b == a:
        b = competitors()
    game_over = False
    score = 0
    while not game_over:
        print(logo)
        print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}')
        print(vs)
        print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}')
        game_over = checking_game_over(a, b)
        if not game_over:
            score += 1
            print(f"You're right! Current Score: {score}")
            a = b
            b = competitors()
            while b == a:
                b = competitors()
    print(f"Sorry, that's wrong. Final Score: {score}")


game()
