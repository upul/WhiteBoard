import functools


def excel_cols(col):
    return functools.reduce(lambda result, c: result*26 + (ord(c) - ord('A') + 1), col, 0)


if __name__ == '__main__':
    assert excel_cols('A') == 1
    assert excel_cols('B') == 2
    assert excel_cols('Z') == 26

    assert excel_cols('AA') == 27
    assert excel_cols('AB') == 28
    print('Passed')
