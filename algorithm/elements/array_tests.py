# This file contains some programming questions 
# involving arrays and string 

def reverse_str(input_str):
    if None or len(input_str) == 0:
        return input_str
    mid = len(input_str) // 2
    j = 0
    input_str = list(input_str)
    while j <= mid:
        input_str[j], input_str[-(j+1)] = input_str[-(j+1)], input_str[j] 
        j += 1
    return input_str

if __name__ == '__main__':
    str1 = 'hello world'
    print(reverse_str(str1))