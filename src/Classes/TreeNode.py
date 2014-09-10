
# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None    # hxl: special for the problem Populating Next Right Pointers In Each Node
        
    def __repr__(self):
        return '[{0}]'.format(self.val)


# OJ's Binary Tree Serialization:
# The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.
# 
# Here's an example:
#    1
#   / \
#  2   3
#     /
#    4
#     \
#      5
# The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

# hxl: WARNING: The value in a node is a string, not a number!
def getTreeFromString(s):
    
    s = s[1:-1].split(',')
    
    if len(s) < 2:  # hxl: should have '{}', at least
        return None
    
    root = TreeNode(s[0])
    nodeArray = [root]
    s = s[1:]
    isAddingToLeftChild = True
    
    while len(s) > 0:
        if s[0] == '#':
            pass
        else:
            if isAddingToLeftChild:
                nodeArray[0].left = TreeNode(s[0])
                nodeArray.append(nodeArray[0].left)
            else:
                nodeArray[0].right = TreeNode(s[0])
                nodeArray.append(nodeArray[0].right)
        
        if isAddingToLeftChild == False:
            nodeArray = nodeArray[1:]   # hxl: the node has two children now
            
        if len(s) >= 1: # hxl: don't run out of index
            s = s[1:]
            
        isAddingToLeftChild = not isAddingToLeftChild
        
    return root
    