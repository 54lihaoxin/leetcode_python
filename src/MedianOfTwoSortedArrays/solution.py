# Median of Two Sorted Arrays
# 
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


# from CommonClasses import * # hxl: comment out this line when submit


debug = True
debug = False


class Solution:
    
    # @return a float
    def findMedianSortedArrays(self, A, B):
        
        if len(A) == 0 and len(B) == 0:
            return None # hxl: return value undefined
        elif len(A) == 0 and len(B) != 0:
            A = B
        elif len(A) != 0 and len(B) == 0:
            B = A
        
        totalLen = len(A) + len(B)
        
        if totalLen % 2 == 0:
            return (self.findKthElement(A, 0, B, 0, totalLen / 2)
                    + self.findKthElement(A, 0, B, 0, totalLen / 2 + 1)) / 2.0
        else:
            return self.findKthElement(A, 0, B, 0, totalLen / 2 + 1)

    # hxl: k starts from 1 (for element at index 0)
    def findKthElement(self, A, numOfDiscardedA, B, numOfDiscardedB, k):
        
        if debug: print A, numOfDiscardedA, B, numOfDiscardedB, k
        numRemainingElementsBeforeKth = k - 1 - numOfDiscardedA - numOfDiscardedB
        
        if numRemainingElementsBeforeKth == 0:  # hxl: base case
            if numOfDiscardedA == len(A):
                return B[numOfDiscardedB]
            elif numOfDiscardedB == len(B):
                return A[numOfDiscardedA]
            else:
                return min(A[numOfDiscardedA], B[numOfDiscardedB])
        else:
            half = (numRemainingElementsBeforeKth - 1) / 2  # numRemainingElementsBeforeKth is at least 1
            nextHalfA = numOfDiscardedA + half
            nextHalfB = numOfDiscardedB + half
            
            if nextHalfA >= len(A):
                nextHalfA = len(A) - 1
            if nextHalfB >= len(B):
                nextHalfB = len(B) - 1
            
            if A[nextHalfA] <= B[nextHalfB]:
                if numOfDiscardedA == nextHalfA + 1:    # hxl: A has been exhausted
                    return self.findKthElement(A, numOfDiscardedA, B, nextHalfB + 1, k)
                else:
                    return self.findKthElement(A, nextHalfA + 1, B, numOfDiscardedB, k)
            else:
                if numOfDiscardedB == nextHalfB + 1:    # hxl: B has been exhausted
                    return self.findKthElement(A, nextHalfA + 1, B, numOfDiscardedB, k)
                else:
                    return self.findKthElement(A, numOfDiscardedA, B, nextHalfB + 1, k)
                  