from os import path, sys
import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv(path.join(sys.path[0],"nato_phonetic_alphabet.csv"))
# for (key,value) in nato_df.iterrows():
#     print(value.code)
nato_dict = {value.letter:value.code for (key,value) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
result = [nato_dict[letter] for letter in user_word]
print(result)