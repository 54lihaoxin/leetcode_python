

debug = True
debug = False


from classes import ListNode   # hxl: comment out this line for submission


class Solution:
    
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        arr = []
        cur = head
        
        while cur != None:
            arr.append(cur)
            cur = cur.next
        
        tempHead = None
        tempTail = None
        
        for i in range(0, len(arr) / 2):
            tempHead = arr[i]
            tempTail = arr[len(arr) - i - 1]
            tempTail.next = tempHead.next
            tempHead.next = tempTail
        
        if len(arr) % 2 == 1:   # odd length
            tempTail.next = arr[len(arr) / 2]
            tempTail = tempTail.next
        
        tempTail.next = None 
        return head
        