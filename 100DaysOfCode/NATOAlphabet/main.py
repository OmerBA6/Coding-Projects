# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# for (key, value) in student_dict.items():


import pandas as pd
data = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Type a name: ").upper()
phonetic_list = [phonetic_dict[letter] for letter in user_input]
print(phonetic_list)
