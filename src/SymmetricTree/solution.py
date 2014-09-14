# Symmetric Tree
# 
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
#    
# Note:
# Bonus points if you could solve it both recursively and iteratively.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        
        if root == None:
            return True
        else:
            return self.isPairSymmetric(root.left, root.right)
            
    def isPairSymmetric(self, left, right):            
            
        if left == None and right == None:
            return True
        elif (left == None and right != None
              or left != None and right == None):
                return False
        elif left.val != right.val:
            return False
        else:
            return (self.isPairSymmetric(left.left, right.right)
                    and self.isPairSymmetric(left.right, right.left))
        