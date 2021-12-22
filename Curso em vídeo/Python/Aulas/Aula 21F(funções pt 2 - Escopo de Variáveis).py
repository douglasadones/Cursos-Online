# Caso desejemos que o python não crie uma variável local, devemos usar a palavra "global" seguido da variável
# Garantindo assim, que o python não crie uma variável local e use e modifique apenas a variável global. Beja:
def teste(b):
    global a # Aqui o python será impedido de criar uma variável "a" local e modificará a variável global :)
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5 # Variável de Escopo Global.
teste(a)
print(f'A fora vale {a}')
