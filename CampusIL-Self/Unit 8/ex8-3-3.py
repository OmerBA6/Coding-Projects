


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))
    




def count_chars(my_str):
    dict_to_return = dict()
    for ch in my_str:
        if (ch not in (dict_to_return.keys())) and (ch != ' '):
            dict_to_return[ch] = my_str.count(ch)

    return dict_to_return
if __name__ == "__main__":
    main()