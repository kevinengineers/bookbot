def word_count(book_string):
    words = book_string.split()
    count = 0

    for word in words:
        count += 1


    return count

def char_count(book_str):
    chars = { }

    for c in list(book_str):
        lowered_c = c.lower()

        if lowered_c in chars:
            chars[lowered_c] += 1
        else:
            chars[lowered_c] = 1

    return chars


def sort_on(single_dict):
   return single_dict["num"]


def sort_dict(dict):

    list_of_dicts = list()

    for key, value in dict.items():
        list_of_dicts.append({"char": key, "num": value})

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

