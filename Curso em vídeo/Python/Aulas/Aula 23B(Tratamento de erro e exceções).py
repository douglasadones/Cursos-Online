# Utilizando as funções para tratamento de erro
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: #Caso dê algum erro
    print('Infelizmente Tivemos um problema')
else:# Caso não dê erro. (Cláusula Opcional.)
    print(f'O Resultado foi {r:.2f}')
finally:# Vai acontecer independente da existência de erro (Cláusula Opcional.)
    print('Volte sempre! Muito obrigado!')
