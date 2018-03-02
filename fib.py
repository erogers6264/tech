# Naive recursive solution, does a lot of extra work.
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
        print result
    return result


# Memoized solution
n = 100
memo = [None for x in range(n+1)]
def memoized_fib(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = memoized_fib(n - 1, memo) + memoized_fib(n - 2, memo)
    print result
    memo[n] = result
    return result

memoized_fib(n, memo)