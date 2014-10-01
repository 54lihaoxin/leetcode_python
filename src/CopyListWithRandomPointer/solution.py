# Copy List with Random Pointer
# 
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.


from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None        
        self.insertNodesInBetween(head)
        self.setUpRandomPointerForNewNodes(head)
        return self.getListOfNewNodes(head)
    
    def insertNodesInBetween(self, head):        
        cur = head        
        while cur != None:
            new = RandomListNode(cur.label)
            new.next = cur.next
            cur.next = new
            cur = new.next
    
    def setUpRandomPointerForNewNodes(self, head):
        cur = head
        while cur != None:
            new = cur.next
            if cur.random == None:
                new.random = None
            else:
                new.random = cur.random.next
            cur = new.next
                
    def getListOfNewNodes(self, head):
        r = head.next
        cur = head
        while cur != None:
            new = cur.next
            cur.next = new.next
            cur = cur.next
            if cur != None:
                new.next = cur.next 
        return r            
        