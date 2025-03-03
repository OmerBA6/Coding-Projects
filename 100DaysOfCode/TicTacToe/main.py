from tictacto import GameBoard
from art import logo


def tictacto():
    game_board = GameBoard()  # Creates new tic tac to game board

    # Print welcome and logo
    print(logo)
    print("Welcome to Tic Tac To!")

    print(f"The board positions are numbered from 1 to {game_board.iof}.")  # Prints explanation
    game_board.print_board()  # Prints initial board

    while not game_board.is_board_full():  # Loops while the board is not full
        player_move = input("Player 1, where would you like to mark 'X'? ")
        while not game_board.check_player_input(player_move):  # Loops while the input is invalid
            player_move = input("Player 1, where would you like to mark 'X'? ")
        game_board.update_board(player=1, pos=player_move)
        game_board.print_board()  # Prints board after first player move
        if game_board.check_win():
            print("Player 1 wins!")
            break  # Breaks the game loop if player won

        if not game_board.is_board_full():  # Checks that the board is not full so the second player can play
            player_move = input("Player 2, where would you like to mark 'O'? ")
            while not game_board.check_player_input(player_move):  # Loops while input is invalid
                player_move = input("Player 2, where would you like to mark 'O'? ")
            game_board.update_board(player=2, pos=player_move)
            game_board.print_board()  # Prints board after second player move
            if game_board.check_win():
                print("Player 2 wins!")
                break  # Breaks the game loop if player won

    # If board is full, with no winner
    if game_board.is_board_full():
        print("It is a Draw!")

    # Play again option, Calls the function again if the user wants to play again
    play_again = input("Would you like to play again (y/n)? ")
    while play_again != 'y' and play_again != 'n':  # Loops while user input is not 'y' or 'n'
        print("Please enter a valid input (y/n)!")
        play_again = input("Would you like to play again (y/n)? ")

    if play_again == 'y':
        tictacto()


tictacto()
