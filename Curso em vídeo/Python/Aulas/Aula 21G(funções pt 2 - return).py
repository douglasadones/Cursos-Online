# As funções podem não retornar valores (imprimir algo pré definido na tela) ou retornar um valor (return). Quando a
# função não retorna um valor, ficamos limitados ao print pré definido da mesma. Não podemos formatar a resposta.

# Ex de função sem return:
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

# O print "A soma vale {s} será repetida várias vezes.
somar(3, 2, 5)
somar(2, 2)
somar(6)


# Ex de função com return:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # Note que não há mais print na função.


# A resposta (s) vai ser armazenada em cara r. Logo, o valor retornado é o resultado s.
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os meus calculos deram {r1}, {r2} e {r3}.')
# Com a possibilidade de um print formatado, podemos usar os resultados (retornos) das funções com mais liberdade.