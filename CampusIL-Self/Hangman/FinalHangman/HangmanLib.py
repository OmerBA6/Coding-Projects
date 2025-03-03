


HANGMAN_ASCII_ART = r""" #Game Opening art
Welcome to the game Hangman!
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/""" + "\n"

MAX_TRIES = 6

HANGMAN_PHOTOS = {1:r"""    
                x-------x

    """, 2:r""" 
                x-------x
                |
                |
                |
                |       
                |
    """, 3:r""" 
                x-------x
                |       |
                |       0
                |
                |
                |
   """, 4:r"""     
                x-------x
                |       |
                |       0
                |       |
                |   
                |


    """, 5:r"""     
                x-------x
                |       |
                |       0
                |      /|\
                |
                |

    """, 6:r"""     
                x-------x
                |       |
                |       0
                |      /|\
                |      /
                |

    """, 7:r"""     
                x-------x
                |       |
                |       0
                |      /|\
                |      / \
                |

    """}

FAILED_GUESS = 1   
ILLEGAL_GUESS = 2
SUCCESSFUL_GUESS = 3

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the giving string is a single English alphabetic letter.
    
    :Param letter_guessed: the string to check
    :param old_letters_guessed: list of already guessed letters
    :Type letter_guessed: string
    :type old_letters_guessed: list

    :return: False if the string is not a single alphabetic letter, True if it is
    :rtype: boolean
    """
    if((len(letter_guessed) != 1) or not (letter_guessed.isalpha()) or (letter_guessed in old_letters_guessed)):
        return False
    else:
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """his function checks if the guessed string is valid if so it adds it to the list of guessed letters.
    
    :Param letter_guessed: the string to check
    :param old_letters_guessed: list of already guessed letters
    :Type letter_guessed: string
    :type old_letters_guessed: list

    :return: False if the string is not valid or already have been guessed , True if the letter is valid and added to the list successfully.
    :rtype: boolean
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        if(letter_guessed not in secret_word):
            old_letters_guessed.append(letter_guessed)
            return (True, FAILED_GUESS)
        else:
            old_letters_guessed.append(letter_guessed)
            return (True, SUCCESSFUL_GUESS)
        
    else:
        return (False, ILLEGAL_GUESS)


def show_hidden_word(secret_word, old_letters_guessed):
    """This function return a string that present the player his progression in the game.
    
    :Param secret_word: the word the player is trying to guess
    :param old_letters_guessed: list of already guessed letters
    :Type letter_guessed: string
    :type old_letters_guessed: list

    :return: a string presentation of the player progression in guessing the word.
    :rtype: string
    """
    str_to_return = ""

    for ch in secret_word:
        if (ch in old_letters_guessed):
            str_to_return += ch + " "
        else:
            str_to_return += "_ "
    
    return str_to_return

def check_win(secret_word, old_letters_guessed):
    """This function return if the player guessed the entire word.
    
    :Param secret_word: the word the player is trying to guess
    :param old_letters_guessed: list of already guessed letters
    :Type letter_guessed: string
    :type old_letters_guessed: list

    :return: True if the player guessed the word false otherwise.
    :rtype: bool
    """
    counter_to_win = len(secret_word)
    counter = 0

    for ch in secret_word:
        if (ch in old_letters_guessed):
            counter += 1
    
    return counter == counter_to_win


def print_hangman(num_of_tries):
    """This function prints the current status of the Hangman in the game.
    
    :Param num_of_tries: number of the player guesses
    :Type num_of_tries: int

    """
    print(HANGMAN_PHOTOS[num_of_tries + 1])


def choose_word(file_path, index):
    """This function picks the word to guess.
    
    :Param file_path: words file path
    :param index: the player random number
    :Type file_path: string
    :type index: int

    :return: the word to guess.
    :rtype: string
    """
    words_file = open(file_path, 'r')
    all_words = words_file.read().split()
    words_file.close()
    num_of_all_words = len(all_words)

    if(index > len(all_words)):
        return all_words[(index % num_of_all_words) - 1]
    else:
        return all_words[index - 1]


def print_open_screen():
    print(HANGMAN_ASCII_ART)#prints the opening game ascii art
    print("You have " + str(MAX_TRIES) + " attempts!")


def get_word_index():
    word_index_str = input("Choose a random number: ")

    while not check_index(word_index_str):
        print("You didn't entered a number!")
        word_index_str = input("Choose a random number: ")

    return int(word_index_str)


def check_index(index_str):
    for ch in index_str:
        if not ch.isnumeric():
            return False
    return True


def print_guessed_letters(old_letters_guessed):
    """This function prints the player's wrong guesses.
    
    :Param old_letters_guessed: list of already guessed letters
    :Type old_letters_guessed: list

    """
    old_letters_guessed_str = ' -> '
    old_letters_guessed.sort()
    old_letters_guessed_str = old_letters_guessed_str.join(old_letters_guessed)
    print("X")
    print(old_letters_guessed_str)
        