

def main():
    print (are_files_equal(r"/Users/omerbenaderet/Desktop/Python/self/Unit 9 /text1.txt", r"/Users/omerbenaderet/Desktop/Python/self/Unit 9 /text3.txt"))
    

def are_files_equal(file1, file2):
    input_file1 = open(file1, 'r')
    input_file2 = open(file2, 'r')
    file1_lines = input_file1.readlines()
    file2_lines = input_file2.readlines()
    if file1_lines == file2_lines:
        return True
    else:
        return False
    input_file1.close()
    input_file2.close()



if __name__ == "__main__":
    main()