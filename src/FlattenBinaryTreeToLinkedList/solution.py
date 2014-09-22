# Flatten Binary Tree to Linked List
# 
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
# 
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#              
# Hints:
# If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flattenWithFlattenSubtree(root, None)
    
    def flattenWithFlattenSubtree(self, root, subtree):
        if root != None:
            if subtree == None:
                if root.left == None and root.right == None:
                    pass    # hxl: nothing to do
                elif root.left == None and root.right != None:
                    self.flattenWithFlattenSubtree(root.right, subtree)
                elif root.left != None and root.right == None:
                    self.flattenWithFlattenSubtree(root.left, subtree)
                    root.right = root.left
                    root.left = None                    
                elif root.left != None and root.right != None:
                    self.flattenWithFlattenSubtree(root.right, subtree)
                    self.flattenWithFlattenSubtree(root.left, root.right)
                    root.right = root.left
                    root.left = None
            else:   # subtree != None
                if root.left == None and root.right == None:
                    root.right = subtree
                elif root.left == None and root.right != None:
                    self.flattenWithFlattenSubtree(root.right, subtree)
                elif root.left != None and root.right == None:
                    self.flattenWithFlattenSubtree(root.left, subtree)
                    root.right = root.left
                    root.left = None                    
                elif root.left != None and root.right != None:
                    self.flattenWithFlattenSubtree(root.right, subtree)
                    self.flattenWithFlattenSubtree(root.left, root.right)
                    root.right = root.left
                    root.left = None
    