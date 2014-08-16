

debug = True
debug = False


from classes import ListNode   # hxl: comment out this line for submission, otherwise Compiler Error on LeetCode

# hxl: see http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html

class Solution:

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        
        if debug: print head
        
        if head == None:
            return None
        else:
            if head.next == head:
                return head
            elif head.next == None:
                return None
        
        p1 = head
        p2 = head   # hxl: move in double speed
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next
            if p1 == p2:
                break
        
        if p2 == None:
            return None
        
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2
    
    