
def main():
    print(sequence_del("Heeyyy   yyouuuuyyy!!!"))



def sequence_del(my_str):
    string_to_return = ""
    
    for i in range(len(my_str) - 1):
        if((my_str[i] not in string_to_return) or my_str[i] != string_to_return[-1]):
            string_to_return += my_str[i]
    return string_to_return

        




if __name__ == "__main__":
    main()