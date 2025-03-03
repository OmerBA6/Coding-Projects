


def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))
    
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))




def mult_tuple(tuple1, tuple2):
    tuple_to_return = ()

    for i in tuple1:
        for j in tuple2:
            temp_tuple = (i, j)
            tuple_to_return += (temp_tuple,)
            temp_tuple = (j, i)
            tuple_to_return += (temp_tuple,)
    
    return tuple_to_return

if __name__ == "__main__":
    main()