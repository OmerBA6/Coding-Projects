
from math import sqrt


def main():
    print (first_prime_over(100000))


def first_prime_over(n):
    prime_numbers = (num for num in range(n, n + 100) if is_prime(num))
    return (next(prime_numbers))

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()