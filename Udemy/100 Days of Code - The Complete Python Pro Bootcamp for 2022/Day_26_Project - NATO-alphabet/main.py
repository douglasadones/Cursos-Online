import pandas

nato_phonectic = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in nato_phonectic.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").strip().upper()
nato_word = [phonetic_dict[letter] for letter in word]
print(nato_word)
