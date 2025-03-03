


def main():
    animal1 = animal("Octavio")
    animal2 = animal("ABCD", 7)
    animal1.birthday()
    
    print (animal1.get_age())
    print (animal2.get_age())


class animal():

    def __init__(self, name = "Octavio", age = 0):
        self._name = name
        self._age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    




if __name__ == "__main__":
    main()