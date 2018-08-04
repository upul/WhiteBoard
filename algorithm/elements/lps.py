def lps(input):
    def _helper(start, end):
        if (start, end) in cache:
            return cache[(start, end)]

        if input == '':
            return ''

        if start == end:
            return input[start]

        if (start + 1) == end and input[start] == input[end]:
            return input[start:end + 1]

        if input[start] == input[end]:
            result = _helper(start+1, end-1)
            cache[(start+1, end-1)] = result

            if (end - start - 1) == len(result):
                return input[start] + result + input[end]
            else:
                result

        left = _helper(start, end-1)
        right = _helper(start+1, end)
        cache[(start, end-1)] = left
        cache[(start+1, end)] = right
        return left if len(left) > len(right) else right

    cache = {}
    return _helper(0, len(input)-1)


def lps_iter(input):
    if input == '':
        return ''
        
    cache = [[0]*len(input) for i in range(len(input))]
    
    for step in range(len(input)):
        for i in range(len(input)-step):
            j = i + step
            if i == j:
                cache[i][j] = input[i]
            elif i + 1 == j and input[i] == input[j]:
                cache[i][j] = input[i:j+1]
            elif input[i] == input[j]:
                middle = cache[i+1][j-1]
                if len(middle) == j - i - 1:
                    cache[i][j] = input[i] + cache[i+1][j-1] + input[j]
                else:
                    large = cache[i][j-1] if len(cache[i][j-1]) > len(cache[i+1][j]) else cache[i+1][j]
                    cache[i][j] = large
            else:
                #print(i, j)
                cache[i][j] = cache[i+1][j] \
                if len(cache[i+1][j]) > len(cache[i][j-1]) \
                else cache[i][j-1]
    
    #for i in range(len(cache)):
        #print(cache[i])

    return cache[0][len(input)-1]


if __name__ == '__main__':
    assert lps_iter('abcda') == 'b'
    assert lps_iter("babad") == 'bab'

    str = 'a'
    assert lps_iter(str) == 'a'

    str = 'aa'
    assert lps_iter(str) == 'aa'

    str = 'ab'
    assert lps_iter(str) == 'a'

    str = 'abc'
    assert lps_iter(str) == 'a'

    str = 'aabac'
    assert lps_iter(str) == 'aba'

    str = 'abapqrqpr'
    assert lps_iter(str) == 'pqrqp'

    print(lps_iter("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))
