# Podemos tratar o erro, mostrando ele.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O Resultado foi {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
    