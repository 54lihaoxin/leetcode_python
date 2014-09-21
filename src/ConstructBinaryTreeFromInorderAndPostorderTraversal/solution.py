# Construct Binary Tree from Inorder and Postorder Traversal
# 
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


# hxl: Here is a iterative solution that is able to handle a deep tree.


class Solution:
    
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
         
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        aboveRoot = TreeNode(-1)    # hxl: for OJ, val has to be an integer
        inOrderValIndexDict = {}    # hxl: K: in order list value; V: in order list index. Only works with no duplicate in list.
        for i in range(len(inorder)):
            inOrderValIndexDict[inorder[i]] = i
        
        # hxl: Each element is a tuple of (start, end, parent) of the input arrays.
        #      This list is used as a stack.
        indexList = [((0, len(inorder) - 1),
                      (0, len(postorder) - 1),
                      aboveRoot)]
         
        while len(indexList) > 0:
            if debug: print indexList
            indexTuple = indexList.pop(-1)            
            inOrderLeft = indexTuple[0][0]
            inOrderRight = indexTuple[0][1]
            postOrderLeft = indexTuple[1][0]
            postOrderRight = indexTuple[1][1]
            parent = indexTuple[2]
            
            # hxl: make node
            curNode = TreeNode(postorder[postOrderRight])
            if parent == aboveRoot:
                parent.right = curNode
            elif inOrderValIndexDict[curNode.val] < inOrderValIndexDict[parent.val]:
                parent.left = curNode
            else:
                parent.right = curNode
            
            inOrderRootIndex = inOrderValIndexDict[curNode.val]
            
            # hxl: add left child to stack
            if inOrderLeft < inOrderRootIndex:
                lenOfLeft = inOrderRootIndex - inOrderLeft
                indexList.append(((inOrderLeft, inOrderRootIndex - 1),
                                  (postOrderLeft, postOrderLeft + lenOfLeft - 1),
                                  curNode))
            
            # hxl: add right child to stack
            if inOrderRootIndex < inOrderRight:
                lenOfRight = inOrderRight - inOrderRootIndex
                indexList.append(((inOrderRootIndex + 1, inOrderRight),
                                  (postOrderRight - lenOfRight, postOrderRight - 1),
                                  curNode))
                
            if debug: print parent.left, parent, parent.right
        
        return aboveRoot.right  # hxl: this is the actual root

    
    # hxl: recursive implementation that fails with big input
#     # @param inorder, a list of integers
#     # @param postorder, a list of integers
#     # @return a tree node
#     def buildTree(self, inorder, postorder):
#          
#         if len(inorder) == 0 or len(postorder) == 0:
#             return None
#          
#         print inorder, postorder
#          
#         root = TreeNode(postorder[-1])
#         indexOfRootInInOrderList = 0
#          
#         for i in range(len(inorder)):
#             if inorder[i] == root.val:
#                 indexOfRootInInOrderList = i
#                 break
#          
#         inOrderLeftHalf = inorder[:indexOfRootInInOrderList]
#         inOrderRightHalf = inorder[indexOfRootInInOrderList + 1:]
#         postOrderLeftHalf = postorder[:indexOfRootInInOrderList]
#         postOrderRightHalf = postorder[-len(inOrderRightHalf) - 1:-1]
#          
#         root.left = self.buildTree(inOrderLeftHalf, postOrderLeftHalf)
#         root.right = self.buildTree(inOrderRightHalf, postOrderRightHalf)
#          
#         return root
    