

debug = True
debug = False


from classes import ListNode   # hxl: comment out this line for submission, otherwise Compiler Error on LeetCode


class Solution:

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        
        if debug: print head
        
        if head == None or head.next == None:
            return None
        
        d = {}
        n = head
        while n.next != None:
            if d.has_key(n):
                return n
            else:
                d[n] = n.val
                n = n.next
            
        return None
        