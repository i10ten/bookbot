def get_num_words(text):
    return len(text.split())

def sort_on(items):
    return items["num"]

def sort_chars(dict_of_chars):
    list_of_chars = []
    for char in dict_of_chars:
        list_of_chars.append({"char": char, "num": dict_of_chars[char]})
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars

def get_num_characters(text):
    num_chars = {}
    for character in text.lower():
        if character not in num_chars:
            num_chars[character] = 1
        else:
            num_chars[character] += 1
    return num_chars
