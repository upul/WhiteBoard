def odd_even(A):
    """
    
    """
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


if __name__ == '__main__':
    a = [1, 0, 2, 3, 4, 7, 16]
    odd_even(a)
    print(a)
