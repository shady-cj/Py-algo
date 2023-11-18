# Implementing linear fibonacci sequence O(n) with loops


def fibonacci_linear(n):
    if n < 2:
        return n
    first = 0
    second = 1

    for i in range(1, n):
        current = first + second
        first = second
        second = current
    return second


# print(fibonacci_linear(900))


def fibonacci_rec(n):
    if n < 2:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_rec_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 2:
        return n

    cache[n] = fibonacci_rec_memo(n - 1, cache) + fibonacci_rec_memo(n - 2, cache)

    return cache[n]


# print(fibonacci_rec_memo(2000))
# print(fibonacci_linear(2000))

# print(fibonacci_rec(50))
