
def _is_alpha(c):
    return c >= 'a' and c <= 'z'

def _is_alpha_dot(c):
    return c >= 'a' and c <= 'z' or c == '.'

def _is_alpha_zero_more(p):
    assert len(p) == 2
    return _is_alpha(p[0]) and p[1] == '*'

def _is_dot_zero_more(p):
    assert len(p) == 2
    return p[0] == '.' and p[1] == '*'

def is_match(data, pattern, last=''):
    data_size = len(data)
    pattern_size = len(pattern)
    if data_size == 0 and pattern_size == 0:
        return True
    if data_size == 0 and pattern_size == 2 and  _is_alpha_zero_more(pattern):
        return True
    if data_size == 0 and pattern_size == 2 and  _is_dot_zero_more(pattern):
        return True

    if data_size > 0 and pattern_size == 0:
        return False
    if data_size == 0 and len(pattern) > 0 and len(last) == 0:        
        return False
    
    assert data_size > 0
    assert pattern_size > 0
       
    if (data[0] == pattern[0]) and (len(pattern) > 1) and (pattern[1] == '*'):
        last += data[0]
        return is_match(data[1:], pattern, last)
    elif (pattern[0] == '.') and (len(pattern) > 1) and (pattern[1] == '*'):
        return is_match(data[1:], pattern)
    elif (data[0] != pattern[0]) and (len(pattern) > 1) and (pattern[1] == '*'):
        if len(pattern) > 2 and pattern[0] == pattern[2]:
            return is_match(pattern[2] + data, pattern[2:])
        else:
            return is_match(data, pattern[2:])    
    elif pattern[0] == '.':
        return is_match(data[1:], pattern[1:])
    elif data[0] == pattern[0] :
        return is_match(data[1:], pattern[1:])
    

if __name__ == '__main__':
    assert is_match('a', 'a') == True
    assert is_match('aa', 'aa') == True
    assert is_match('ab', 'a') == False

    assert is_match('ab', '..') == True
    assert is_match('aab', 'a.b') == True

    assert is_match('aa', 'a*') == True
    assert is_match('ab', 'a*b') == True
    assert is_match('abr', 'a*b.') == True
    assert is_match('ab', 'a*b.') == False

    assert is_match("a", ".*..a*") == False

    assert is_match('mississippi', 'mis*is*p*.') == False
    assert is_match('mississippi', 'mis*is*ip*.') == True
    assert is_match('mississippi', 'mis*is*ip*i*') == True

    assert is_match("a", ".*aa.*") == False
    assert is_match("", ".*") == True
    assert is_match('ab', '.*') == True

    assert is_match('aab', 'c*a*b') == True

    assert is_match('aaa', 'a*a') == True

    print('Test Passed!')
    