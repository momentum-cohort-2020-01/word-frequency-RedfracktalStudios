# # STOP_WORDS = [
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
#     'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
#     'will', 'with'
# ]


def findreplace(char, string):
    place = string.index(char)
    string['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
           'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
           'will', 'with'] = ''
    return string

    def main():
        # opens file in read/text mode
        f = open('emancipation_proclamation.txt', 'rt')
        # checks if the file is open; if yes we proceed
        if f.mode == 'rt':
            # reads and stores it as variable content
            contents = f.read()
