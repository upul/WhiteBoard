def knapsack(weights, values, capacity):

    def _helper(current_capacity, index):
        if index == 0 or current_capacity == 0:
            return 0

        if (current_capacity, index) in cache:
            return cache[(current_capacity, index)]

        if capacity < weights[index]:
            cache[(current_capacity, index - 1)
                  ] = _helper(current_capacity, index - 1)
            return cache[(current_capacity, index - 1)]

        cache[(current_capacity - weights[index-1], index-1)] = _helper(current_capacity - weights[index-1], index-1)
        cache[(current_capacity, index-1)] = _helper(current_capacity, index-1)
        return max(cache[(current_capacity - weights[index-1], index-1)] + values[index],
                   cache[(current_capacity, index-1)])

    cache = {}
    return _helper(capacity, len(weights)-1)


if __name__ == '__main__':
    values = [60, 100, 120, 1000]
    weights = [10, 20, 30, 51]
    capacity = 50
    assert knapsack(weights, values, capacity) == 220
