import functools
import string


def int_to_string(x):
    """
    """
    is_negative = False
    if x < 0:
        is_negative, x = True, -x

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x = x // 10
        if x == 0:
            break
    return '-' if is_negative else '' + ''.join(reversed(s))


def str_to_int(x):
    # This can further simplified
    # using func tools

    is_negative = False
    if x[0] == '-':
        is_negative, x = True, x[1:]

    running_sum = string.digits.index(x[0])
    for c in x[1:]:
        running_sum = running_sum*10 + string.digits.index(c)

    return -1*running_sum if is_negative else running_sum

def str_to_int_compact(x):
    return functools.reduce(lambda res, c: res*10 + string.digits.index(c), x, 0)


if __name__ == '__main__':
    #print('type: {}, value: {}'.format(type(int_to_string(123)), int_to_string(123)))
    print(str_to_int('-123777'))
    print(str_to_int_compact("123777"))
