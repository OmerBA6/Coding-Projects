
def main():
    print(is_greater([1, 30, 25, 60, 27, 28], 28))




def is_greater(my_list, n):
    list_to_return = []
    for i in my_list:
        if i > n:
            list_to_return.append(i)
    return list_to_return
    

if __name__ == "__main__":
    main()