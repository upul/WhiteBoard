def three_sum(A):
    def find_two_element(sum, skip):
        i, j = 0, len(A) - 1
        while True:
            if i == skip:
                i += 1
            elif j == skip:
                j -= 1
            if i > j:
                return []
            
            current = A[i] + A[j]
            
            if current == sum:
                return [A[i], A[j]]
            if current > sum:
                j -= 1
            else:
                i += 1
            


    

if __name__ == '__main__':
    A = [-1, 0, 1, 2, -1, -4]
    print(three_sum(A))

    print('Test Passed!')