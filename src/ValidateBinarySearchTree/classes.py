
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self):
        return '[{0}]'.format(self.val)
    