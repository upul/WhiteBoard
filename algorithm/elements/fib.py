def fib(n, memo={}):
    """
    Calculating Fibonacci number using 
    Dynamic Programming.
    """
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        memo[n] = result
        return result 

def fib_iterative(n):
    """
    Iterative algorithm for Fibonacci numbers
    """
    memory = {}
    for i in range(1, n+1):
        if i <= 2:
            memory[i] = 1
        else:
            memory[i] = memory[i-1] + memory[i-2]
    return memory[n]

if __name__ == '__main__':
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(12) == 144
    assert fib(20) == 6765
    assert fib(100) == 354224848179261915075
    assert fib(250) == 7896325826131730509282738943634332893686268675876375

    assert fib_iterative(1)  == 1
    assert fib_iterative(2)  == 1
    assert fib_iterative(12) == 144
    assert fib_iterative(20) == 6765
    assert fib_iterative(100) == 354224848179261915075
    assert fib_iterative(250) == 7896325826131730509282738943634332893686268675876375

    print('Test Passed!')