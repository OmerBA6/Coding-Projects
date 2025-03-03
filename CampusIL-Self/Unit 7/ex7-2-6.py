


MAIN_MENU = """
0 - Print main menu.
1 - Print all the shopping list.
2 - Print the number of products in the shopping list.
3 - Is the product is in the list <input>.
4 - How many times a product is in the list <input>.
5 - Delete a product <input>.
6 - Add a product <input>
7 - Print all illegal products.
8 - Remove Every double product.
9 - Exit
"""


def main():

    #shopping_list_str =  input("Enter your shopping list: ")
    #shopping_list_list = string_to_list_converter(shopping_list_str)

    shopping_list_list = ["Milk" , "ad", "$asfsd", "Beer", "#", "Bread", "Beer"]

    print(MAIN_MENU)
    user_command = input("Enter a command: ")

    while((not is_input_valid(user_command)) or (user_command != '9')):
        if(user_command == '0'):
            print(MAIN_MENU + "\n")
        elif(user_command == '1'):
            print_list(shopping_list_list)
        elif(user_command == '2'):
            print("The number of products is: " + str(len(shopping_list_list)))
        elif(user_command == '3'):
            product_to_check = input("Enter a product: ")
            print(is_a_product_in_the_list(product_to_check, shopping_list_list))
        elif(user_command == '4'):
            product_to_check = input("Enter a product: ")
            print ("The products appear " + how_many_times(product_to_check, shopping_list_list) + " times!")
        elif(user_command == '5'):
            product_to_delete = input("Enter a product: ")
            shopping_list_list.remove(product_to_delete)
        elif(user_command == '6'):
            product_to_add = input("Enter a product: ")
            shopping_list_list.append(product_to_add)
        elif(user_command == '7'):
            for product in shopping_list_list:
                if not(check_product_validity(product)):
                    print (product)
        elif(user_command == '8'):
            remove_all_doubles(shopping_list_list)
        
        user_command = input("Enter a command: ")
    
    print("Thank You!")



    



def is_input_valid(user_input):
    """
    This function checks if the user's input is valid.
    valid input is a number between 1-9.

    :param user_input: user's input.
    :type user_input: string

    :return: false is the input is not valid, True if it is valid.
    :rtype: boolean
    """
    if((len(user_input) != 1) or not (user_input.isnumeric())):
        print("Wrong input!")
        return False
    return True


def string_to_list_converter(my_str):
    my_list = my_str.split(',')
    return my_list


def print_list(shopping_list):
    for product in shopping_list:
        print (product)

def is_a_product_in_the_list(product, shopping_list):
    return (product in shopping_list)

def how_many_times(product, shopping_list):
    counter = 0
    for item in shopping_list:
        if item == product:
            counter += 1
    
    return str(counter)

def check_product_validity(product):
    if (len(product) < 3):
        return False
    for ch in product:
        if not ch.isalpha():
            return False
    
    return True

def remove_all_doubles(shopping_list):
    for product in shopping_list:
        counter = int(how_many_times(product, shopping_list))
        if(counter > 1):
            for i in range(counter - 1):
                shopping_list.remove(product)
    
if __name__ == "__main__":
    main()