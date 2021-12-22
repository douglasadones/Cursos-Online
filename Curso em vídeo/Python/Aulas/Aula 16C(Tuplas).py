#podemos ordenar as Tuplas (Em ordem alfabética)
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
print(sorted(lanche))
print(lanche)#A tupla é imutável

# podemos juntar duas Tuplas com o "+"
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(a)
print(b)
print(c)
print(sorted(c))
print(c.count(5)) #quantas vezes o número 5 aparece na tupla c

#propriedade .index() para saber a posição dos objetos
print(c)
print(c.index(2)) #Só mostra a primeira ocorrência
print(c.index(2, 1)) #Começa a busca a partir da posição 1(Deslocamento).

