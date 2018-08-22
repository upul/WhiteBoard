def max_sub_array(A, k=1):
    start = end = 0
    max_values = []
    for _ in range(len(A)):
        end += 1
        if (end - start) == k:
            max_values.append(max(A[start:end]))
            start += 1
    return max_values

if __name__ == '__main__':
    a =  [10, 5, 2, 7, 8, 7]
    print(max_sub_array(a, k=3))
