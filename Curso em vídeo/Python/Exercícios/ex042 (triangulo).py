l1 = float(input('Digite o Primeiro segmento de reta: '))
l2 = float(input('Digite o Segundo segmento de reta: '))
l3 = float(input('Digite o Terceiro segmento de reta: '))
if abs(l2 - l3) < l1 < (l2 + l3) and abs(l1 - l3) < l2 < (l1 + l3) and abs(l1 - l2) < l3 < (l1 + l2):
    print('Sim! é possível formar com triângulo com os segmetos {:.2f}, {:.2f} e {:.2f}'.format(l1, l2, l3))
    if l1 == l2 and l2 == l3:
        print('Triângulo do tipo \033[1;34mEQUILÁTERO\033[m!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Triângulo do tipo \033[1;34mISÓSCELES\033[m!')
    else:
        print('Triângulo do tipo \033[1;34mESCALENO\033[m!')
else:
    print('Não é possível formar um triângulo com os segmentos {:.2f}, {:.2f} e {:.2f}'.format(l1, l2, l3))
