

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        
        if head == None:
            return False
        
        d = {}
        n = head
        while n.next != None:
            if d.has_key(n):
                return True
            else:
                d[n] = n.val
                n = n.next
            
        return False
        