

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
        else:
            if head.next == head:
                return True
            elif head.next == None:
                return False
        
        p1 = head
        p2 = head   # hxl: move in double speed
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next
            if p1 == p2:
                return True
            
        return False
        