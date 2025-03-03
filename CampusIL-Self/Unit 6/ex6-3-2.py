


def main():
    print(longest(["av", "asfasf", "asfaf"]))



def longest(my_list):
    return (max(my_list, key=len))



if __name__ == "__main__":
    main()