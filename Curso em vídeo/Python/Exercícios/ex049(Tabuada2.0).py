# Fazer uma tabuada usando a estrutura de repetição for
frase = 'TABUADA'
print('{:^52}'.format(frase))
n = int(input('Digite o número inteiro para vizualizar sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print('{} x {:>2} = \033[1;34m{}\033[m'.format(n, c, n * c))
print('-' * 12)
