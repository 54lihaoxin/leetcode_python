# Minimum Path Sum
# 
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.curMinDepth = 0
        
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        self.depthFirstSearch(root, 1)
        return self.curMinDepth
    
    def depthFirstSearch(self, root, curDepth):
        
        if (root == None
            or (self.curMinDepth != 0
                and curDepth == self.curMinDepth)):
            return  # hxl: don't do extra search      
        
        if root.left == None and root.right == None:
            if self.curMinDepth == 0:
                self.curMinDepth = curDepth
            else:
                self.curMinDepth = min(self.curMinDepth, curDepth)
        else:
            self.depthFirstSearch(root.left, curDepth + 1)
            self.depthFirstSearch(root.right, curDepth + 1)
        