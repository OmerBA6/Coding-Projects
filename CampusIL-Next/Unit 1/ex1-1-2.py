__author__ = "Omer"

import functools




def main():
   print(double_letter("python"))
   print(double_letter("we are the champions!"))



def double_letter(string):
    """
    This function gets a string and return the same string with every letter doubled

    :param string: The string to double
    :type string: string

    :return: The original string with every letter doubled 
    :rtype: string
    """
    return (functools.reduce(add_add, map(make_double, string)))
    
    
        
def make_double(ch):
    """
    This function gets a character and return the same one doubled

    :param ch: The ch to double
    :type ch: char

    :return: The character doubled
    :rtype: string
    """
    return ch*2


def add_add(ch1,ch2):
    """
    This function gets 2 strings and add them together

    :param ch1: The first string
    :param ch2: The second string
    :type ch1: string
    :type ch2: string

    :return: The strings together
    :rtype: string
    """
    return ch1 + ch2


if __name__ == "__main__":
    main()