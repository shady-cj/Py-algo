# Write a function fib(n) that takes in a number as an argument. 
# Th function should return the n-th number of the Fibonacci sequenct. 

# The 0th number of the sequence is 0
# The 1st number of the sequence is 1 

# To generate the next number of the sequence, we sum the previous 2

# Method 1

# def fib(n):
#     table = [0] * (n+1)
#     table[1] = 1
#     for i in range(n+1):
#         if i+1 < n+1:
#             table[i+1] += table[i]
#         if i+2 < n+1:
#             table[i+2] += table[i]
#     return table[n]

# Method 2
def fib(n):
    table = [0] * (n+1)
    table[1] = 1
    for i in range(2,n+1):
        table[i] += table[i-1] + table[i-2]
    return table[n]



print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))


# Time complexity O(N) and space complexity = O(N)