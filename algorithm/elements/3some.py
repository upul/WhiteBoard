def three_some(arr):
    arr.sort()

    def two_number_to_given_sum(expected_sum, skip):
        i = skip + 1 if skip == 0 else 0
        j = len(arr) - 1
        result = []
        while i < j:
            if i == skip:
                i += 1
            elif j == skip:
                j -= 1
            if i >= len(arr) or j < 0:
                continue

            if (arr[j] + arr[i]) == expected_sum:
                result.append([expected_sum, arr[i], arr[j]])
                i += 1
                j -= 1
            elif (arr[i] + arr[j]) < expected_sum:
                i += 1
            else:
                j -= 1
        return result

    result = []
    visited = set()
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        else:
            visited.add(arr[i])
        sub_result = two_number_to_given_sum(arr[i], i)
        if len(sub_result) > 0:
            result.append(sub_result)

    return result


if __name__ == '__main__':
    arr = [-1, 0, 1, 2, -1, -4]
    output = three_some(arr)
    print(output)
