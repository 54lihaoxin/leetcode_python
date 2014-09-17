# Partition List
# 
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        
        if head == None or head.next == None:
            return head
        
        dummyHead = ListNode(0)
        dummyHead.next = head   # hxl: having a node before would make things a lot easier
        cur = dummyHead
        preInsert = None
        postInsert = None
        
        # hxl: search for the insert point
        while cur.next != None:
            if x <= cur.next.val:
                preInsert = cur
                postInsert = cur.next
                break
            cur = cur.next
        
        # hxl: didn't find any insert point... done!
        if postInsert == None:
            return head
        
        # hxl: move the rest of the smaller nodes to the front
        cur = postInsert
        while cur != None:
            if cur.next != None and cur.next.val < x:
                preInsert.next = cur.next
                preInsert = cur.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        preInsert.next = postInsert
            
        return dummyHead.next
        