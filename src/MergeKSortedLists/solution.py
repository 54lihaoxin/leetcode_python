

debug = True
debug = False


from classes import ListNode   # hxl: comment out this line for submission
from heapq import heappush
from heapq import heappop

class Solution:
    
    # hxl: a heap sort implementation
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        
        r = []
        h = []
        
        # hxl: all lists are added to the heap
        for l in lists:
            heappush(h, (l.val, l))
            
        while len(h) != 0:
            (val, node) = heappop(h)
            node = node.next
            if node != None:    # hxl: Don't forget the ending condition!
                heappush(h, (node.val, node))
            r.append(val)
            
        return r
    
    # hxl: a binary merge implementation
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists_binaryMerge(self, lists):
        if debug: print 'mergeKLists[{0}]:'.format(len(lists)), lists
        if lists == None or len(lists) == 0:
            return lists
        elif len(lists) == 1:
            return lists[0]
        else:
            firstHalf = self.mergeKLists(lists[:len(lists)/2])
            secondHalf = self.mergeKLists(lists[len(lists)/2:])
            r = self.mergeTwoLists(firstHalf, secondHalf)
            if debug: print '\t merged:', r
            return r
    
    # hxl: mergeTwoLists is copied from the problem Merge Two List
    
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
#             if debug: print 'l1:', l1
#             if debug: print 'l2:', l2
#             if debug: print 'head:', head
#             if debug: print 
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