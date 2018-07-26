def mul(num1, num2):
    for j in reversed(range(0, len(num2))):
        carry = 0
        for i in reversed(range(0, len(num1))):
            factor =  num2[j]
            result = (num1[i]*factor + carry)
            #print((len(num2)  - j))
            num1[i - (1 - j)] = result % 10
            carry =  result // 10

if __name__ == '__main__':
    a1 = [1, 2, 3]
    a2 = [2, 1]
    mul(a1, a2)
    print(a1)