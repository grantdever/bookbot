from stats import get_num_words, count_chars, sorted_char_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text():
    with open(book, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents
text = get_book_text()
counted_chars = count_chars(text)
sorted_chars = sorted_char_count(counted_chars)

def print_report(sorted_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at "+ book +".")
    print("----------- Word Count ----------")
    print("Found " + str(get_num_words(text)) + " total words")
    print("----------- Character Count ----------")
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

def main():
    print_report(sorted_chars)


if __name__ == "__main__":
    main()
