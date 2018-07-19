def contiguous_area_largest_sum(A):
    local_sum = global_sum = 0
    for i in range(len(A)):
        local_sum += A[i]
        if local_sum < 0:
            local_sum = 0
        if local_sum > global_sum:
            global_sum = local_sum
    return global_sum

if __name__ == '__main__':
    A = [1, 2, -7, 5, 12, -2, 1]
    assert contiguous_area_largest_sum(A) == 17

    A = [50, 2, -7, 25, 12, -50, 1]
    assert contiguous_area_largest_sum(A) == 82

    print('Test Passed!')
