# Exite o Escopo Global (vale para o programa principal) e o Escopo Local (Vale apenas na função inserida.

def teste():
    x = 8 # Variável de escopo local
    print(f'Na função test, n vale {n}') # Usa a variável de escopo global declarada fora da função
    print(f'Na função test, x vale {x}') # Variável de escopo local só é válida dentro da função.


n = 2 # Variável de escopo Global, pois mesmo dentro da função, ela mantêm o mesmo valor
print(f'No programa principal, n vale {n}') #Vai mostrar o n normalmente
teste()
print(f'No programa principal, x vale {x}') # vai dar erro pois o x, por ter sido declarado dentro de uma def, possúi
# Apenas o escopo local (Só pode ser usado dentro da def).
