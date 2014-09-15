# Balanced Binary Tree
# 
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        
        if root == None:
            return True
        
        (isTreeBalanced, treeDepth) = self.depthFirstSearch(root)
        return isTreeBalanced
        
    def depthFirstSearch(self, root):
        
        if root.left == None and root.right == None:
            return (True, 1)
        
        isLeftTreeBalanced = True
        leftTreeDepth = 0
        if root.left != None:
            (isLeftTreeBalanced, leftTreeDepth) = self.depthFirstSearch(root.left)
        
        isRightTreeBalanced = True
        rightTreeDepth = 0
        if root.right != None:
            (isRightTreeBalanced, rightTreeDepth) = self.depthFirstSearch(root.right)
        
        if (isLeftTreeBalanced
            and isRightTreeBalanced
            and abs(leftTreeDepth - rightTreeDepth) <= 1):
            return (True, max(leftTreeDepth, rightTreeDepth) + 1)
        else:
            return (False, max(leftTreeDepth, rightTreeDepth) + 1)
        