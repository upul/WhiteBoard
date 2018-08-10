def num_ways(number):
    assert number >= 0    
    if number <= 2:
        return number
    return num_ways(number-1) + num_ways(number-2)

def num_ways_iter(number):
    cache = [0 for _ in range(number+1)]
    for i in range(number+1):
        if i == 0 or i == 1 or i == 2:
            cache[i] = i
        else:
            cache[i] = cache[i-2] + cache[i-1]
    return cache[number]


if __name__ == '__main__':
    assert num_ways_iter(3) == 3
    assert num_ways_iter(4) == 5
    assert num_ways_iter(500) 