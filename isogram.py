from collections import Counter

ASCII_LOWER_BOUND = 97
ASCII_UPPER_BOUND = 123

def is_isogram(string):
    char_counts = Counter(string.lower())
    return all(
        char_counts[char] == 1 
        for char in char_counts 
        if ord(char) in range(ASCII_LOWER_BOUND, ASCII_UPPER_BOUND + 1)
        )
