__author__ = " Omer"


import functools

def main():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))



def intersection(list1, list2):
    """
    This function receives 2 lists and return a list of all shared values (no duplicates)

    :param list1: first list
    :param list2: second list
    :type list1: list
    :type list2: list 

    :return: list of shared values
    :rtype: list
    """
    return list(set([item1 for item1 in list1 if item1 in list2])) #set() is being used because it does'nt allow duplicate values
 
    
        


if __name__ == "__main__":
    main()