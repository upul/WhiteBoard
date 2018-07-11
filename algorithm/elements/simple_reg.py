from enum import Enum


def match(regex, ss):

    def _match_exact(index, reg):
        if index >= len(ss):
            return index, False

        if index + len(reg) >= len(ss):
            return index, False

        return index+len(reg), ss[index: index + len(reg)] == reg
    # def _match_exact(i, val):
    #     #print(val)
    #     for v in val:
    #         if i < len(ss) and v == ss[i]:
    #             i += 1
    #         else:
    #             return i, False
    #     return i, True

    def _match_any_one(i, val, next):
        if next is not None and i < len(ss) and ss[i] == next[1][0]:                
                return i, False                

        if i < len(ss):
            i += 1
            return i, True
        else:
            return i, False

    def _match_any_zero_more(i, val, next):
        result = False
        #print(next)
        while i < len(ss):
            #print(i)
            if next is not None and ss[i] == next[1][0]:                
                return i, True                
            i, r = _match_any_one(i, val, next)
            result = result or r
            if not r:
                break
        return i, result
    
    def _match_given_zero_more(i, val, next):
        #result = True
        while i < len(ss):
            if ss[i] != val:
                break

            if next is not None and ss[i] == next[1][0]:
                return i, True
            i += 1
        return i, True

    # def _match_given_zero_more(i, val, next):
    #     result = False
    #     while i < len(ss):
    #         if next is not None and ss[i] == next[1][0]:                
    #             return i, True                
    #         i, r = _match_exact(i, val)
    #         result = result or r
    #         if not r:
    #             break
    #     return i, result

    i = 0
    result = False
    tokens = get_regex_tokens(regex)
    for t in range(len(tokens)):
        tok_type, val = tokens[t]
        # print(tok_type)
        if tok_type == RegState.EXACT:
            i, result = _match_exact(i, val)
        elif tok_type == RegState.ANY_ONE:
            i, result = _match_any_one(i, val, tokens[t +1] if t +1 < len(tokens) else None)
        elif tok_type == RegState.ANY_ZERO_MORE:
            i, result = _match_any_zero_more(i, val, tokens[t +1] if t+1 < len(tokens) else None)
        elif tok_type == RegState.GIVEN_ZERO_MORE:
            i, result = _match_given_zero_more(i, val, tokens[t+1] if t+1 < len(tokens) else None)
                   
        if not result:
            return False
    if i < len(ss):
        return False

    return result


class RegState(Enum):
    ANY_ONE = 1,
    GIVEN_ZERO_MORE = 2,
    ANY_ZERO_MORE = 3
    EXACT = 4


def get_regex_tokens(regex):
    if len(regex) == 1 and regex == '.':
        return [(RegState.ANY_ONE, '.')]
    if len(regex) == 1 and regex == '*':
        return [(RegState.ANY_ZERO_MORE, '*')]
    token = ''
    tokens = []
    for i in range(len(regex)):
        char = regex[i]
        if char >= 'a' and char <= 'z':
            if (i + 1) < len(regex) and regex[i+1] == '*' and len(token) > 0:
                tokens.append((RegState.EXACT, token))
                token = char
                i += 1
            elif (i + 1) < len(regex) and regex[i+1] == '.':
                token += char
                tokens.append((RegState.EXACT, token))
                token = ''
            else:
                token += char
        if char == '.':
            if (i + 1) < len(regex) and regex[i+1] == '*':
                token = char
                i += 1
            else:
                if len(token) > 0:
                    tokens.append((RegState.EXACT, token))
                else:
                    tokens.append((RegState.ANY_ONE, '.'))
                token = ''
        elif char == '*':
            if token == '.':
                tokens.append((RegState.ANY_ZERO_MORE, token))
            else:
                tokens.append((RegState.GIVEN_ZERO_MORE, token))
            token = ''
    if len(token) > 0:
        tokens.append((RegState.EXACT, token))
    return tokens


if __name__ == '__main__':
    print(get_regex_tokens('ab*'))
    print(match('ab*', 'ab'))
