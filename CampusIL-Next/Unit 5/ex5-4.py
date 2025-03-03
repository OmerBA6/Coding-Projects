__author__ = "Omer"


TOP_LIMIT_ID_NUMBER = 1000000000
BOTTOM_LIMIT_ID_NUMBER = 100000000
MULTIPLAYER_FOR_EVEN_INDEX = 2
ID_NUMBER_LENGTH = 9


ID_INPUT_CODE = 1
IT_OR_GEN_INPUT_CODE = 2
YES_OR_NO_INPUT_CODE = 3
HOW_MANY_INPUT_CODE = 4


def main():

    another_id_maker = ""
    while(another_id_maker != "No"): #Main program loop
        id_maker = () #Defining a variable that would be the iterator or generator
        
        id_input = input("Enter ID: ")
        while (True): #loop to get a valid ID number
            try:
                check_if_user_input_is_valid(id_input, ID_INPUT_CODE)
            except Exception as e:
                print (e)
                id_input = input("Enter ID: ")
                continue
            else:
                break

        it_or_gen_input = input("Generator or Iterator? (gen/it)? ")
        while(True): #loop to get a valid "gen" or "it" input
            try:
                check_if_user_input_is_valid(it_or_gen_input, IT_OR_GEN_INPUT_CODE)
            except Exception as e:
                print (e)
                it_or_gen_input = input("Generator or Iterator? (gen/it)? ")
                continue
            else: #if input is valid, Create Iterator or Generator by the input
                if (it_or_gen_input == "it"):
                    id_maker = IDiterator(int(id_input))
                elif(it_or_gen_input == "gen"):
                    id_maker = id_generator(int(id_input))
                break
        

        how_many_input = input("Enter How many ID numbers do you want: ")
        more_same_id = ""
        try: #to catch StopIteration Exception if needed
            while(more_same_id != "No"): #Loop to work with the ID that was given
                while(True): #loop to get valid number input
                    try:
                        check_if_user_input_is_valid(how_many_input, HOW_MANY_INPUT_CODE)
                    except Exception as e:
                        print (e)
                        how_many_input = input("How many ID numbers do you want? ")
                        continue
                    else: #if a number was entered, Produce from iterator\generator how_many_input ID numbers
                        for i in range(int(how_many_input)):
                            if (it_or_gen_input == "it"):
                                print(next(id_maker))
                            elif(it_or_gen_input == "gen"):
                                print(next(id_maker))
                                
                        break
                
                more_same_id = input("Do you want more <Yes\\No>? ")
                while(True): #loop to get valid "Yes" or "No" input
                    try:
                        check_if_user_input_is_valid(more_same_id, YES_OR_NO_INPUT_CODE)
                    except Exception as e:
                        print (e)
                        more_same_id = input("Do you want more <Yes\\No>? ")
                        continue
                    else:
                        if(more_same_id == "Yes"):
                            how_many_input = input("How many ID numbers do you want? ")
                        break
        except StopIteration: #if reached to StopIteration from current ID
            print("No more ID numbers can be produced from current ID!")

        

        another_id_maker = input("Do you want to produce more ID numbers from a different ID <Yes\\No>? ")
        while(True): #loop to get valid "Yes" or "No" input
            try:
                check_if_user_input_is_valid(another_id_maker, YES_OR_NO_INPUT_CODE)
            except Exception as e:
                print (e)
                another_id_maker = input("Do you want to produce more ID numbers from a different ID <Yes\\No>? ")
                continue
            else:
                break
        





