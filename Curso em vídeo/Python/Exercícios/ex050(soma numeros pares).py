# programa que leia seis números inteirsos e mostre a soma apenas dos numeros pares. Se o valor digitador for
#ímpar, desconsidere-o
s = 0 #acumulador
cont = 0 #contador
for c in range(1, 7):
    n = int(input('Digite o {}º valor: '.format(c))) # dica legal aqui no format
    if n % 2 == 0:
        s = s + n # ou s += n
        cont = cont + 1
print('A soma dos {} números pares informados é: {}'.format(cont, s))
