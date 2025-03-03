
def main():
    print(shift_left([0, 1, 2]))




def shift_left(my_list):
    """
    This function shifts a list to the left.

    :param my_list: The list to shift.
    :type my_list: list.

    :return: The list shifted to the left.
    :rtype: list.
    """
    my_list.append(my_list.pop(0))
    return my_list



if __name__ == "__main__":
    main()