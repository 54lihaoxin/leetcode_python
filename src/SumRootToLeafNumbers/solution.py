# Sum Root to Leaf Numbers
# 
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25.


debug = True
debug = False


class Solution:
    
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        
        if root == None:
            return 0
        else:
            return self.sumNumbersWithHistory(root, 0, 0)   # hxl: init value should be nothing!
    
    def sumNumbersWithHistory(self, root, curNum, curSum):
        
        n = curNum * 10 + long(root.val)
        
        if root.left == None and root.right == None:
            return n + curSum   # hxl: only add in the base case
        else:
            if root.left != None:   # hxl: don't make a mistake here checking the other child is None...
                curSum = self.sumNumbersWithHistory(root.left, n, curSum)
            if root.right != None:
                curSum = self.sumNumbersWithHistory(root.right, n, curSum)
            return curSum
        