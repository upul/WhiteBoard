from collections import defaultdict


def first_non_repeating_char(string):
    char_map = defaultdict(int)
    for c in string:
        char_map[c] += 1

    for key in char_map.keys():
        if char_map[key] == 1:
            return key
    return None

if __name__ == '__main__':
    assert first_non_repeating_char('GeeksforGeeks') == 'f' 
    assert first_non_repeating_char('GeeksQuiz') == 'G' 
    assert first_non_repeating_char('abcCde') == 'a'
    assert first_non_repeating_char('aaaa') == None 
