def get_word_count(text):
    return len(text.split())

def get_letter_counts(text):
    word_counts = {}
    for c in text:
        if c.lower() in word_counts:
            word_counts[c.lower()] += 1
        else:
            word_counts[c.lower()] = 1
    return word_counts

def sort_on(d):
    return d["count"]

def sort_letter_counts(letter_count_dict):
    sorted_list = []
    for key in letter_count_dict:
        sorted_list.append({"letter": key, "count": letter_count_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list