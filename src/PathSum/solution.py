# Path Sum
# 
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        else:
            return self.depthFirstSearch(root, 0, sum)
    
    def depthFirstSearch(self, root, curSum, targetSum):
        
        curSum += root.val
        
        if root.left == None and root.right == None:
            return curSum == targetSum
        elif root.left != None and root.right == None:
            return self.depthFirstSearch(root.left, curSum, targetSum)
        elif root.left == None and root.right != None:
            return self.depthFirstSearch(root.right, curSum, targetSum)
        else:
            r = self.depthFirstSearch(root.left, curSum, targetSum)
            if not r:
                r = self.depthFirstSearch(root.right, curSum, targetSum)
            return r
        