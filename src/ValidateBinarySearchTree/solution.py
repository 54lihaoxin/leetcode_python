

debug = True
debug = False


from classes import TreeNode   # hxl: comment out this line for submission
import sys


class Solution:
    
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.validateBST(root, -sys.maxint - 1, sys.maxint)
    
    def validateBST(self, root, minVal, maxVal):
        
        if root == None:
            return True
        
        return (minVal < root.val
                and root.val < maxVal
                and self.validateBST(root.left, minVal, root.val)
                and self.validateBST(root.right, root.val, maxVal))
        