import sys 
# Fibonacci sequence value of a given nth number solving with recursion

def fib(n):

    if (n <= 2):
        return 1
   
    return fib(n-1) + fib(n-2)

# memoized version
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif (n <= 2):
        return 1
    memo[n] = fib_memo(n-1,memo) + fib_memo(n-2,memo)
    return memo[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_args = int(sys.argv[1])
        print(fib(get_args))