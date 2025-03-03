SIZE = 3  # Number of rows and columns
PLAYER_ONE_SIGN = 'X'
PLAYER_TWO_SIGN = 'O'


class GameBoard:

    def __init__(self):
        # Init func, creates a list of rows, row*SIZE, each row with SIZE items
        self.board = []
        for i in range(SIZE):
            row = [' ' for _ in range(SIZE)]
            self.board.append(row)
        self.iof = SIZE**2

    def print_board(self):
        # Prints board
        for i in range(SIZE):
            print(*self.board[i], sep=' | ')
            if i != SIZE - 1:
                print("---"*SIZE)

    def is_board_full(self):
        # Checks if board is full, return True if it is, False otherwise
        for row in self.board:
            for pos in row:
                if pos == ' ':
                    return False
        return True

    def update_board(self, player, pos):
        # Updates the board with the according player sign
        if player == 1:
            sign = PLAYER_ONE_SIGN
        else:
            sign = PLAYER_TWO_SIGN
        row, col = self.pos_to_row_col(int(pos) - 1)

        self.board[row][col] = sign

    def check_player_input(self, player_input):
        # Checks Player position input, return False if not, True otherwise
        if not player_input.isnumeric():
            # Checks if the input is a number
            print("Please enter a number!")
            return False
        elif int(player_input) > self.iof or int(player_input) < 1:
            # Checks of the input is in range
            print(f"Position out of range! Remember (1 to {self.iof})!")
            return False
        else:
            # Checks if position is already taken
            row, col = self.pos_to_row_col(int(player_input) - 1)
            # Sends -1 so that that input can start from 1,
            # so it is easier for the players
            if self.board[row][col] != ' ':
                print("Position already taken!")
                self.print_board()  # Prints the board so that the player can see the taken positions
                return False

        return True

    @staticmethod
    def pos_to_row_col(pos):
        # Gets the row and column from pos(User Input)
        row = pos // SIZE  # Gets the row number from the input (pos)
        col = pos % SIZE  # Gets the column number from the input (pos)

        return row, col

    def check_win(self):
        # Checks win
        # Checking method is, makes a string from list and checks if it is the same as 'X'*SIZE or 'O'*SIZE,
        # Does the same for all rows, columns and slants

        # Row Checking
        for row in self.board:
            row_str = ''.join(row)
            if row_str == 'X'*SIZE or row_str == 'O'*SIZE:
                return True

        # Columns Checking
        for i in range(SIZE):
            col = []
            for j in range(SIZE):
                col.append(self.board[j][i])
            col_str = ''.join(col)
            if col_str == 'X'*SIZE or col_str == 'O'*SIZE:
                return True

        # Slants Checking
        # First slant
        first_slant = [self.board[i][i] for i in range(SIZE)]
        first_slant_str = ''.join(first_slant)
        if first_slant_str == 'X' * SIZE or first_slant_str == 'O' * SIZE:
            return True

        # Second slant
        second_slant = [self.board[i][abs((i + 1) - SIZE)] for i in range(SIZE)]
        second_slant_str = ''.join(second_slant)
        if second_slant_str == 'X' * SIZE or second_slant_str == 'O' * SIZE:
            return True

        return False
