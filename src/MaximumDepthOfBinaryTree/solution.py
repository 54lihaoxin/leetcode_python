
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            return 1 + self.maxDepth(root.right)
        elif root.left != None and root.right == None:
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
        