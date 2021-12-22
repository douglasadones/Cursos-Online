# No python, existe o seguinte caso especial: Pode acontecer do python criar duas variáveis a, por exemplo
# porém podendo conter valores diferentes, sendo uma, uma variável global e outra uma variável local. Veja:
def função():
    n1 = 4 #Variável de escopo local
    print(f'N1 Dentro vale {n1}')


n1 = 2 #Variável de escopo global
função() # Aqui, será mostrado a variável n1 local.
print(f'N1 fora vale {n1}') # Aui será mostrado a variável n1 global.
