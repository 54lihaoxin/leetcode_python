

debug = True
debug = False


from TreeNode import TreeNode   # hxl: comment out this line for submission


class Solution:

    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        
        if debug: print root
        
        if root == None:
            return []
        
        r = []
        
        if root.left != None:
            r += self.inorderTraversal(root.left)
            
        r += [root.val]
        
        if root.right != None:
            r += self.inorderTraversal(root.right)
        
        return r
        