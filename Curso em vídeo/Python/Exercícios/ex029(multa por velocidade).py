velocidade = int(input('Digite a velocidade do seu carro em km/h: '))
maxima = 80
if velocidade <= maxima:
    print('Não sofreu multas! Você está dentro do limite de velocidade.')
else:
    multa = (velocidade - maxima) * 7
    print('Você sofreu uma multa no valor de R${}!'.format(multa))
