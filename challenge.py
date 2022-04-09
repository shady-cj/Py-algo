# Writing a code to find the longest common subsequence between 2 array of words
# 

# That is words like "common" and "condo" have 3 common subsequence with the letters "coo" occuring 

# The solution
# first we initialize to variables at 0 which serves as the index for the 2 arrays 

# We check for a terminating condition that is when any of the 2 variables is equal to the length of their corresponding arrays 


# Then we also check for when the values of both arrays are equal based on their corresponding index that we defined earlier... Then if they are equal we return 1 + the recursion of both arrays increment the variables for array 1 and array 2

# We check for a last condition which is when the values of the corresponding indexes are not equal.. Which means we split the conditions into increment the variable index for array 1 and leave array 2 or vice versa..., we then call the main function recursively on both arrays with the conditions... the maximum from this condition will be the highest subsequence from them and then the result is added and returned..

# let's implement the solution now...

# Define a function that takes array 1, array 2, idx1 and idx2 

def recursive_lcs( arr1, arr2, idx1=0, idx2=0):
    # we then check for the terminating condition
    if idx1 == len(arr1) or idx2 == len(arr2):
        return 0 #we return 0
    
    # Now we check if the value of arr1[idx1] is equal to that of arr2[idx2]

    elif arr1[idx1] == arr2[idx2]:
        # We return the addition of 1 and the recursion of the rest of the array with their corresponding index incremented

        return 1 + recursive_lcs(arr1, arr2, idx1+1,idx2+1)

    # We the check for the last condition where they are not equal and their indexes are still range


    else:
        # This is where we check for the 2 conditions 

        # First we increment idx1 and leave idx2

        option1 = recursive_lcs(arr1, arr2, idx1+1, idx2)
        
        # Second we increment idx2 and leave idx1

        option2  = recursive_lcs(arr1, arr2,idx1,idx2+1)

        return max(option1, option2)


    #
    # You can use this approach directly on strings too...


    # Time complexity of this approach is O(2^m+n) where m and n are the lengths of the 2 strings/array
    #  
print(recursive_lcs(['a','b','c','e','y','f','d','e'], ['a','e','e','e','e','b','c','e','y','d','e']))


# improved solution using memoization



def recursive_lcs_memo(arr1, arr2, idx1=0, idx2=0, memo={}):
    # we then check for the terminating condition

    idx = (idx1, idx2)
    if idx in memo:
        return memo[idx]
    elif idx1 == len(arr1) or idx2 == len(arr2):
        return 0 #we return 0
    
    # Now we check if the value of arr1[idx1] is equal to that of arr2[idx2]

    elif arr1[idx1] == arr2[idx2]:
        # We return the addition of 1 and the recursion of the rest of the array with their corresponding index incremented
        memo[idx] = 1 + recursive_lcs_memo(arr1, arr2, idx1+1,idx2+1, memo)

    # We the check for the last condition where they are not equal and their indexes are still range


    else:
        # This is where we check for the 2 conditions 

        # First we increment idx1 and leave idx2

        option1 = recursive_lcs_memo(arr1, arr2, idx1+1, idx2, memo)
        
        # Second we increment idx2 and leave idx1

        option2  = recursive_lcs_memo(arr1, arr2,idx1,idx2+1, memo)

        memo[idx]= max(option1, option2)
    # print(memo)
    return memo[idx]


# print(recursive_lcs_memo(['a','b','c','e','y','f','d','e'], ['a','e','e','e','e','b','c','e','y','d','e']))

# Memoization approach makes sure you don't repeat the same subproblems and you can save the result of the subproblems and use it later... since we will comparing those 2 options in the last part of the function that is the else condition... using the first approach poses a problem of re-evaluating the same sub-problems again and again... thus we use memoization to avoid this problem... 
# this is the time complexity of the memoization approach is O(m*n) where m and n are the lengths of the 2 strings/array which is for example for our problem above m = 8 (['a','b','c','e','y','f','d','e']) and n =11 ( ['a','e','e','e','e','b','c','e','y','d','e']) which implies solving the subproblems (8*11) times in the worst case scenario(i.e where there is no common subsequence) compared to the mere recursive approach which is 2^(8+11) which is 2^19(524,288) which is a lot of subproblems to solve... in the worst case scenario where as the memoized version does that in just (88) subproblems...