


def main():
    print(are_list_equal([0.6,1,2,3],[1,3,0.6,2]))



def are_list_equal(list1, list2):

    list1.sort()
    list2.sort()

    return (list1 == list2)



if __name__ == "__main__":
    main()