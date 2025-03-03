
def main():
    print(format_list(['av', 'bsa', 'vsdv', 'dsvsdv', 'asfsf', 'asfsf', 'asfasf']))




def format_list(my_list):
    str_to_return = ', '
    str_to_return = str_to_return.join(my_list[:len(my_list) -2:2])
    str_to_return += " and " + my_list[len(my_list) - 1]
    return str_to_return



if __name__ == "__main__":
    main()