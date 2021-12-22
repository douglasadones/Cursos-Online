expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(') #Aqui ele adiciona na lista um parênteses aberto
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop() #Aqui, caso o parêntese aberto encontre um fechado, ele exclui um "(" da lista.
        else:
            pilha.append(')') # aqui, caso a pilha esteja vazia, ele mostrará um erro.
            break
if len(pilha) == 0:
    print('Sua expressão é Valida!')
else:
    print('Sua expressão está errada!')
