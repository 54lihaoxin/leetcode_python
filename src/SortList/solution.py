# Sort List
# 
# Sort a linked list in O(n log n) time using constant space complexity.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        
        if head == None:
            return None
        elif head.next == None: # hxl: one node case
            return head
        elif head.next.next == None:
            if head.val <= head.next.val:   # hxl: two nodes case
                return head
            else:
                newHead = head.next
                newHead.next = head
                newHead.next.next = None
                return newHead
        else:   # hxl: more than two nodes case
            prePtr1x = None
            ptr1x = head    # hxl: this will end up pointing to the middle of the list
            ptr2x = head
            
            while ptr2x != None:
                prePtr1x = ptr1x 
                ptr1x = ptr1x.next
                ptr2x = ptr2x.next
                if ptr2x != None:
                    ptr2x = ptr2x.next 
            
            if debug: print head, ptr1x
            prePtr1x.next = None    # hxl: don't forget to cut the list before doing sort!
            firstSortedHalf = self.sortList(head)
            secondSortedHalf = self.sortList(ptr1x)
            
            if debug: print firstSortedHalf, secondSortedHalf
            
            newHead = None
            
            if firstSortedHalf.val < secondSortedHalf.val:
                newHead = firstSortedHalf
                firstSortedHalf = firstSortedHalf.next
            else:
                newHead = secondSortedHalf
                secondSortedHalf = secondSortedHalf.next
            
            cur = newHead
                
            while (firstSortedHalf != None
                   and secondSortedHalf != None):
                if firstSortedHalf.val < secondSortedHalf.val:
                    cur.next = firstSortedHalf
                    cur = cur.next
                    firstSortedHalf = firstSortedHalf.next
                else:
                    cur.next = secondSortedHalf
                    cur = cur.next
                    secondSortedHalf = secondSortedHalf.next
                    
            if firstSortedHalf == None:
                cur.next = secondSortedHalf
            else:   # secondSortedHalf is empty
                cur.next = firstSortedHalf
                
            return newHead
        