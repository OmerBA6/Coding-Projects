
import functools


def main():
   print(sum_of_digits(1352323512))



def sum_of_digits(number):
    return (functools.reduce(add_numbers, str(number)))

def add_numbers(num_in_str1, num_in_str2):
    return int(num_in_str1) + int(num_in_str2)

if __name__ == "__main__":
    main()