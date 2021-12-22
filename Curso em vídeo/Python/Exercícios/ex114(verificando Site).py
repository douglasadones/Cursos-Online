# Crie um código em python que teste se o site Pudim está acessível pelo computador usado.
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O Site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
