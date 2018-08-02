def num_messages(encoded):
    """
    TODO: Use Dynamic Programming....
    """
    num_to_alpha = [str(i) for i in range(1, 27)]

    def _is_valid(x):
        return x in num_to_alpha

    if len(encoded) <= 1 and (_is_valid(encoded) or encoded == ''):
        return 1

    left = num_messages(encoded[1:]) if _is_valid(encoded[0]) else 0
    right = num_messages(encoded[2:]) if _is_valid(encoded[0:2]) else 0
    return left + right


if __name__ == '__main__':
    encoded_message = '01'
    assert num_messages(encoded_message) == 0
