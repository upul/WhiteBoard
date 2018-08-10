def find_contiguous_sub_array(array, expected_sum):
    i, cct_sum, cct_index = 0, 0, 0

    while cct_index <= i:
        cct_sum += array[i]
        if cct_sum == expected_sum:
            return [cct_index, i]
        elif cct_sum > expected_sum:
            cct_sum -= array[cct_index]
            cct_index += 1

        if i < len(array):
            i += 1
    return []


if __name__ == '__main__':
    print(find_contiguous_sub_array([9, 5, 5, 1, 3], 6))
