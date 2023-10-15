# Implementing a binary tree with basic operations


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(
            {
                "left": self.left.__dict__ if self.left else None,
                "right": self.right.__dict__ if self.right else None,
                "value": self.value,
            }
        )


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self.root
        current_node = self.root
        while True:
            if value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left

    def lookup(self, value):
        if self.root is None:
            return None

        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node.__dict__
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def remove(self, value):
        if self.root is None:
            return None
        parent_node = None
        current_node = self.root
        root = self.root.value == value

        while current_node:
            if value == current_node.value:
                # if it's a leaf node just remove (easiest removal condition)
                # if the right subtree of the current node(node to be removed) is empty or None then put in or replace with the left subtree of the current node
                # if the left subtree of the current node is empty or None then put in or replace with the right subtree of the current node
                # if the current node has both a right and left subtree then traverse the right subtree of and take the leftmost element of the right subtree of the current node then make the leftmost subtree and replace it with the current node, then shift the rest of the tree.
                # To visualize this visit https://visualgo.net/en/bst

                if current_node.left is None and current_node.right is None:
                    if root:
                        self.root = None
                    else:
                        if parent_node.left.value == value:
                            parent_node.left = None
                        else:
                            parent_node.right = None
                elif current_node.right is None:
                    if root:
                        self.root = current_node.left
                    else:
                        if parent_node.left.value == value:
                            parent_node.left = current_node.left
                        else:
                            parent_node.right = current_node.left
                elif current_node.left is None:
                    if root:
                        self.root = current_node.right
                    else:
                        if parent_node.left.value == value:
                            parent_node.left = current_node.right
                        else:
                            parent_node.right = current_node.right
                else:
                    current_right_node = current_node.right
                    parent_right_node = None
                    # current_left_node_of_right_node = current_right_node.left
                    while current_right_node.left:
                        parent_right_node = current_right_node
                        current_right_node = current_right_node.left
                    if parent_right_node:
                        parent_right_node.left = current_right_node.right
                        current_right_node.right = current_node.right
                    current_right_node.left = current_node.left
                    if root:
                        self.root = current_right_node
                    else:
                        if parent_node.left.value == value:
                            parent_node.left = current_right_node
                        else:
                            parent_node.right = current_right_node
                break
            elif value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right

    def traverse(self, node):
        tree = []
        tree.append(
            {
                "left": node.left.value if node.left else None,
                "right": node.right.value if node.right else None,
                "value": node.value,
            }
        )
        if node.left:
            tree.extend(self.traverse(node.left))
        if node.right:
            tree.extend(self.traverse(node.right))
        return tree
        # print(node)


nums = BinaryTree()
data = [39, 18, 54, 14, 17, 8, 20, 19, 25, 52, 60]
for value in data:
    nums.insert(value)
print(nums.traverse(nums.root))
# print(nums.lookup(32))

nums.remove(17)
nums.remove(14)
nums.remove(18)
nums.remove(39)
print("After removal")
print("\n\n\n")
print(nums.traverse(nums.root))
