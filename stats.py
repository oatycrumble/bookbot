def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars_dict = {}
    chars_lowered = str.lower(text)
    for c in chars_lowered:
        if c.isalpha():
            if c in chars_dict:
                chars_dict[c] += 1
            else:
                chars_dict[c] = 1
    return chars_dict

def sort_on(dict):
    return dict["count"]

def get_sorted_list(chars_dict):
    sorted_list = []
    for c in chars_dict:
        sorted_list.append({"char": c, "count": chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
