n1 = int(input('Escreva um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}'.format(n1+n2)) esse comando serve caso você não precise usar a soma posteriormente.
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
# {:.3f} especifica que ele quer uma aproximação de até 3 casas decimais e o 'f' se refere a ponto flutuante(float)
print('A divisão inteira é {} e a potência {}'.format(di, e))
print('='*40)
# Se por , end=' ' no final do primeiro print, o próximo print será impresso na mesma linha do anterior. Ex:
# Obs: Se você por algo dentro do ' ', ele será reproduzido na interseção dos print ex: , end=' >>> ' vai gerar: blablabla >>> blebleble
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {} e a potência {}'.format(di, e))
print('='*40)
# Podemos o comando \n para quebrar a linha de um print adicionado outra linha na impressão para não precisar ficar repetindo o comando print várias vezes. Ex:
print('A soma é {}, \no produto é {} e a \ndivisão é {:.3f}'.format(s, m, d))
