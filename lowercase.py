# def main():
#      with open('emancipation_proclamation.txt', 'r') as reader:
#           open_file = file.read()
#           print(string.lower())
#       print(open_file)


def main():
  # opens file in read/text mode
    f = open('emancipation_proclamation.txt', 'rt')
    # checks if the file is open; if yes we proceed
    if f.mode == 'rt':
        # reads and stores it as variable content
        contents = f.read()
        # print(contents)
        print(contents.lower())


# prints to console
if __name__ == "__main__":
    main()
