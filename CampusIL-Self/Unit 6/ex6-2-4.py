
def main():
    print(extend_list([4,5,6],[1,2,3]))
    print([1,2,3] + [4,5,6])



def extend_list(list_x, list_y):
    joined_list = list_y

    for i in list_x:
        joined_list.append(i)

    return joined_list



if __name__ == "__main__":
    main()