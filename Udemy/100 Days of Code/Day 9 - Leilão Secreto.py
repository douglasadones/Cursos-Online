# IDE para iniciantes que ajuda na vizualização: https://pythontutor.com/visualize.html#mode=edit
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
repetição = ''
lances = {}
while repetição != 'não':
    nome = str(input('Qual o seu nome? '))
    oferta = int(input('Qual a sua oferta? R$'))
    lances[nome] = oferta
    print(lances)
    repetição = str(input('Existem mais ofertas? digite "sim" ou "não\n')).strip().lower()
    if repetição == 'não':
        break

#Verificando a maior oferta e seu dono.
maior_oferta = 0
vencedor = ''
for ofertante in lances:
    if lances[ofertante] > maior_oferta:
        maior_oferta = lances[ofertante]
        vencedor = ofertante
ganhador = [vencedor, maior_oferta]
lances['vencedor'] = ganhador
print(f'O vencedor é {lances["vencedor"][0]} com a oferta de R${lances["vencedor"][1]}')
