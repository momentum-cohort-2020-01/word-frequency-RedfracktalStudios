# load seneca_falls text file
import string
filename = 'emancipation_proclamation.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
# split the text file into words
words = text.split()
# remove punctuation
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table)for w in words]
print(stripped)

# def main():
#   # opens file in read/text mode
#     f = open('emancipation_proclamation.txt', 'rt')
#     # checks if the file is open; if yes we proceed
#     if f.mode == 'rt':
#         # reads and stores it as variable content
#         contents = f.read()
#         # print(contents)
#         print(contents.lower())


# # prints to console
# if __name__ == "__main__":
#     main()