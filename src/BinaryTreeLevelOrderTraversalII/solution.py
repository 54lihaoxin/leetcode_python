

debug = True
debug = False


from classes import TreeNode   # hxl: comment out this line for submission


class Solution:

    # @param root, a tree node
    # @return a list of integers
    def levelOrder(self, root):
        
        if debug: print root
        
        if root == None:
            return []
        
        a = [root]
        b = []
        r = [[root.val]]
        
        while len(a) > 0 or len(b) > 0 :
            if len(a) == 0:
                a = b
                b = []
                t = []
                for n in a:
                    t.append(n.val)
                r.append(t)
            else:
                while len(a) > 0:
                    if a[0].left != None:
                        b.append(a[0].left)
                    if a[0].right != None:
                        b.append(a[0].right)
                    a.pop(0)
        
        return r
    
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        r = self.levelOrder(root)
        r.reverse()
        return r
    