import itertools

def find_max_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

if __name__ == '__main__':
    A = [-1, 12, -1, 10, 1, -3, 1]
    print(find_max_subarray(A))