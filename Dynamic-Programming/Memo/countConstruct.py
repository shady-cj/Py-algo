# Write a function countConstruct(target, word_bank) that accepts a target string and an array of strings.
# The function should return the number of ways that the target can be constructed by concatenating elements of the word_bank array. 
# You may reuse elements of word_bank as many times as needed.

def countConstruct(target, word_bank):
    if target == "":
        return 1
    total_count = 0
    for word in word_bank:
        if(target.find(word) == 0):
            num_ways_for_rest = countConstruct(target[len(word):], word_bank)
            total_count += num_ways_for_rest
        
    return total_count



# print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
# print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
# print(countConstruct('enterapotentpot', ["a", "p", "ent", "enter","ot", "o","t"]))
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee","eee","eeee","eeeee","eeeeeee"]))

# where m = length of the target  and n = length of the word_bank array
# m = height of the tree so
# Time complexity is 0(n^m * m)
# Space complexity is 0(m^2)

# Memoized version

def countConstructMemo(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    total_count = 0
    for word in word_bank:
        if(target.find(word) == 0):
            num_ways_for_rest = countConstructMemo(target[len(word):], word_bank, memo)
            total_count += num_ways_for_rest
        
    memo[target] =total_count
    return memo[target]



print(countConstructMemo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstructMemo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstructMemo('enterapotentpot', ["a", "p", "ent", "enter","ot", "o","t"]))
print(countConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee","eee","eeee","eeeee","eeeeeee"]))

# where m = length of the target  and n = length of the word_bank array
# m = height of the tree so
# Time complexity is 0(n * m^2)
# Space complexity is 0(m^2)
