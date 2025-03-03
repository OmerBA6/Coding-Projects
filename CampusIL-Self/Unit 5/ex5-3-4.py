
def last_early(my_str):
    """
    This function check if the last letter of a given is string also appears before in the same string

    :Param my_str: The string to check
    :Type my_str: string

    :return: True if the last letter of the string is also appears before false otherwise
    :rtype: bool
    """
    return my_str[-1] in my_str[0:len(my_str) - 1]

print (last_early(input("Enter a word: ")))
