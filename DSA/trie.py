# Implementing a trie or prefix tree


"""
T
|
r
|
y
"""

"""
Solution to https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
"""


class Node:
    def __init__(self):
        self.characters = {}
        self.is_word = False

    def __repr__(self):
        return str(self.characters)

    def __str__(self):
        return self.__repr__()


class Trie:
    def __init__(self):
        self.root = None

    def insert(self, string):
        if not self.root:
            self.root = Node()
        ptr = self.root
        for character in string:
            if character not in ptr.characters:
                ptr.characters[character] = Node()
            ptr = ptr.characters[character]
        ptr.is_word = True

    def search(self, string):
        if self.root is None:
            return False
        ptr = self.root
        for character in string:
            if character not in ptr.characters:
                return False
            ptr = ptr.characters[character]
        return ptr.is_word

    def startswith(self, prefix):
        if self.root is None:
            return False
        ptr = self.root
        for character in prefix:
            if character not in ptr.characters:
                return False
            ptr = ptr.characters[character]
        return True


new_trie = Trie()

new_trie.insert("string")
new_trie.insert("try")
new_trie.insert("tree")
# print(new_trie.root)

print(new_trie.search("string"))
print(new_trie.search("str"))
print(new_trie.startswith("str"))
