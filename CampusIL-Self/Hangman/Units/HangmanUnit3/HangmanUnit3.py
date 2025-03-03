#Hangman Unit 2

HANGMAN_ASCII_ART = r"""
Welcome to the game Hangman

| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/""" + "\n"

MAX_TRIES = 6



print(HANGMAN_ASCII_ART)
print("You have " + str(MAX_TRIES) + " attempts!")
word_to_guess = input("Please enter a word: ")
word_to_guess_length = (len(word_to_guess))
print("_ " * word_to_guess_length)