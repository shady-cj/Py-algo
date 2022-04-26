# Write a function allConstruct(target,word_bank) that accepts a target string and an array of strings.


# The function should return a 2D array containing all of the ways that  the target can be constructed by concatenating elements of the word_bank array. Each element of the 2D array should represent one combination that constructs the target. 

# You may reuse elements of  word_bank as many times as needed. 


def allConstruct(target, word_bank):
    if target == "":
        return [[]]
    
    result = []
    for word in word_bank:
        if target.find(word) == 0 :
            suffix = target[len(word):]
            suffix_ways = allConstruct(suffix, word_bank) 
            target_ways  =  [x[:] for x in suffix_ways]
            [way.insert(0, word) for way in target_ways]
            result.extend(target_ways)

    return result



print(allConstruct("purple", ["purp", "p", "ur","le", "purpl"]))

print(allConstruct("skateboard", ["bo", "rd", "ate", "t" ,"ska", "boar"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"]))

print(allConstruct("aaaaaaaaaaaaaaaz", ["a", "aa","aaa", "aaaa", "aaaaa"]))


# Where m = target and n = wordBank.length 

# O(n^m) time complexity and space complexity is O(m)




# using memo wont have much effect on the optimization and doesn't really affect the true bigger worst case of return 2 dim. arrays 

def allConstructMemo(target, word_bank,memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    
    result = []
    for word in word_bank:
        if target.find(word) == 0 :
            suffix = target[len(word):]
            suffix_ways = allConstructMemo(suffix, word_bank,memo) 
            target_ways  =  [x[:] for x in suffix_ways]
            [way.insert(0, word) for way in target_ways]
            result.extend(target_ways)
    memo[target] = result
    return result



# print(allConstructMemo("purple", ["purp", "p", "ur","le", "purpl"]))

# print(allConstructMemo("skateboard", ["bo", "rd", "ate", "t" ,"ska", "boar"]))
# print(allConstructMemo("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"]))

# print(allConstruct("aaaaaaaaaaaaaaaz", ["a", "aa","aaa", "aaaa", "aaaaa"]))