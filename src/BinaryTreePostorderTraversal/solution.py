

debug = True
debug = False


from classes import TreeNode   # hxl: comment out this line for submission


class Solution:

    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        
        if debug: print root
        
        if root == None:
            return []
        
        r = []
        
        if root.left != None:
            r += self.postorderTraversal(root.left)
        
        if root.right != None:
            r += self.postorderTraversal(root.right)
        
        r += [root.val]
        
        return r
        