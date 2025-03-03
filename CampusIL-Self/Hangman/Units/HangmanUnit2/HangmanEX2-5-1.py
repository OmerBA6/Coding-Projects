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