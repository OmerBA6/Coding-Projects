


def main():

    ch = input("Enter a letter:")
    max_length_int = 0

    while (not is_ch_valid(ch)):
        print("Input not Valid! You must type only one letter!")
        ch = input("Enter a letter: ")
    
    max_length_str = input("Enter the max length: ")
    while (not is_max_length_valid(max_length_str)):
        print("You must enter a int number!")
        max_length_str = input("Enter a new number: ")

    max_length_int = int(max_length_str)
    print(arrow(ch, max_length_int))


def is_ch_valid(user_ch):
    return (len(user_ch) == 1)

def is_max_length_valid(max_legth_str):
    for ch in max_legth_str:
        if not(ch.isnumeric()):
            return False
    return True

def arrow(ch, max_length):
    arrow_str = ""
    for i in range(max_length + 1):
        arrow_str += ((ch + " ") * i) + "\n"

    for j in range(max_length - 1, 0, -1):
        arrow_str += ((ch + " ") * j) + "\n"
    
    return arrow_str


if __name__ == "__main__":
    main()