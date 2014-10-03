# Insertion Sort List
# 
# Sort a linked list using insertion sort.

 
debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        
        
        # hxl: see wiki here: http://en.wikipedia.org/wiki/Insertion_sort
        
        
        if head == None or head.next == None:
            return head
        
        dummyHead = ListNode(-1)
        dummyHead.next = head
        cur = dummyHead
        
        while cur != None:
            if cur == dummyHead:
                cur = cur.next
            else:
                if cur.next == None:
                    cur = None
                else:
                    if cur.val <= cur.next.val:
                        cur = cur.next
                    else:
                        next = cur.next
                        nodeBeforeInsertion = dummyHead
                        while nodeBeforeInsertion.next.val < next.val:
                            nodeBeforeInsertion = nodeBeforeInsertion.next
                        cur.next = cur.next.next
                        next.next = nodeBeforeInsertion.next
                        nodeBeforeInsertion.next = next
                        
        return dummyHead.next
