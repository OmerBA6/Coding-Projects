

def main():
  print (my_mp3_playlist("songs.txt"))


def my_mp3_playlist(file_path):
    input_file = open(file_path, 'r')

    list_of_songs_dict = []

    for line in input_file: 
        temp_dict = {} 
        splitted_row = line.split(';')
        temp_dict["name"] = splitted_row[0]
        temp_dict["performer"] = splitted_row[1]
        temp_dict["time"] = splitted_row[2]    
        list_of_songs_dict.append(temp_dict)

    input_file.close()

    list_to_return = ["", 0, ""]
    for song_dict in list_of_songs_dict:
        song_minutes_time = int(song_dict["time"].split(':')[0])
        if (song_minutes_time > list_to_return[1]):
            list_to_return[0] = song_dict["name"]
            list_to_return[1] = song_minutes_time
    
    list_of_performers = []
    for song_dict in list_of_songs_dict:
        list_of_performers.append(song_dict["performer"])

    for performer in list_of_performers:
        if(list_of_performers.count(performer) >= list_of_performers.count(list_to_return[2])):
            list_to_return[2] = performer
            

    return tuple(list_to_return)
    

if __name__ == "__main__":
    main()