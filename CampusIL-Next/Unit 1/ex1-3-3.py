
import functools
from operator import index
import string



def main():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    print(decode(password))


def decode(password):

    #reduce() on a list of character
    #map() makes the int list to characters
    #map() makes the given string to a int list of the ascii value of each letter
    return functools.reduce(lambda x,y: x + y,list(map(lambda x: chr(x) if x != ' ' else x,(list(map(lambda x: ord(x) + 2 if x != " " else x, list(password)))))))
    
    
        


if __name__ == "__main__":
    main()