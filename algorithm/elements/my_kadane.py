import itertools

def max_sum_subarray(A):
    max_so_far = 0
    max_ending_here = 0
    for element in A:
        max_ending_here = max_ending_here + element
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far

if __name__ == '__main__':
    A = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_sum_subarray(A))