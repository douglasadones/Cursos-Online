#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Programa Principal
# O objetivo desse projeto é gerar um convite para cada nome inserido em "invited_names.txt"
PLACEHOLDER = "[name]"

# Criando lista com os nomes contidos em "invited_names.txt" :
with open("Input/Names/invited_names.txt") as file_name:
    name_list = file_name.read().strip().split("\n")

# Criando um convite (tendo como modelo "starting_letter") para cada nome da lista.
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in name_list:
        stripped_name = name.strip()
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_letter:
            new_letter.write(letter.replace(PLACEHOLDER, stripped_name))
