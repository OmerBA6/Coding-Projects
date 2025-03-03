__author__ = "Omer"


import functools



def main():
    print(is_prime(42))
    print(is_prime(43))



def is_prime(num):
    """
    This function return if a number is prime or not

    :param num: the number check
    :type num: int

    :return: True if the number is prime, false otherwise
    :rtype: boolean
    """

    #boolean reduce is being applied to a list the finds the num dividers
    return not(functools.reduce(lambda x ,y: x or y, [(num % x == 0) for x in range(2 ,num)]))
 
    
        


if __name__ == "__main__":
    main()