# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# for (key, value) in student_dict.items():


import pandas as pd


def make_phonetic():
    user_input = input("Type a name: ").upper()
    try:
        phonetic_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        make_phonetic()
    else:
        print(phonetic_list)


data = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

make_phonetic()

