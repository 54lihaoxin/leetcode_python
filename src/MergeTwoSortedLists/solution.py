

debug = True
debug = False


from ListNode import ListNode   # hxl: comment out this line for submission


class Solution:
    
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        
        # hxl: Pay attention and don't alter l1 or l2!!
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val < l2.val:
            cur = ListNode(l1.val)
            l1 = l1.next
        else:
            cur = ListNode(l2.val)
            l2 = l2.next
            
        head = cur  # hxl: Don't forget to keep a reference to the head!
        
        while l1 != None or l2 != None:
            if debug: print 'l1:', l1
            if debug: print 'l2:', l2
            if debug: print 'head:', head
            if debug: print 
            if l1 == None:
                cur.next = l2
                return head
            elif l2 == None:
                cur.next = l1
                return head
            
            # hxl: Don't forget to create new node and point correctly!
            if l1.val < l2.val:
                next = ListNode(l1.val)
                cur.next = next
                cur = next
                l1 = l1.next
            else:
                next = ListNode(l2.val)
                cur.next = next
                cur = next
                l2 = l2.next
                
        return head
    