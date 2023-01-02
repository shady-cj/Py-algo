
"""
Given a binary tree, determine if it is height-balanced.
"""


# Solution 
class Solution:
    def height(self, root):
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if (abs(left - right) > 1):
            return False
        leftB = self.isBalanced(root.left)
        rightB= self.isBalanced(root.right)
        if leftB == False or rightB == False:
            return False
        return True
            
