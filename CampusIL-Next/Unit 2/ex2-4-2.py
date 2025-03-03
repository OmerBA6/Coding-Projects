


def main():
    pass


class BigThing():

    def __init__(self, var):
        self._var = var

    def size(self):
        if (type(self._var) == int or type(self._var) == float):
            return self._var
        else:
            return len(self._var)


class BigCat(BigThing):

    def __init__(self, name, weight):
        self._name = name
        self._weight = weight
    
    def size(self):
        if(self._weight > 20):
            print("Very Fat")
        elif(self._weight > 15):
            print("Fat")
        else:
            print("Ok")
        
    
    


    

    




if __name__ == "__main__":
    main()