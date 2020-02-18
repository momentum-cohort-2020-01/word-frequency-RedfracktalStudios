# test = ["apples", "pear", "grapes", "banana"]
# for fruit in test:
#     print("my fav fruit " + fruit)
#     print(len(fruit) + )


def main():
  # opens file in read/text mode
    f = open('emancipation_proclamation.txt', 'r')
    # checks if the file is open; if yes we proceed
    if f.mode == 'r':
        # reads and stores it as variable content
        contents = f.read()
        # print(contents)
        print(len(contents))


# prints to console
# if __name__ == "__main__":
#     main()
