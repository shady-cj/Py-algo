# Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings.

# The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array. 


# You may reuse elements of wordBank as many times as needed.

# E.g canConstruct("cat", ["cat", "cats", "dog", "catsdog"]) should return true.
# can canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) should return true.

def canConstruct( target, word_bank):
    if target == "":
        return True

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            is_present = canConstruct(suffix, word_bank)
            if is_present ==True:
                return True

    return False

# print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
# print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
# print(canConstruct('enterapotentpot', ["a", "p", "ent", "enter","ot", "o","t"]))
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee","eee","eeee","eeeee","eeeeeee"]))

# where m = length of the target  and n = length of the word_bank array
# m = height of the tree so
# Time complexity is 0(n^m * m)
# Space complexity is 0(m^2)



# Memoized version
def canConstructMemo(target, word_bank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return True

    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            is_present = canConstructMemo(suffix, word_bank, memo)
            if is_present ==True:
                memo[target] = True
                return True
    memo[target] = False
    return False
    



print(canConstructMemo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstructMemo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstructMemo('enterapotentpot', ["a", "p", "ent", "enter","ot", "o","t"]))
print(canConstructMemo("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee","eee","eeee","eeeee","eeeeeee"]))



# where m = length of the target  and n = length of the word_bank array
# m = height of the tree so
# Time complexity is 0(n * m^2)
# Space complexity is 0(m^2)
