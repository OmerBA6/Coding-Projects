from  itertools import chain


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))




def sort_anagrams(list_of_strings):
    list_to_return = []
    for i in list_of_strings:
        temp_list = []
        for j in list_of_strings:
            if(j not in chain(*list_to_return) and are_string_anegrams(i, j)):
                temp_list.append(j)
        if not (len(temp_list) == 0):
            list_to_return.append(temp_list)
    
    return list_to_return

def are_string_anegrams(string1, string2):
    return (sorted(string1) == sorted(string2))


if __name__ == "__main__":
    main()