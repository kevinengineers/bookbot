from stats import word_count, char_count, sort_dict

def get_book_text(filepath):

    with open(filepath, 'r') as file:
        return file.read()


def pretty_print_dict(list_of_dicts):

    for i in range(0, len(list_of_dicts)):
        if list_of_dicts[i]["char"].isalpha():
            print(f"{list_of_dicts[i]["char"]}: {list_of_dicts[i]["num"]}")


def main():
    book_str = get_book_text("./books/frankenstein.txt")
    num_of_words = word_count(book_str)
    dict_of_words = char_count(book_str)
    char_list = sort_dict(dict_of_words)
    # words = word_count(get_book_text("./books/frankenstein.txt"))
    # print(f"{words} words found in the document")
    # print(char_count(get_book_text("./books/frankenstein.txt")))
    book = "./books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("------------ Word Count ------------")
    print(f"Found { num_of_words } total words")
    print("--------- Character Count -------")
    pretty_print_dict(char_list)    
#    for i in range(0, len(char_list)):
#        print(f"{char_list[i]}")
    print("============= END ===============")
main()
