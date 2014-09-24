# Reverse Linked List II
# 
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.


from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        
        if head == None or head.next == None or m == n:
            return head
        
        # hxl: make use of a dummy head so that the case m = 1 is easy to deal with
        dummyHead = ListNode(0)
        dummyHead.next = head
        c = 1   # hxl: node counter
        cur = dummyHead
        
        # hxl: point cur to the node before node m
        while c < m:
            cur = cur.next
            c += 1
        
        nodeBeforeM = cur
        nodeM = cur.next
        cur = nodeM
        next = nodeM.next
        nextNext = next.next
        
        while c < n:
            next.next = cur
            cur = next
            next = nextNext
            if nextNext != None:    # hxl: watch out if the current node is the last node
                nextNext = nextNext.next            
            c += 1
        
        nodeBeforeM.next = cur
        nodeM.next = next
        
        return dummyHead.next
