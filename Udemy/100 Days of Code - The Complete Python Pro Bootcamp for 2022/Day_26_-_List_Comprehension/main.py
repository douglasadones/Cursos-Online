# Compreensão de lista
numers = [1, 2, 3]
new_numbers = [n + 1 for n in numers]  # Irá preencher esta lista com 2, 3, 4.
print(new_numbers)
name = "Angela"
letter_list = [letter for letter in name]  # Irá preencher a lista com as letras da string "name"
print(letter_list)
range_list = [n*2 for n in range(1, 5)]  # Irá preencher a lista com 1, 2, 3, 4.
print(range_list)


# Compreensão de lista com condição
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]  # Preencherá apénas com nomes de até 4 letras
print(short_names)
long_names = [name.upper() for name in names if len(name) > 4]  # Preencherá com a forma maiúscula dos nomes com 5 letras ou mais.
print(long_names)


# Lista com apenas os números pares
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)


# Criando uma lista "result" que contém os elementos que estão simultaneamente em file1.txt e file2.txt
with open("file1.txt") as file1:
    num_in_file1 = file1.readlines()
with open("file1.txt") as file1:
    num_in_file2 = file1.readlines()
result = [int(num) for num in num_in_file1 if num in num_in_file2]
print(result)

# OBS: O "\n" Não conta como uma string, logo, int(num) funciona.
