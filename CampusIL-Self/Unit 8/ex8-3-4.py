


def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))
    




def inverse_dict(my_dict):
    dict_to_return = {}

    for key1  in my_dict.keys():
        temp_list = []
        for key2 in my_dict.keys():
            if (my_dict[key1] == my_dict[key2]) and not (check_if_in_dict(my_dict[key2], dict_to_return)):
                temp_list.append(key2)
        dict_to_return[my_dict[key1]] = temp_list

    for key3 in dict_to_return.keys():
        dict_to_return[key3] = sorted(dict_to_return[key3])

    return dict_to_return

        
def check_if_in_dict(value, dict1):
    for key1 in dict1.keys():
        if value in list(dict1[key1]):
            return True
    return False




if __name__ == "__main__":
    main()