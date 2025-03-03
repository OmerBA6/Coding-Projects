

from csv import list_dialects


def main():
   copy_file_content("/Users/omerbenaderet/Desktop/Python/self/Unit 9 /copy.txt", "1.txt")




def copy_file_content(source_path, destination_path):

    """
    source_file = open(source_path, 'r')
    destination_file = open(destination_path, 'w') 
    destination_file.write(source_file.read())
    source_file.close()
    destination_file.close() """


    """
    source_file = open(source_path, 'r')
    source_file_text = ""
    for line in source_file:
        source_file_text += line
    source_file.close()  
    destination_file = open(destination_path, 'w')
    destination_file.write(source_file_text)
    destination_file.close()"""
    pass

    
        


if __name__ == "__main__":
    main()