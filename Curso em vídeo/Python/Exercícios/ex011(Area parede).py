#Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
