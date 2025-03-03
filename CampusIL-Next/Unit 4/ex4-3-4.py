
from math import sqrt
import numbers


def main():
    fibo = get_fibo()
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))
    print(next(fibo))
    

def get_fibo():
    x = 0
    y = 1 
    yield x
    yield y
    
    while(True):
        next = x + y
        yield next
        x = y
        y = next
    

if __name__ == "__main__":
    main()

