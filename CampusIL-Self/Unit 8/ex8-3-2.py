


def main():

    my_dict = {"first_name":"Maria", "last_name":"Carey", "birth_date":"27.03.1970", "hobbies":["Sing", "Compose", "Act"]}
    user_action = input("Enter a command: ")

    if(user_action == '1'):
        print(my_dict["first_name"])
    elif(user_action == '2'):
        print((my_dict["birth_date"][3:5]))
    elif(user_action == '3'):
        for hobby in my_dict["hobbies"]:
            print (hobby)
    elif(user_action == '5'):
        print (my_dict["hobbies"][-1])
    elif(user_action == '6'):
        age_tuple = (my_dict["birth_date"][0:2], my_dict["birth_date"][3:5], my_dict["birth_date"][6:])
        print (age_tuple)
    elif(user_action == '7'):
        print (2022 - int(my_dict["birth_date"][6:]))







if __name__ == "__main__":
    main()