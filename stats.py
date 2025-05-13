def num_words(text):
    words = text.split()
    count = len(words)
    return count

def num_letters(text):
    counter = {}
    for char in text.lower():
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter

def report(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append({"char": char, "num": count})
    def sort_by_count(item):
        return item["num"]
    char_list.sort(reverse=True, key=sort_by_count)
    return char_list