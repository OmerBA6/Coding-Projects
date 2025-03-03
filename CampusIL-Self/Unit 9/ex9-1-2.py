

from csv import list_dialects


def main():
    #file_path = input("Enter a file path: ")
    file_path = r"/Users/omerbenaderet/Desktop/Python/self/Unit 9 /text1.txt"
    user_command = input("Enter a command: ")

    while (not check_user_command_valid(user_command) or user_command != "exit"):
        if(user_command == 'sort'):
            print(sort_file(file_path))
        elif(user_command == "rev"):
            print_rev_lines(file_path)
        elif(user_command == "last"):
            n = int(input("Enter the number of lines you want to print: "))
            print_last_lines(file_path, n)
        elif(user_command == "exit"):
            break
        else:
            print("You entered illegal command!")
        user_command = input("Enter a command: ")
        

def sort_file(file_path):
    sorted_text_to_return = []
    input_file = open(file_path, 'r')
    for line in input_file:
        for word in line.split():
            if not(word in sorted_text_to_return):      
                sorted_text_to_return.append(word)

    input_file.close()
    return (sorted(sorted_text_to_return))


def print_rev_lines(file_path):
    input_file = open(file_path, 'r')
    input_file_lines_reversed = []

    for line in input_file:
        print("".join(reversed(line.rstrip('\n'))))#input_file_lines_reversed.append("".join(reversed(line.rstrip('\n'))))

    input_file.close()


def print_last_lines(file_path, n):
    input_file = open(file_path, 'r')
    input_file_lines = []

    for line in input_file:
        input_file_lines.append(line.rstrip())

    print (input_file_lines[-1:len(input_file_lines) - n - 1:-1])

    input_file.close()

def check_user_command_valid(user_command):
    if not(user_command == "sort" or user_command == "rev" or user_command == "last"):
        return False
    return True

if __name__ == "__main__":
    main()