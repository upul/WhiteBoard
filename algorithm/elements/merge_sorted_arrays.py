import heapq

def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_index = heapq.heappop(min_heap)
        result.append(smallest_entry)
        smallest_iter = sorted_arrays_iters[smallest_index]
        next_element = next(smallest_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_index))
    
    return result



if __name__ == '__main__':
    array_1 = [0, 2, 4, 10, 29]
    array_2 = [0, 10, 20, 21, 30]
    array_3 = [10, 21, 31, 100, 500]

    print(merge_sorted_arrays([array_1, array_2, array_3]))