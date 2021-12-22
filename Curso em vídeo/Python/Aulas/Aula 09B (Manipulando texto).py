frase = 'Curso em Vídeo Python'
print(frase[12]) #mostra o caractere da posição 12
print(frase.count('o')) #conta quantos 'o' existem na frase
print(frase.upper().count('O')) #números de o maiúsculo (após por todos os caracteres em maiúsculo
print(len(frase)) #número de caracteres na frase
print(len(frase.strip())) #exclui os espaços inúteis
print(frase.replace('Python', 'Android')) #Troca a primeira palavra pela segunda
print('Curso' in frase) #Verifica se a palavra 'Curso' está dentro da frase (retorna True ou False)
print(frase.find('Curso')) #Mostra em que posição começa a palavra 'Curso'. (se o resultado foir '-1' é pq n existe.
print(frase.lower()) #tudo em minúsculo
print(frase.upper()) #Tudo em maiúsculo
print(frase.capitalize()) #Primeiro caractere em maiúsculo
print(frase.title()) #Cada palavra começando em maiúsculo
print(frase.split()) #Divide as palavras e cria uma lista.
dividido = frase.split()
print(dividido[0]) #Escolhi uma das palavras da lista para ser impressa.
print(dividido[2][3]) #"pegue o dividido 2 e me mostre o caractere 3" (lembra que o .split() zera os microespaços a cada divisão)
print('-'.join(frase)) #Você pode escolher algum caractere para separar as letras.
