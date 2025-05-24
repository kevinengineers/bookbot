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

