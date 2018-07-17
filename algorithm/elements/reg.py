
def is_match(data, pattern, last_match=''):
    # if len(data) == 0 and len(pattern) == 0:
    #     return True
    # if len(data) == 0 and pattern == '.*':
    #     return True
    # if len(data) == 0 and len(pattern) >= 2 and (pattern[0] >= 'a' and pattern[0] <= 'z') and pattern[1] == '*':
    #     return  is_match('', pattern[2:], pattern[0])
    # if len(data) == 0 and len(pattern) > 0:
    #     if last_match == pattern[0]:
    #         return True
    #     else:
    #         return False

    # if len(data) > 0 and len(pattern) == 0:
    #     return False
    
    # if len(data) > 0 and len(pattern) == 0:
    #     return False
    # if len(data) == 0 and len(pattern) == 1:
    #     return False
    # if len(data) == 0 and len(pattern) >= 2 and (pattern[0] >= 'a' and pattern[0] <= 'z') and pattern[1] == '*':
    #     return is_match('', '')
    # if len(data) == 0 and not (len(pattern) == 2 and ( ((pattern[0] >= 'a' and pattern[0] <= 'z') or pattern[0] == '.') and pattern[1] == '*')):
    #     return False    

    # char = data[0]
    # if len(pattern) >= 2 and (pattern[0] >= 'a' and pattern[0] <= 'z') and pattern[1] == '*':
    #     return is_match(data[1:], pattern, pattern[0])
    # if char == pattern[0]:
    #     return is_match(data[1:], pattern[1:])
    # if pattern[0] == '.':
    #     return is_match(data[1:], pattern[1:])
        
    # return False 

    

if __name__ == '__main__':
    assert is_match('aa', 'aa') == True
    assert is_match('ab', 'ab') == True
    assert is_match('ab', 'abb') == False

    assert is_match('a', '.') == True
    assert is_match('ab', '..') == True
    assert is_match('ab', '.') == False

    assert is_match('aa', 'a*') == True
    assert is_match('aaa', 'a*a') == True
    assert is_match('aaa', 'ab*a*c*a') == True

    assert is_match('mississippi', 'mis*is*p*') == True
    assert is_match('aab', 'c*a*b') == True

    assert is_match("a", ".*..a*") == False
    assert is_match("aa", "a") == False

    assert is_match("a", ".*aa.*") == False
    assert is_match("", ".*") == True
    assert is_match('ab', '.*') == True
    print('Test Passed!')