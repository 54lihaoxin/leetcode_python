

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    def __init__(self):
        self.result = []
    
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        
        writeIndex = 0
        readIndex = 0
        
        while readIndex < len(A):
            
            if A[readIndex] != elem:
                A[writeIndex] = A[readIndex]
                writeIndex += 1
            
            readIndex += 1
            
        return writeIndex
    