

debug = True
debug = False


from classes import TreeNode   # hxl: comment out this line for submission


class Solution:

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        
        if debug: print root
        
        if root == None:
            return []
        
        r = [root.val]
        
        if root.left != None:
            r += self.preorderTraversal(root.left)
        if root.right != None:
            r += self.preorderTraversal(root.right)
        
        return r
        