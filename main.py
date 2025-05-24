from stats import word_count, char

def some_func(something):
    for item in somethign:
def get_book_text(filepath):

    with open(filepath, 'r') as file:
        return file.read()

def main():

    words = word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{words} words found in the document")

main()
