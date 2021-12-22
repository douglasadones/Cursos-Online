#Para que um parâmetro seja opcional, basta definir um valor padrão para este. Veja:

# Sem parâmetro opcional:
def contador(a, b, c):
    s = a + b + c
    print(f'O resultado da soma é {s}')


contador(0, 10, 2) # Aqui funciona tudo normal>
contador(10, 80) # Aqui dá erro, pois a cariável p não foi informada!


# Com um parâmetro opcional:
def contador(a, b, c=0): # O parâmetro c agora é opcional.
    s = a + b + c
    print(f'O resultado da soma é {s}')


contador(0, 10, 2) # Aqui funciona tudo normal>
contador(10, 80) # Agora funciona, pois, mesmo não informado, o parâmetro c vale, por padrão, zero.


# Com mais de um parâmetro opcional:
def contador(a=0, b=0, c=0): # Aqui, todos os parâmetros são opcionais. Funciona normalmente.
    s = a + b + c
    print(f'O resultado da soma é {s}')


contador(0, 10, 2) # resulta em 12
contador(10, 80) # Resulta em 90
contador() # Resulta em 0
