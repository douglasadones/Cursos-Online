#Programa que leia 5 números, adicione-os em uma lista nas posições corretas fazendo com que o print inal mostre a lista em ordem crescente.
#Não pode usar o comando sort().
lista = []
for c in range(0, 5):
    n = int(input('Adicione um valor: '))
    if c == 0 or n >= lista[-1]: #num[-1] é o último elemento.
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {lista}')
