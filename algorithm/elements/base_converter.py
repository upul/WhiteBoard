import functools
import string


def _to_10(number, base):
    """
    """
    return functools.reduce(lambda result, c: result*base + string.hexdigits.index(c), number, 0)


def _from_10_recursive(number, res, base):
    """
    """
    if number == 0:
        return res[::-1]
    res += (string.hexdigits[number % base].upper())
    return _from_10_recursive(number // base, res, base)

# def _from_10(number, base):
#     """
#     """
#     result = ''
#     while True:
#         result += string.hexdigits[number % base].upper()
#         number = number // base
#         if number == 0:
#             break
#     return result[::-1]


def base_converter(number, src_base, dest_base):
    return _from_10_recursive(_to_10(number, src_base), '', dest_base)
     


if __name__ == '__main__':
    assert base_converter('111', 2, 10) == '7'
    assert base_converter('ff1', 16, 10) == '4081'
    assert base_converter('1000100001111', 2, 16) == '110F'
    print('Test Passed!')
