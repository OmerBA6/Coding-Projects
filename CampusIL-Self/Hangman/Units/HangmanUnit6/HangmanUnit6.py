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
    print(try_update_letter_guessed(guessed_letter, ['a', 'p', 'c', 'f']))




def is_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the giving string is a single English alphabetic letter.
    
    :Param letter_guessed: the string to check
    :param old_letters_guessed: list of already guessed letters
    :Type letter_guessed: string
    :type old_letters_guessed: list

    :return: False if the string is not a single alphabetic letter, True if it is
    :rtype: boolean
    """
    if(len(letter_guessed) != 1 and letter_guessed.isalpha()): #Check if the string is more than one letter and only alphabetic letters
        print("E1")
        return False
    elif(len(letter_guessed) != 1 and not letter_guessed.isalpha()): #Check if the string is more than one letter and not only alphabetic letters
        print("E3")
        return False
    elif(len(letter_guessed) == 1 and not letter_guessed.isalpha()): #check if the string is one letter not alphabetic
        print("E2")
        return False
    elif letter_guessed in old_letters_guessed:
        print("You already guessed this letter!")
        return False
    else: #if the string is one alphabetic letter
        print (letter_guessed)
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """his function checks if the guessed string is valid if so it adds it to the list of guessed letters.
    
    :Param letter_guessed: the string to check
    :param old_letters_guessed: list of already guessed letters
    :Type letter_guessed: string
    :type old_letters_guessed: list

    :return: False if the string is not valid or already have been guessed , True if the letter is valid and added to the list successfully.
    :rtype: boolean
    """
    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        old_letters_guessed_str = ' -> '
        old_letters_guessed.sort()
        old_letters_guessed_str = old_letters_guessed_str.join(old_letters_guessed)
        print("X\n" + old_letters_guessed_str)
        return False




if __name__ == "__main__":
    main()

