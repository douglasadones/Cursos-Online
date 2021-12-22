#Funções com listas. Vamos tentar dobrar os valores de uma lista através de uma função.
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2, 4, 3, 6, 5, 7]
print(valores)
dobra(valores)
print(valores)

# Note que ao aplicarmos dobra() em valores, existem duas listas: "lts" e "valores". Onde tudo que for feito em
# lst, será feito em valores.

#OBS: Isso não é um empacotamento