def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        if numbers[abs(numbers[i])] < 0:
            duplicates.append(abs(numbers[i]))
        else:
            numbers[abs(numbers[i])] = -1*numbers[abs(numbers[i])]
    return duplicates
    
if __name__ == '__main__':
    assert find_duplicates([]) == []
    assert find_duplicates([0]) == []
    assert find_duplicates([1, 0]) == []
    assert find_duplicates([0, 1, 1, 2]) == [1]
    assert find_duplicates([1, 2, 3, 1, 3, 6, 6]) == [1, 3, 6]