# Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings.

# The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array. 


# You may reuse elements of wordBank as many times as needed.

# E.g canConstruct("cat", ["cat", "cats", "dog", "catsdog"]) should return true.
# can canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) should return true.


def canConstruct(target, wordBank):
    table = [False] * (len(target) + 1)
    table[0] = True
    
    for i in range(len(target) + 1):
        if table[i] ==True:
            for word in wordBank:
                if target[i:(i+len(word))] == word:
                    table[i+len(word)] = True
    return table[len(target)]





print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canConstruct('enterapotentpot', ["a", "p", "ent", "enter","ot", "o","t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee","eee","eeee","eeeee","eeeeeee"]))

# time complexity O(m^2*n) and space of O(m^2) where m = target and n = length of wordBank