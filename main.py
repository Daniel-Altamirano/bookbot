import sys
from stats import *


def main():

    if len(sys.argv) < 2:
        print("Missing relative path to book.\nUsage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    user_input_path = sys.argv[1]
    text = get_book_text(user_input_path)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    list_of_char_and_num = create_sorted_list_of_dicts_with_char_and_num(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {user_input_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list_of_char_and_num:
        char = dict["char"]
        if not char.isalpha():
            continue
        num = dict["num"]
        print(f"{char}: {num}")

if __name__ == "__main__":
    main()