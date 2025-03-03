#Hangman Unit 1

import random


print ("Welcome to the game Hangman\n")
print (r"""
Welcome to the game Hangman

| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/""")
print ("You have " + str(random.randint(5,10)) + " attempts!\n") 
