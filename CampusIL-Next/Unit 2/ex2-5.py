


from sqlite3 import DatabaseError


def main():
    zoo_lst = []
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky", 0))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))

    for animal in zoo_lst:
        print (animal)
        while animal.is_hungry():
            animal.feed()


class Animal():

    def __init__(self, name, hunger = 0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        return bool(self._hunger)

    def feed(self):
        self._hunger -= 1
    


class Dog(Animal):

    def __str__(self):
        return ("Dog {}".format(self._name))



class Cat(Animal):
    
    def __str__(self):
        return ("Cat {}".format(self._name))



class Skunk(Animal):
    
    def __str__(self):
        return ("Skunk {}".format(self._name))



class Unicorn(Animal):

    def __str__(self):
        return ("Unicorn {}".format(self._name))



class Dragon(Animal):
    
    def __str__(self):
        return ("Dragon {}".format(self._name))
    
    


    

    




if __name__ == "__main__":
    main()