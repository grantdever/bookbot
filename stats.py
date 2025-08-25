def get_num_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(items):
    return items[1]

def sorted_char_count(char_count):
    sorted_char_count = sorted(char_count.items(), key=sort_on, reverse = True)
    return sorted_char_count
