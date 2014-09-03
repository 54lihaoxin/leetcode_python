

debug = True
debug = False


from ListNode import ListNode   # hxl: comment out this line for submission
 
 
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        
        if head == None or head.next == None:
            return head
        elif head.next.next == None:
            head.next.next = head
            head = head.next
            head.next.next = None
            return head
        
        cur = head
        head = head.next
        cur.next = head.next
        head.next = cur
        
        while cur != None and cur.next != None and cur.next.next != None:
            p = cur.next
            q = cur.next.next
            cur.next = q
            cur = p
            p.next = q.next
            q.next = p
            
        return head
        