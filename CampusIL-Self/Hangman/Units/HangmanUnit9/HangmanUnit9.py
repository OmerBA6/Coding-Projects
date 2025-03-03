

def main():
  print (choose_word("words.txt", 39))


def choose_word(file_path, index):
    list_to_return = [0, ""]
    words_file = open(file_path, 'r')
    all_words = words_file.read().split()
    words_file.close()
    num_of_all_words = len(all_words)

    if(index > len(all_words)):
        list_to_return[1] = all_words[(index % num_of_all_words) - 1]
    else:
        list_to_return[1] = all_words[index - 1]
        
    words_no_doubles = []
    for word in all_words:
        if word not in words_no_doubles:
            words_no_doubles.append(word)

    list_to_return[0] = len(words_no_doubles)
    
    return tuple(list_to_return)

if __name__ == "__main__":
    main()