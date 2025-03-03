


def main():
    read_file("ab.txt")
    read_file("abc.txt")


def read_file(file_name):

    print ("__CONTENT_START__")
    try:
        f = open(file_name)
    except:
        print("__NO_SUCH_FILE__")
    else:
        for line in f:
            print (line)
        f.close()
    finally:
        print ("__CONTENT_END__")



if __name__ == "__main__":
    main()