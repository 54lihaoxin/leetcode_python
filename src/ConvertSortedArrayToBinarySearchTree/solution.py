# Convert Sorted Array to Binary Search Tree
# 
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        
        if len(num) == 0:
            return None
        
        mid = len(num) / 2
        r = TreeNode(num[mid])
        if 0 < mid:
            r.left = self.sortedArrayToBST(num[:mid])
        if mid + 1 < len(num):
            r.right = self.sortedArrayToBST(num[mid + 1:])
        return r
        
