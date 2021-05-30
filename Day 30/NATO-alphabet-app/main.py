from os import path, sys
import pandas

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv(path.join(sys.path[0],"nato_phonetic_alphabet.csv"))
nato_dict = {value.letter:value.code for (key,value) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()