# Populating Next Right Pointers in Each Node II
# 
# Follow up for problem "Populating Next Right Pointers in Each Node".
# 
# What if the given tree could be any binary tree? Would your previous solution still work?
# 
# Note:
# 
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


debug = True
debug = False


# from TreeNode import TreeNode   # hxl: comment out this line for submission


class Solution:

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        
        if root == None:
            return
        
        a = [root]
        b = []
        
        while len(a) > 0 or len(b) > 0 :
            if len(a) == 0:
                a = b
                b = []
                for i in range(0, len(a) - 1):
                    a[i].next = a[i + 1]
            else:
                print a
                while len(a) > 0:
                    if a[0].left != None:
                        b.append(a[0].left)
                    if a[0].right != None:
                        b.append(a[0].right)
                    a.pop(0)
        