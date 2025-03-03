HANGMAN_ASCII_ART = r""" #Game Opening art
Welcome to the game Hangman

| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/""" + "\n"

MAX_TRIES = 6


def main():
    print(HANGMAN_ASCII_ART)#prints the opening game ascii art
    print("You have " + str(MAX_TRIES) + " attempts!")
    word_to_guess = input("Please enter a word: ")
    print("_ " * len(word_to_guess) + "\n")


    guessed_letter = input("Guess a letter: ")
    print(is_valid_input(guessed_letter))




def is_valid_input(user_input):
    """
    This function checks if the giving string is a single English alphabetic letter.
    
    :Param user_input: the string to check
    :Type user_input: string

    :return: False if the string is not a single alphabetic letter, True if it is
    :rtype: boolean
    """
    if(len(user_input) != 1 and user_input.isalpha()): #Check if the string is more than one letter and only alphabetic letters
        print("E1")
        return False
    elif(len(user_input) != 1 and not user_input.isalpha()): #Check if the string is more than one letter and not only alphabetic letters
        print("E3")
        return False
    elif(len(user_input) == 1 and not user_input.isalpha()): #check if the string is one letter not alphabetic
        print("E2")
        return False
    else: #if the string is one alphabetic letter
        print (user_input)
        return True




if __name__ == "__main__":
    main()

