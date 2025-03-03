__author__ = "Omer"

import functools


def main():
   result = list(four_dividers(56))
   print (result)


def four_dividers(number):
    return (filter(is_divided_by_4, range(1, number + 1)))

def is_divided_by_4(num_to_check):
    if(num_to_check % 4 == 0):
        return True
    return False

if __name__ == "__main__":
    main()