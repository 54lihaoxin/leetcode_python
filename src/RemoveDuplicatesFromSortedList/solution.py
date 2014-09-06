# Remove Duplicates from Sorted List
# 
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        cur = head
        
        # hxl: it's just a matter of deciding whether to change cur or cur.next
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
        return head
        