
from math import sqrt
import numbers


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))
    

def parse_ranges(ranges_string):
    number_ranges = (i.split("-") for i in ranges_string.split(",")) 
    return (num for start, stop in number_ranges for num in range(int(start), int(stop) + 1))
    

if __name__ == "__main__":
    main()

