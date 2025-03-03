
import string



def main():

    while(True):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        try:
            check_input(username, password)
        except Exception as e:
            print (e)
        else:
            break


def check_input(username, password):

    if (len(username) < 3):
        raise UsernameTooShort(username)
    elif (len(username) > 16):
        raise UsernameTooLong(username)
    else:
        for ch in username:
            if not(ch.isnumeric() or ch.isalpha() or ch == "_"):
                raise UsernameContainsIllegalCharacter(username, ch)

    if (len(password) < 8):
        raise PasswordTooShort(password)
    elif (len(password) > 40):
        raise PasswordTooLong(password)
    else:
        big_letter = False
        small_letter = False
        special_ch = False
        number_ch = False
        for ch in password:
            if (ch.isupper()):
                big_letter = True
            elif (ch.islower()):
                small_letter = True
            elif (ch.isnumeric()):
                number_ch = True
            elif (ch in string.punctuation):
                special_ch = True

        if not(big_letter):
            raise UppercaseMissing(password)
        elif not(small_letter):
            raise LowercaseMissing(password)
        elif not(number_ch):
            raise DigitMissing(password)
        elif not(special_ch):
            raise SpecialMissing(password)

            
    print ("OK")


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username, ch):
        self._username = username
        self._illegalch = ch

    def __str__(self):
        return ("Username contain illegal character. character \"{0}\" in position {1}".format(self._illegalch, self._username.find(self._illegalch) + 1))

class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return ("Username is too short! Must be at least 3 characters.")
class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return ("Username is too long! Must be 16 characters at max.")

class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return ("Password is too short! Must be at least 8 characters.")
class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return ("Password is too long! Must be 40 characters at max.")


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return ("Password is missing a character")

class UppercaseMissing(PasswordMissingCharacter):
    def __str__(self):
        return (super().__str__ ()+ " (Uppercase)")
class LowercaseMissing(PasswordMissingCharacter):
    def __str__(self):
        return (super().__str__ ()+ " (Lowercase)")
class DigitMissing(PasswordMissingCharacter):
    def __str__(self):
        return (super().__str__ ()+ " (Digit)")
class SpecialMissing(PasswordMissingCharacter):
    def __str__(self):
        return (super().__str__() + " (Special)")
    

if __name__ == "__main__":
    main()