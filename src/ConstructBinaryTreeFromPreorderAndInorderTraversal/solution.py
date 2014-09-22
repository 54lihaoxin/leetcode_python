# Construct Binary Tree from Inorder and Postorder Traversal
# 
# Given inorder and postorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.


debug = True
# debug = False


from CommonClasses import * # hxl: comment out this line for submission


# hxl: Here is a iterative solution that is able to handle a deep tree.


class Solution:
    
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
         
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        aboveRoot = TreeNode(-1)    # hxl: for OJ, val has to be an integer
        inOrderValIndexDict = {}    # hxl: K: in order list value; V: in order list index. Only works with no duplicate in list.
        for i in range(len(inorder)):
            inOrderValIndexDict[inorder[i]] = i
        
        # hxl: Each element is a tuple of (start, end, parent) of the input arrays.
        #      This list is used as a stack.
        indexList = [((0, len(preorder) - 1),
                      (0, len(inorder) - 1),
                      aboveRoot)]
         
        while len(indexList) > 0:
            if debug: print indexList
            indexTuple = indexList.pop(-1)
            preOrderLeft = indexTuple[0][0]
            preOrderRight = indexTuple[0][1]            
            inOrderLeft = indexTuple[1][0]
            inOrderRight = indexTuple[1][1]
            parent = indexTuple[2]
            
            # hxl: make node
            curNode = TreeNode(preorder[preOrderLeft])
            inOrderRootIndex = inOrderValIndexDict[curNode.val]
            
            if parent == aboveRoot:
                parent.right = curNode
            elif inOrderRootIndex < inOrderValIndexDict[parent.val]:
                parent.left = curNode
            else:
                parent.right = curNode
            
            # hxl: add left child to stack
            if inOrderLeft < inOrderRootIndex:
                lenOfLeft = inOrderRootIndex - inOrderLeft
                indexList.append(((preOrderLeft + 1, preOrderLeft + lenOfLeft),
                                  (inOrderLeft, inOrderRootIndex - 1),
                                  curNode))
            
            # hxl: add right child to stack
            if inOrderRootIndex < inOrderRight:
                lenOfRight = inOrderRight - inOrderRootIndex
                indexList.append(((preOrderRight - lenOfRight + 1, preOrderRight),
                                  (inOrderRootIndex + 1, inOrderRight),
                                  curNode))
                
            if debug: print parent.left, parent, parent.right
        
        return aboveRoot.right  # hxl: this is the actual root
    