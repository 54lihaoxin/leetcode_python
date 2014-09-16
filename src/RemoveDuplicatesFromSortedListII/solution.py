# Remove Duplicates from Sorted List II
# 
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        # hxl: this implementation checks three nodes at a time
        
        if head == None or head.next == None:
            return head
        elif head.next.next == None:
            if head.val == head.next.val:
                return None
            else:
                return head
            
        cur = head
        head = None
        isCurDuplicate = False # hxl: set this to True or False every time before cur = cur.next!
        
        # hxl: look for the first node that has no duplicate as head
        while head == None and cur.next != None:
            if cur.val == cur.next.val: # case: ..., 1, 1, ...
                isCurDuplicate = True
            else:   # case: ..., 1, 2, [2 or 3], ...
                if isCurDuplicate == False:
                    head = cur
                else:
                    isCurDuplicate = False
            cur = cur.next
            
            # hxl: handle cases such as 1 -> 1 -> 2 (head is the last element)
            if (cur.next == None
                and isCurDuplicate == False
                and head == None):
                head = cur 
        
        if head == None:
            return None
        
        cur = head
        
        # hxl: look at the next two or three elements
        while cur!= None and cur.next != None:
            if cur.val == cur.next.val: # hxl: I feel like the flow won't get into this case
                cur.next = cur.next.next
            else:
                if cur.next.next == None:
                    cur = cur.next  # hxl: reaching the last element
                else:
                    if cur.next.val != cur.next.next.val:   # hxl: not duplicate
                        cur = cur.next
                    else:   # hxl: next is duplicate
                        nextVal = cur.next.val
                        while cur.next != None and cur.next.val == nextVal:
                            cur.next = cur.next.next
                            
        return head
    