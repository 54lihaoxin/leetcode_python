

debug = True
debug = False


from ListNode import ListNode   # hxl: comment out this line for submission
 
 
class Solution:
     
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        
        p1 = l1
        p2 = l2
        r = None
        cur = None
        overflow = False
        
        while p1 != None or p2 != None:
            if debug: print p1.val, p2.val, overflow
            if overflow:
                n = (p1.val + p2.val + 1) % 10
            else:
                n = (p1.val + p2.val) % 10
            overflow = (p1.val + p2.val) >= 10  # hxl: Don't put this line above the assignment of n!
            p1 = p1.next
            p2 = p2.next
            
            if r == None:
                cur = ListNode(n)
                r = cur
            else:
                cur.next = ListNode(n)
                cur = cur.next
                
            if p1 == None:  # hxl: consume p2 if p1 is consumed
                while p2 != None:
                    if overflow:
                        cur.next = ListNode(p2.val + 1)
                        overflow = False
                    else:
                        cur.next = ListNode(p2.val)
                    cur = cur.next
                    p2 = p2.next
                    
            if p2 == None:  # hxl: consume p1 if p2 is consumed
                while p1 != None:
                    if overflow:
                        cur.next = ListNode(p1.val + 1)
                        overflow = False
                    else:
                        cur.next = ListNode(p1.val)
                    cur = cur.next
                    p1 = p1.next
            
        return r
        