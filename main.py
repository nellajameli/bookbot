import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    word_count = get_num_words(text)
    char_count = get_num_char(text)
    sorted_chars = chars_dict_to_sorted_list(char_count)
    print_stats(word_count, sorted_chars)

def get_book_path(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(number):
    words = number.split()
    return len(words)

def get_num_char(chars):
    letters_dict = {}
    lower_chars = chars.lower()
    words = []
    for letter in lower_chars:
        if letter in string.ascii_letters:
            words.append(letter)
    for letter in words:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_stats(words, characters):
    print("--- Begin report of books/frankenstein.txt ---")
    nl = '\n'
    print(f'{words} words are in the novel Frankenstein.{nl}')
    for item in characters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print(f'{nl}--- End report ---')

main()