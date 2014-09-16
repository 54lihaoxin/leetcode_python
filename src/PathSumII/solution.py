# Path Sum II
# 
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.pathList = []
    
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root == None:
            return self.pathList
        else:
            self.depthFirstSearch(root, [], sum)
            return self.pathList
    
    def depthFirstSearch(self, root, curPath, targetSum):
        
        curPath.append(root.val)
        
        if root.left == None and root.right == None:
            if sum(curPath) == targetSum:
                self.pathList.append(list(curPath))
        else:
            if root.left != None:
                self.depthFirstSearch(root.left, curPath, targetSum)
            if root.right != None:
                self.depthFirstSearch(root.right, curPath, targetSum)
                
        curPath.pop(-1)
        