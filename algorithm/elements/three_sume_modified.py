def three_sum(A):
    def find_two_to_given_sum(expected_sum, skipped_index):
        i, j = 0, len(A) - 1
        while True:
            if i == skipped_index:
                i += 1
            elif j == skipped_index:
                j -= 1

            if i >= j:
                break

            current_sum = A[i] + A[j]
            if current_sum == expected_sum:
                return [A[i], A[j]]
            elif current_sum > expected_sum:
                j -= 1
            else:
                i += 1
        return []
    
    A = sorted(A)
    result = set()
    for i in range(len(A)):
        current = A[i]
        expected_sum = -1 * current
        elements = find_two_to_given_sum(expected_sum, i)
        if len(elements) > 0:
            x = min(elements[0], elements[1], current)
            y = max(elements[0], elements[1], current)
            z = elements[0] + elements[1] + current - x - y
            if (x, z, y) not in result:
                result.add((x, z, y))
    print(list(result))
        
if __name__ == '__main__':
    A = [-1, 0, 1, 2, -1, -4]
    print(three_sum(A))
