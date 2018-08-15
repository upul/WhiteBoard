import heapq

def merge_k_shorted_arrays(sorted_arrays):
    sorted_iters = [iter(x) for x in sorted_arrays]
    min_heap = []

    for i, it in enumerate(sorted_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    result = []
    while min_heap:
        smallest_value, smallest_index = heapq.heappop(min_heap)
        result.append(smallest_value)
        itr = sorted_iters[smallest_index]
        next_element = next(itr, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_index))
    return result

if __name__ == '__main__':
    array_1 = [0, 2, 4, 10, 29]
    array_2 = [0, 10, 20, 21, 30]
    array_3 = [10, 21, 31, 100, 500]

    print(merge_k_shorted_arrays([array_1, array_2, array_3]))