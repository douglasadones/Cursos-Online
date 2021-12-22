# Podemos ter vários except com vários tipos de exceção.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O Erro encontrado foi {erro.__cause__}')
else:
    print(f'O Resultado foi {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
