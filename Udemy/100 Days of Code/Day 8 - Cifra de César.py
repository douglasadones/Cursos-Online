alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cesar(texto_inicial, quant_deslocamento, direção_da_cifra):
    texto_final = ''
    if direção_da_cifra == "decodificar":
        quant_deslocamento *= -1
    for caractere in texto_inicial:
        if caractere in alfabeto:
            posição = alfabeto.index(caractere)
            nova_posição = posição + quant_deslocamento
            texto_final += alfabeto[nova_posição]
        else:
            texto_final += caractere
    print(f"Aqui está o resultado: {texto_final}")


encerrar = False
while not encerrar:
    direção = input('Digite "codificar" para criptografar, digite "decodificar" para descriptografar:\n')
    texto = input("Escreva a sua mensagem:\n").lower()
    deslocamento = int(input("Digite a quantidade de deslocamento:\n"))


    # E se o usuário inserir uma key maior do que o número de letras do alfabeto?
    deslocamento = deslocamento % 26
    cesar(texto_inicial=texto, quant_deslocamento=deslocamento, direção_da_cifra=direção)


    # Perguntando ao usuário se ele quer iniciar novamente
    reiniciar = input('Digite "sim" caso queira iniciar novamente ou "não" para encerrar.\n')
    if reiniciar == "não":
        encerrar = True
        print("Programa Finalizado.")
