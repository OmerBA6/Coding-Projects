

from csv import list_dialects


def main():
   print(who_is_missing("findme.txt"))




def who_is_missing(file_path):
    file_to_search = open(file_path, 'r')
    list_of_numbers = file_to_search.read().split(',')
    file_to_search.close()
    list_of_numbers.sort()
    missing_numbers = []

    for i in range(0,len(list_of_numbers)):
        list_of_numbers[i] = int(list_of_numbers[i])

    for ele in range(list_of_numbers[0], list_of_numbers[-1] + 1):
        if ele not in list_of_numbers:
            missing_numbers.append(ele)

    founded_file = open("found.txt", 'w')
    for missed_number in missing_numbers:
        founded_file.write(str(missed_number) + ', ')

    founded_file.close()

    return missing_numbers


if __name__ == "__main__":
    main()