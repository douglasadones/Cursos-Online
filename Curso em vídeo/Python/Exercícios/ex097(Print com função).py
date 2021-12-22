# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    lin = len(txt) + 4
    print('~' * lin)
    print(f'  {txt}')
    print('~' * lin)


escreva('jhk Mundo!')
escreva('Oi!')
escreva('Curso de Python em Vídeo')


