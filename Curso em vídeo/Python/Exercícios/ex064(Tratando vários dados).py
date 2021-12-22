# Programa que leia vários números, pare de ler ao ser digitado 999 e some todos os números (com exceção do 999)
n = cont = soma = 0 #importante lembrar dessa sintaxe
n = int(input('Digite um número [999 para parar]: '))
while n != 999: #999 é o nosso "flag"
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: ')) # está repetido aqui pois, ao digitar 999, o programa não irá
                                                          # repetir e com isso não contará com o 999 na soma e no cont.
print('Você digitou {} números e a soma entre eles foi de {}'.format(cont, soma))
