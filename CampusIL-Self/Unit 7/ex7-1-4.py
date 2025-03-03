
def main():
    print(squared_numbers(-3, 3))




def squared_numbers(start, stop):
    squared_list = []
    while start <= stop:
        squared_list.append(start ** 2)
        start += 1
    return squared_list
    

if __name__ == "__main__":
    main()