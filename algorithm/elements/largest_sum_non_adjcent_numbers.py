def largest_sum_non_adj_numbers(A):
    def helper(i, array_len):
        if i == array_len - 1:
            return A[i]
        if i + 1 == array_len - 1:
            return max(A[i], A[i+1])

        right = 0
        if (i + 2) <= array_len - 1:
            right = helper(i+2, array_len)

        return max(A[i] + right, A[i])

    global_max = 0
    for i in range(len(A)):
        if i < 2:
            global_max = max(helper(i, len(A)), global_max)
        else:
            global_max = max(helper(i, len(A)), global_max)

    return global_max


if __name__ == '__main__':
    assert largest_sum_non_adj_numbers([2, 4, 6, 2, 5]) == 13
    assert largest_sum_non_adj_numbers([5, 1, 1, 5]) == 10
