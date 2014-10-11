
# Definition for doubly-linked list.
class DoublyLinkedListNode:
    
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
        
    def __repr__(self):
        return '[{0}]'.format(self.val)
    