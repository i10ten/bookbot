import sys
from stats import get_num_words, get_num_characters, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1] # "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for char in sort_chars(num_chars):
        if char["char"].isalpha():
            letter = char["char"]
            num = char["num"]
            print(f"{letter}: {num}")
    print("============= END ===============")

main()
