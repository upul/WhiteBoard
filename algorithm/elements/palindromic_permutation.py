from collections import defaultdict
from collections import Counter

def can_form_palindrome(s):
    letters = defaultdict(int)
    for c in s:
        letters[c] += 1
    detect_single_char = False
    for k, v in letters.items():
        if v % 2 == 0:
            continue
        if v == 1 and not detect_single_char:
            detect_single_char = True
            continue
        return False
    return True

def can_form_palindrome_oneline(s):
    return sum([v % 2 for v in Counter(s).values()]) <= 1

if __name__ == '__main__':
    assert can_form_palindrome('edified') == True
    assert can_form_palindrome('ediffied') == True

    assert can_form_palindrome_oneline('edified') == True
    assert can_form_palindrome_oneline('ediffied') == True
        