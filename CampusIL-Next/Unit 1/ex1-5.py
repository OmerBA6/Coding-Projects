
import functools
from operator import index
import string
from tkinter.font import names

def main():
    file_path = "names.txt"
    #print (longest_name(file_path))
    #print (total_length_of_names(file_path))
    #print (names_length_to_new_file(file_path))
    print (names_length_x(file_path))


def longest_name(file_path):
    """
    This function returns the longest name of a given file

    :param file_path: path of the file to open
    :type file_path: string

    :return: The longest name in the file
    :rtype: string
    """
    my_file = open(file_path, 'r')

    names_list = [name.strip() for name in my_file] #create a list of every line (list creation by loop)
    my_file.close()

     #get the longest name with lambada function the that compares lengths
    return (functools.reduce(lambda x,y: x if len(x) > len(y) else y, names_list))

    


def total_length_of_names(file_path):
    """
    This function returns the total lengths of the lines in file

    :param file_path: path of the file to open
    :type file_path: string

    :return: Total lengths of lines in file
    :rtype: int
    """
    my_file = open(file_path, 'r')

    #strip() to get rid of \n in line
    names_list = [len(name.strip()) for name in my_file] #create a list of every line (list creation by loop)
    my_file.close()
    
    #reduce() is applied on a list of the lines lengths and adds them up with lambada
    return (functools.reduce(lambda x,y: x + y, names_list)) 


def shortest_names(file_path):
    """
    This function returns the shortest lines in a file

    :param file_path: path of the file to open
    :type file_path: string

    :return: A string contains all the shortest line in a file
    :rtype: string
    """
    my_file = open(file_path, 'r')

    #strip() to get rid of \n in line
    names_list = [name.strip() for name in my_file] #create a list of every line (list creation by loop)
    my_file.close()

    #gets the shortest line length
    length_shortest_name = (functools.reduce(lambda x,y: x if x < y else y, [len(name) for name in names_list]))

    #create a new list of the shortest lines by comparing the line length with length_shortest_name
    shortest_names_list = [name for name in names_list if len(name) == length_shortest_name]

    #create a string from the shortest line list
    return (functools.reduce(lambda x,y: x + "\n" + y, shortest_names_list))



def names_length_to_new_file(file_path):
    """
    This function writes the length of every line in a given file to a new file

    :param file_path: path of the file to open
    :type file_path: string
    """

    names_file = open(file_path, 'r')
    names_length_file = open('name_length.txt' , 'w')

    #create a list of every line (list creation by loop)
    #strip() to get rid of \n in line
    names_list = [name.strip() for name in names_file]

    names_file.close()

    #turn the lines list to a list containing the lines lengths with map() and lambda
    names_list = list(map(lambda x: len(x), names_list))

    #write a string created with reduce() from the lines lengths list
    names_length_file.write(functools.reduce(lambda x,y: str(x) + "\n" + str(y), names_list))
    names_length_file.close()
    

def names_length_x(file_path):
    """
    This function returns the names that their lengths equals to the input number

    :param file_path: path of the file to open
    :type file_path: string

    :return: A string contains all the names with equal length to the user input
    :rtype: string
    """
    names_file = open(file_path, 'r')

    length = int(input("Enter name length: "))

    #create a list of every line (list creation by loop) that the her length is equal to user's input
    #strip() to get rid of \n in line
    names_list = [name.strip() for name in names_file if len(name.strip()) == length]
    names_file.close()
    
    #reduce() is applied to create a string from the list
    return (functools.reduce(lambda x,y: x + "\n" + y, names_list))




if __name__ == "__main__":
    main()