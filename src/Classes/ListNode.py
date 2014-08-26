
# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def __repr__(self):
        s = ''
        cur = self
        while cur != None:
            s += '[{0}]->'.format(cur.val)
            cur = cur.next
        s += 'X '
        return s
    
    
# @param a list
# @return a ListNode, which is the head of a linked list
def listFromList(l):
    
    if l == None or len(l) == 0:
        return None
    
    r = ListNode(l[0])
    cur = r
    l.pop(0)
    
    while len(l) > 0:
        cur.next = ListNode(l[0])
        cur = cur.next
        l.pop(0)
        
    return r

    
# @param a list of sorted lists such as [[0, 1],[-1,2],[3,4]]
# @return a list of ListNode's
def listOfLists(lol):
    r = []
    for l in lol:
        head = None
        cur = None
        for n in l:
            if head == None:
                head = ListNode(n)
                cur = head
            else:
                cur.next = ListNode(n)
                cur = cur.next 
        r.append(head)
    return r