def check_if_user_input_is_valid(user_input, input_code):
    """
    This function checks if user_input is valid, depends on input_code and raise Exceptions if not

    :param user_input: user's input
    :param input_code: a number representing what the user input should be
    :type user_input: str
    :type input_code: int

    :return: None
    :rtype: None
    """
    if(input_code == ID_INPUT_CODE): #In case user is input is ID number
        if (len(user_input) != ID_NUMBER_LENGTH): #if input not in length - Length = ID_NUMBER_LENGTH = 9
            raise IdNotInLength(user_input)
        else: 
            for ch in user_input: #check if ID numbers contain characters that are not numbers
                if not(ch.isnumeric()):
                    raise IdContainIllegalCharacter(user_input) 
        if (int(user_input) < BOTTOM_LIMIT_ID_NUMBER): #If the input ID is under the BOTTOM_LIMIT_ID_NUMBER = 100000000
            raise IdNotInRange(user_input)
    
    elif(input_code == IT_OR_GEN_INPUT_CODE): #In case user input should be "it" or "gen"
        if (user_input != "it" and user_input != "gen"):
            raise ItOrGenException(user_input)

    elif(input_code == YES_OR_NO_INPUT_CODE): #In case user input should be "Yes" or "No"
        if (user_input != "Yes" and user_input != "No"):
            raise YesOrNoException(user_input)

    elif(input_code == HOW_MANY_INPUT_CODE): #In case user input should be a number
        try: #Check if input is a number by trying to int()
            int(user_input)
        except:
            raise NotNumber(user_input)




class IdNotInLength(Exception):
    """
    This class is an represent Exception 
    """
    def __str__(self):
        return ("IDError: ID number not in correct length!")

class IdContainIllegalCharacter(Exception):
    """
    This class is an represent Exception
    """
    def __str__(self):
        return ("IDError: ID number contain illegal character (Must be only numbers)!")

class IdNotInRange(Exception):
    """
    This class is an represent Exception
    """
    def __str__(self):
        return ("IDError: ID number must be over 100000000")

class ItOrGenException(Exception):
    """
    This class is an represent Exception
    """
    def __str__(self):
        return ("InputError: You must enter \'\'it\'\' or \'\'gen\'\'>!")

class YesOrNoException(Exception):
    """
    This class is an represent Exception
    """
    def __str__(self):
        return ("InputError: You must enter \'\'Yes\'\' or \'\'No\'\')!")

class NotNumber(Exception):
    """
    This class is an represent Exception
    """
    def __str__(self):
        return ("InputError: You must enter a number!")






def id_generator(id_number):
    """
    This function is a generator function that produce ID numbers

    :param id_number: The ID number to start from
    :type id_number: int

    :return: ID numbers generator
    :rtype: generator
    """
    for possible_id_number in range(id_number + 1, TOP_LIMIT_ID_NUMBER):
        if(check_id_valid(possible_id_number)):
            yield possible_id_number
    raise StopIteration


class IDiterator():
    """
    This class is an id numbers iterator
    """
    def __init__(self, id):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        for possible_id_number in range(self._id + 1, TOP_LIMIT_ID_NUMBER):
            if(check_id_valid(possible_id_number)):
                self._id = possible_id_number
                return self._id
        
        raise StopIteration





def check_id_valid(id_number):
    """
    This function gets a number representing an id number and returns if he is valid or not
    Valid id number is a number that after calculations on the number digits the result needs to be able to divide by 10

    :param id_number: The number representing the id number
    :type index_and_value: int

    :return: True if the id number is valid, False otherwise
    :rtype: bool
    """

    #sum() is being applied on iterable object from map
    #map() is applied on iterable object from enumerate
    #enumerate() is a applied on str(id_number)
    return (sum(map(multiply_by_index, enumerate(str(id_number)))) % 10 == 0)



def multiply_by_index(index_and_value):
    """
    This function gets a tuple (index, value) and return the value itself if the index is odd,
    or the sum of the digits after multiplying the value by 2 if the index is even

    :param index_and_value: Tuple representing index and value
    :type index_and_value: Tuple

    :return: The value it self if index is odd, Sum of digits after multiplying by 2 if index is even 
    :rtype: int
    """
    idx, digit = index_and_value #idx gets the first value in the tuple, digit the second

    if((idx + 1) % 2 == 0):
        return add_digits(int(digit) * MULTIPLAYER_FOR_EVEN_INDEX)
    else:
        return int(digit)



def add_digits(number):
    """
    This function returns the sum of digits of the giving number

    :param number: The number to calculate his digits
    :type number: int

    :return: Sum of digits of param num
    :rtype: int
    """
    return sum([int(digit) for digit in str(number)])#sum() on the list of digits from number //int not iterable, str is 



if __name__ == "__main__":
    main()