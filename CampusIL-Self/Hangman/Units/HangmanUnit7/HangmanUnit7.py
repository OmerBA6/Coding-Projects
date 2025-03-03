




def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
    
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))


def show_hidden_word(secret_word, old_letters_guessed):
    str_to_return = ""

    for ch in secret_word:
        if (ch in old_letters_guessed):
            str_to_return += ch + " "
        else:
            str_to_return += "_ "
    
    return str_to_return

def check_win(secret_word, old_letters_guessed):
    counter_to_win = len(secret_word)
    counter = 0

    for ch in secret_word:
        if (ch in old_letters_guessed):
            counter += 1
    
    return counter == counter_to_win

if __name__ == "__main__":
    main()