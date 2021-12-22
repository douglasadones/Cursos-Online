num = [2, 2, 5, 3, 9, 1]
print(num)
num.append(4) #Adicionando elemento no final da lista
print(num)
num.sort() #Ordenando a lista (crescente)
print(num)
num.sort(reverse=True) #Ordenando a lista (Decrescente)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0) #Adicionando o valor 0 na posição 2
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.pop() #Exclui o último elemento da lista
print(num)
num.pop(2) #Exclui o elemento da posição 2
print(num)
num.remove(2) #Note que ele excluiu apenas o primeiro elemento "2"
print(num)
if 26 in num: #Usando o if e o in para excluir algo que pode não estar em uma lista evitando assim, erros.
    num.remove(26)
else:
    print('Não encontrei o valor 26')
