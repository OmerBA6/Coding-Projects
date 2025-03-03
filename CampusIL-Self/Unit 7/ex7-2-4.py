
def main():
    print(seven_boom(77))




def seven_boom(end_number):
    list_to_return = []
    for i in range(end_number + 1):
        if i % 7 == 0:
            list_to_return.append("boom")
        elif '7' in str(i):
            list_to_return.append("boom")
        else:
            list_to_return.append(i)
    
    return[list_to_return]



if __name__ == "__main__":
    main()