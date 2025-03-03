


def main():
    data = ("self", "py", 1.543)
    format_string = "Hello {0}.{1} learner, you have only {2:.1f} units left before you master the course!".format(data[0], data[1], data[2])
    print (format_string)
    

if __name__ == "__main__":
    main()