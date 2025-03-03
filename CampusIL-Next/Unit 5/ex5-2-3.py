__author__ = "Omer"

import itertools


def main():
    bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    option = set()

    for i in range(1, len(bills)):
        all_combinations = itertools.combinations(bills, i)
        for current_combination in all_combinations:
            if (sum(current_combination) == 100):
                option.add(current_combination)

    print (len(option))


if __name__ == "__main__":
    main()

