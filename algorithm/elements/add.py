def add_one(number):
    """
    This is an simple example on how to add one to a given
    number.
    """
    number[-1] += 1
    for i in reversed(range(0, len(number))):
        if number[i] == 10:
            number[i] = 0
            if i > 0: 
                number[i - 1] += 1      
            else:
                number.insert(0, 1)
        else:
              break

if __name__ == '__main__':
    a1 = [9, 8, 9, 9]
    add_one(a1)
    print(a1)