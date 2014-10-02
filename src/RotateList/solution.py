# Rotate List
# 
# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
        
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        
        if (head == None
            or head.next == None
            or k < 1):
            return head
        
        ptrCur = head
        length = 0
        
        # hxl: need to know the length because k can be larger than list length
        while ptrCur != None:
            ptrCur = ptrCur.next
            length += 1
        
        k = k % length
        ptrCur = head
        ptrK = head
        
        if k == 0:  # hxl: no need to rotate
            return head
        
        # hxl: ptrK moves k nodes ahead
        while ptrK != None and k > 0:
            k -= 1
            ptrK = ptrK.next
                
        # hxl: both pointers move in the same speed
        while ptrK.next != None:
            ptrCur = ptrCur.next
            ptrK = ptrK.next
        
        ptrK.next = head
        head = ptrCur.next
        ptrCur.next = None
        
        return head
        