
import HangmanLib 


def main():
    HangmanLib.print_open_screen() #print opening screen
    words_file_path = "words.txt" #############
    secret_word = HangmanLib.choose_word(words_file_path, HangmanLib.get_word_index()) #Get the secret word from file
    num_of_guesses = 0
    old_letters_guessed = []

    print ("\nLet's Begin!\n")
    HangmanLib.print_hangman(num_of_guesses) #print the first stage of the Hangman

    #THE GAME LOOP, as long the player not won or has guesses left
    while (not(HangmanLib.check_win(secret_word, old_letters_guessed))) and (num_of_guesses < 6):

        print(HangmanLib.show_hidden_word(secret_word, old_letters_guessed))

        user_guess = input("Guess a letter: ")
        response_code = HangmanLib.try_update_letter_guessed(user_guess.lower(), old_letters_guessed, secret_word) #check if user input is valid


        if (response_code[0]): #if letter is valid
            if(response_code[1] == HangmanLib.FAILED_GUESS): #if its a failed guess
                print (":(")
                num_of_guesses +=1
                HangmanLib.print_hangman(num_of_guesses)
        else: #if letter is not valid
            HangmanLib.print_guessed_letters(old_letters_guessed)



    if(HangmanLib.check_win(secret_word, old_letters_guessed)):
        print(HangmanLib.show_hidden_word(secret_word, old_letters_guessed))
        print("WON")
    else:
        print(HangmanLib.show_hidden_word(secret_word, old_letters_guessed))
        print("LOSE")
    
    






if __name__ == "__main__":
    main()