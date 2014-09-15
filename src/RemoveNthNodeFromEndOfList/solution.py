# Letter Combinations of a Phone Number
# 
# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        
        if head == None or head.next == None:
            return None
        
        count = 0
        cur = head
        
        while cur != None:
            cur = cur.next
            count += 1
        
        if count == n:
            head = head.next
        else:
            cur = head
            while count != n + 1:
                cur = cur.next
                count -= 1
            cur.next = cur.next.next
        
        return head
    