# Para saber como uma função interna/biblioteca do python funciona, podemos ler um docstring(tutorial)
# mostrando seu modo de uso. Podemos fazer isso de três formas:

# Primeira forma: Pelo python console, escreva help() e vc entrará no modo interactive help.
    # Agora basta digitar algum comando que vc deseja saber o modo de uso. Ex: print, len, input e etc.
    # Para sair desse modo, basta digitar quit.

#Segunda forma:
help(print)

#Terceira forma:
print(input.__doc__)
