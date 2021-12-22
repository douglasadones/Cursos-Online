#Programa que leia uma expressão matemática com parênteses e verifique se ela é uma
#expressão válida.
lista = []
lista.append(str(input('Digite a expressão: ')))
lista = ' '.join(lista)
aberto = fechado = 0
for c in lista:
    if c == '(':
        aberto += 1
    if c == ')':
        fechado += 1
if aberto == fechado:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
