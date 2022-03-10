# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_to_tree(root):
    if len(root) > 0:
        if root[0] is not None:
            tree = TreeNode(val = root[0])
            
            if len(root) > 1 and root[1] != None:
                tree.left = convert_to_tree(root[1:])
            elif len(root) > 1 and root[1] == None:
                tree.right = convert_to_tree(root[2:])
        else:
            tree = None
        return tree 
    

root = [1]

tree = convert_to_tree(root)



