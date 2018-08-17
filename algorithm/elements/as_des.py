from collections import namedtuple
import heapq

assending, descending = range(2)
SubArrayData = namedtuple('SubArrayData', ('array', 'property'))


def chop_array(A):
    state = assending
    stopped_point = 0
    sorted_sub_arrays = []

    for i in range(1, len(A)):
        if (A[i-1] < A[i] and state == descending) or (A[i-1] > A[i] and state == assending):
            sorted_sub_arrays.append(SubArrayData(A[stopped_point:i], state))
            stopped_point = i
            state = assending if state == descending else descending

    sorted_sub_arrays.append(SubArrayData(A[stopped_point:], state))
    return sorted_sub_arrays


def merge(sorted_arrays):
    iters = [iter(x.array) if x.property == assending else reversed(x.array)
             for x in sorted_arrays]
    min_heap = []

    for i, itr in enumerate(iters):
        first_element = next(itr, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_value, value_index = heapq.heappop(min_heap)
        result.append(smallest_value)
        candidate_iter = iters[value_index]
        next_element = next(candidate_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, value_index))
    return result

def resort_assending_descending(array):
    chopped_sub_arrays = chop_array(array)
    return merge(chopped_sub_arrays)


if __name__ == '__main__':
    arr = [-10, 0, 20, 10, 8, 5, 10, 20, 35, 20, 10, -100]
    result = resort_assending_descending(arr)
    print('Test Passed')
