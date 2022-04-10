# On the initial challenge we did longest common subsequence of 2 words or arrays 
# Now we would solve for the longest increasing subsequence of a numbers of arrays or words 
# for example [1,3,5,2,5,6,3,5,7] the longest increasing subsequence of this array is [1,3,5,6,7] or [1,2,5,6,7]

# Implementing the solution

def lis_recursive(arr,start=0, end=1):
    # print(arr,start, end)
    if len(arr) == 0:
        return 0
    if end == len(arr):
        return 1

    elif arr[start] < arr[end]:
        opt1 = 1 + lis_recursive(arr, end, end+1)
        opt2 = lis_recursive(arr, start, end+1)  
        return max(opt1, opt2)
    else:
        return lis_recursive(arr,start, end+1)
    


# print(lis_recursive([3,2]))
# print(lis_recursive([1,3,7,4,6,5,6,7]))
# print(lis_recursive([1,4,3,2,3,6,4,5]))
# print(lis_recursive([1,3,5,2,5,6,3,5,7] ))
    
# print(lis_recursive([3,1,5,2,6]))
# print(lis_recursive([1,5,2,1]))

# Time complexity of O(2^n)


# Memoized version 
def lis_recursive_memo(arr, start=0, end=0, memo={}):
    idx = (start, end)
    if len(arr) == 0:
        return 0
    elif idx in memo:
        return memo[idx]
    
    elif end == len(arr):
        return 1
    
    elif arr[start] < arr[end]:
        opt1 = 1 +  lis_recursive_memo(arr, end, end+1,memo)
        opt2 = lis_recursive_memo(arr, start, end+1,memo)  
        memo[idx] = max(opt1, opt2)
    else:
        memo[idx] = lis_recursive_memo(arr,start, end+1, memo)
    return memo[idx]

# print(lis_recursive_memo([1,3,5,2,5,6,3,5,7,8,9,10,11,4,12] ))