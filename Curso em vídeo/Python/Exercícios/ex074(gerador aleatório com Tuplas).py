from random import randint
tupla = ()
cont = 0
maior = menor = int
while cont < 5:
    random = randint(0, 10),
    tupla += random
    cont += 1
    if cont == 1:
        maior = random
        menor = random
    else:
        if random > maior:
            maior = random
        if random < menor:
            menor = random
print(tupla)
print(f'O maior número sorteado foi {maior[0]}\nO menor número sorteado foi {menor[0]}')
