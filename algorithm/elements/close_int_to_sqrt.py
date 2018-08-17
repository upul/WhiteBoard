def find_close_int_to_sqrt(x):
    lower, upper = 0, x
    while lower <= upper:
        mid = (lower + upper) // 2
        mid_square = mid * mid 

        if mid_square < x:
            lower += 1 
        elif mid_square > x:
            upper -= 1
        else:
            return mid
    return lower - 1

if __name__ == '__main__':
    print(find_close_int_to_sqrt(16))
    print(find_close_int_to_sqrt(28))