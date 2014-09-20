# Convert Sorted List to Binary Search Tree
# 
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


# hxl: It's easy to create an array to hold to list and then build a tree from it, but it's boring.
#      The following solution doesn't make use of an extra array.


class Solution:
    
    def __init__(self):
        self.remainingList = None
    
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):        
        if head == None:
            return None        
        self.remainingList = head
        length = self.getListLength(head)        
        return self.binaryMakeTree(length)
    
    def getListLength(self, head):
        count = 0
        while head != None:
            head = head.next
            count += 1
        return count
    
    def binaryMakeTree(self, length):
        if length < 1:
            return None
        if length == 1:
            root = TreeNode(self.remainingList.val)
            self.remainingList = self.remainingList.next
            return root
        elif length == 2:
            left = TreeNode(self.remainingList.val)
            self.remainingList = self.remainingList.next
            root = TreeNode(self.remainingList.val)
            self.remainingList = self.remainingList.next
            root.left = left    
            return root
        elif length == 3:
            left = TreeNode(self.remainingList.val)
            self.remainingList = self.remainingList.next
            root = TreeNode(self.remainingList.val)
            root.left = left
            self.remainingList = self.remainingList.next            
            root.right = TreeNode(self.remainingList.val)
            self.remainingList = self.remainingList.next    
            return root
        else:
            midPoint = length / 2
            left = self.binaryMakeTree(midPoint)
            root = self.binaryMakeTree(1)
            root.left = left
            root.right = self.binaryMakeTree(length - midPoint - 1)
            return root
