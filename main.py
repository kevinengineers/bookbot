from stats import word_count, char_count, sort_dict
import sys

def get_book_text(filepath):

    with open(filepath, 'r') as file:
        return file.read()


def pretty_print_dict(list_of_dicts):

    for i in range(0, len(list_of_dicts)):
        if list_of_dicts[i]["char"].isalpha():
            print(f"{list_of_dicts[i]["char"]}: {list_of_dicts[i]["num"]}")


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_str = get_book_text(sys.argv[1])
        num_of_words = word_count(book_str)
        dict_of_words = char_count(book_str)
        char_list = sort_dict(dict_of_words)
        book = "./books/frankenstein.txt"
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}")
        print("------------ Word Count ------------")
        print(f"Found { num_of_words } total words")
        print("--------- Character Count -------")
        pretty_print_dict(char_list)    
        print("============= END ===============")

main()
