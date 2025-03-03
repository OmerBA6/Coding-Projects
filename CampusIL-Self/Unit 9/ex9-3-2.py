

def main():
  print (my_mp4_playlist("songs1.txt", "Python Love Story"))


def my_mp4_playlist(file_path, new_song):
    input_file = open(file_path, 'r+')
    input_file_lines = input_file.readlines()
    print (input_file_lines)
    input_file.close()

    num_of_lines = len(input_file_lines)
    if(num_of_lines < 3):
        for i in range(2 - num_of_lines):
            input_file_lines.append("\n")
        input_file_lines.append(new_song + "\n")
    else:
        input_file_lines[2] = new_song + ";" + input_file_lines[2].split(";")[1] + ";" + input_file_lines[2].split(";")[2] + ";\n"

    input_file = open(file_path, 'w')
    for line in input_file_lines:
        input_file.write(line)
    
    input_file.close()
        
    

if __name__ == "__main__":
    main()