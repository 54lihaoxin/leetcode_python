# Reverse Nodes in k-Group
# 
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# 
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# 
# You may not alter the values in the nodes, only nodes itself may be changed.
# 
# Only constant memory is allowed.
# 
# For example,
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class Solution:
        
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        
        if head == None or k < 2:
            return head
        
        dummyHead = ListNode(-1)
        dummyHead.next = head
        
        # hxl: setup a window
        preKHead = dummyHead
        kHead = preKHead.next
        kTail = self.getTailForKGroup(kHead, k)
        if kTail != None:
            postKTail = kTail.next
        
        while kTail != None:
            # hxl: reverse
            kTail.next = None
            preKHead.next = self.reverseList(kHead)            
            kHead.next = postKTail
            
            # hxl: shift the window
            preKHead = kHead
            kHead = preKHead.next
            kTail = self.getTailForKGroup(kHead, k)
            if kTail != None:
                postKTail = kTail.next
                
        return dummyHead.next
        
    # hxl: return None if there are less than k nodes
    def getTailForKGroup(self, head, k):
        i = 1   # hxl: head has been counted
        cur = head
        while cur != None and i < k:
            cur = cur.next
            i += 1
        return cur
    
    # hxl: take three pointers to revers a list and the result list ends with None
    def reverseList(self, head):
        
        if head.next == None:
            return head
        
        pre = head
        cur = pre.next
        next = cur.next
        head.next = None
        
        while next != None:
            cur.next = pre
            pre = cur
            cur = next
            next = next.next
                        
        cur.next = pre
        
        return cur
        