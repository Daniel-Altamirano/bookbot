from stats import get_num_words
from stats import get_book_text
from stats import get_char_counts

def main():
    path_frankenstein = "books/frankenstein.txt"
    text = get_book_text(path_frankenstein)
    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    print(f"{num_words} words found in the document")
    print(char_counts)

if __name__ == "__main__":
    main()