def find_main(A):
    low, heigh = 0, len(A) - 1

    while low <= heigh:
        mid = (low + heigh) // 2
        mid_plus = (mid + 1) % len(A)
        mid_minus = (mid - 1)

        if A[mid] < A[mid_minus] and A[mid] < A[mid_plus]:
            return A[mid]

        # Zero shifted array
        if A[mid] < A[heigh] and A[mid] > A[low]:
            return A[low]

        if A[mid] > A[heigh]:
            low = mid + 1
        elif A[mid] < A[low]:
            heigh = mid - 1


if __name__ == '__main__':
    # [1, 2, 3, 4, 5] => [4, 5, 1, 2, 3]
    assert find_main([4, 5, 1, 2, 3]) == 1

    # [1, 2, 3, 4, 5] => [5, 1, 2, 3, 4]
    assert find_main([5, 1, 2, 3, 4]) == 1

    # [1, 2, 3, 4, 5] => [2, 3, 4, 5, 1]
    assert find_main([2, 3, 4, 5, 1]) == 1

    # [1, 2, 3, 4, 5] => [1, 2, 3, 4, 5]
    assert find_main([1, 2, 3, 4, 5]) == 1
