# Write a function countConstruct(target, word_bank) that accepts a target string and an array of strings.
# The function should return the number of ways that the target can be constructed by concatenating elements of the word_bank array. 
# You may reuse elements of word_bank as many times as needed.


def countConstruct( target, wordBank):
    table = [0] * (len(target) + 1)

    table[0] = 1

    for i in range(len(target)):
        for word in wordBank:
            if target[i: (i+len(word))] == word:
                table[i + len(word)] += table[i] 
    return table[len(target)]



print(countConstruct('purple', ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(countConstruct('enterapotentpot', ["a", "p", "ent", "enter","ot", "o","t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee","eee","eeee","eeeee","eeeeeee"]))

# time complexity O(m^2*n) and space of O(m^2) where m = target and n = length of wordBank