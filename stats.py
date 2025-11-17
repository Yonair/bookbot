def get_num_words(text):
    words = text.split()
    return len(words)


def get_count_characters(text):
    counts = {}
    
    
    for ch in text:
        ch = ch.lower()
    
    
        if ch in counts:
            counts[ch] += 1
    
    
        else:
            counts[ch] = 1
    
    return counts

def sort_on(character):
    return character["num"]

def get_sorted_char_counts_list(counts):
    char = []
    for count, num in counts.items():
        if count.isalpha():
            alpha = {"char": count, "num": num}
            char.append(alpha)
    char.sort(reverse=True, key=sort_on)
    return char
    