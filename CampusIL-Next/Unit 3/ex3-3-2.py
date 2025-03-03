


def main():
    send_invitation("Avi", 20)
    send_invitation("David", 17)



class UnderAge(Exception):

    def __init__(self, age):
        self._age = age
        
    def __str__(self):
        print("Sorry you are {0}. only 18+ people can be invited.\n But no worry just another {1} years and you would be invited".format(self._age, 18 - self._age))





def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAge(age)
    else:
        print("You should send an invite to " + name)

if __name__ == "__main__":
    main()