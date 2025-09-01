def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def get_num_words(string):
    split_string = string.split()

    return len(split_string)


def get_char_counts(string):
    string = string.lower()
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    
    return char_counts

