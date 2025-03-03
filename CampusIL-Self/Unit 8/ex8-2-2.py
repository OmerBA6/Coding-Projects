


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))
    

def sort_prices(list_of_tuples):
    #list_of_tuples.sort(key=lambda y: y[1], reverse = True)
    #return sorted(list_of_tuples, key=lambda y: y[1], reverse = True)
    return sorted(list_of_tuples, key=get_the_price_from_the_tuple, reverse = True)

def get_the_price_from_the_tuple(my_tuple):
    return my_tuple[1]

if __name__ == "__main__":
    main()