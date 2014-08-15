

debug = True
debug = False


from classes import TreeNode   # hxl: comment out this line for submission


class Solution:

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        
        if debug: print root
        
        if root == None or root.left == None or root.right == None:
            return
        
        a = [root]
        b = []
        r = [[root.val]]
        
        while len(a) > 0 or len(b) > 0 :
            if len(a) == 0:
                a = b
                b = []
                for i in range(0, len(a) - 1):
                    a[i].next = a[i + 1]
            else:
                while len(a) > 0:
                    if a[0].left != None:
                        b.append(a[0].left)
                    if a[0].right != None:
                        b.append(a[0].right)
                    a.pop(0)
        