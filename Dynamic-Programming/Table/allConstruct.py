# Write a function allConstruct(target,word_bank) that accepts a target string and an array of strings.


# The function should return a 2D array containing all of the ways that  the target can be constructed by concatenating elements of the word_bank array. Each element of the 2D array should represent one combination that constructs the target. 

# You may reuse elements of  word_bank as many times as needed. 


def allConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in wordBank:
            if target[i: len(word)+i] == word:
                tableCopy = [t[:] for t in table[i]]
                [way.append(word) for way in tableCopy]
                table[i + len(word)].extend(tableCopy)

    return table[len(target)]         
print(allConstruct("purple", ["purp", "p", "ur","le", "purpl"]))

print(allConstruct("skateboard", ["bo", "rd", "ate", "t" ,"ska", "boar"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd","ef","c"]))

print(allConstruct("aaaaaaaaaaaaaaaz", ["a", "aa","aaa", "aaaa", "aaaaa"]))
print(allConstruct("shgas", ["sh", "as", "gas"]))
# m = target.length n=wordBank.length
# 
# Time complexity O(n^m)
# space complexity O(n^m)
# Exponential complexity 
