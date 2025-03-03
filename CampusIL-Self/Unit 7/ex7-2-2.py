
def main():
    print(numbers_letters_count("Python 3.6.3"))




def numbers_letters_count(my_str):
    num_of_numbers = 0
    for ch in my_str:
        if ch.isnumeric():
            num_of_numbers += 1
    
    return[num_of_numbers, len(my_str) - num_of_numbers]



if __name__ == "__main__":
    main()