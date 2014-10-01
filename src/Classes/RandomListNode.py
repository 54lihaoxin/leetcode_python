
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    
    def __repr__(self):
        return '[{0}]'.format(self.label)
    