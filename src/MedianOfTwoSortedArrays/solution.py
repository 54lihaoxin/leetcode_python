# Median of Two Sorted Arrays
# 
# There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


from CommonClasses import * # hxl: comment out this line when submit


debug = True
debug = False


class Solution:
    
    # @return a float
    def findMedianSortedArrays(self, A, B):
        
        if debug: print 'A', A
        if debug: print 'B', B
        if debug: print 'A + B = {0} + {1} = {2} \n'.format(len(A), len(B), len(A) + len(B))
        
        return self.findMedian(A, 0, B, 0, (len(A) + len(B)) / 4)
    
    def findMedian(self, A, startA, B, startB, span):
        
        if debug: print 'A[{0}/{1}] = {2}, B[{3}/{4}] = {5}  / span = {6}'.format(startA, len(A)-1, A[startA], startB, len(B)-1, B[startB], span)
        
        # hxl: startA can be interpreted as "number of elements on the left of a[startA]". 
        #      Same for startB. So, startA + startB == totalLen / 2 means the base case is reached.
        totalLen = len(A) + len(B)
        if ((totalLen % 2 == 1
             and startA + startB == totalLen / 2)
            or
            (totalLen % 2 == 0
            and startA + startB == totalLen / 2 - 1)):
            return self.findMedianHelper(A, startA, B, startB)
        
        if span < 1:
            span = 1    # hxl: make sure there some progress
        
        nextSpan = span / 2
        nextIndexA = startA + span
        nextIndexB = startB + span
        
        if nextIndexA >= len(A):
            nextIndexA = max(0, len(A) - 1) # hxl: it's possible that A is empty
        if nextIndexB >= len(B):
            nextIndexB = max(0, len(B) - 1) # hxl: it's possible that B is empty
            
        if ((nextIndexA != startA
             or len(A) == 1)
            and (nextIndexB != startB
                 or len(B) == 1)
            and len(A) > 0
            and len(B) > 0):
            if A[nextIndexA] < B[nextIndexB]:
                nextIndexB = startB
            elif A[nextIndexA] > B[nextIndexB]:
                nextIndexA = startA
            else:   # A[nextIndexA] == B[nextIndexB]:
                nextAPlus = min(nextIndexA + 1, len(A) - 1)
                nextBPlus = min(nextIndexB + 1, len(B) - 1)
                if A[nextAPlus] < B[nextBPlus]:
                    nextIndexA = startA
                elif A[nextAPlus] > B[nextBPlus]:
                    nextIndexB = startB
                else:
                    nextIndexA = startA # hxl: randomly picked this one
                
        return self.findMedian(A, nextIndexA, B, nextIndexB, nextSpan)
        
    def findMedianHelper(self, A, indexA, B, indexB):
        if (len(A) + len(B)) % 2 == 1:
            if len(A) == 0:
                return B[indexB]
            elif len(B) == 0:
                return A[indexA]
            else:
                return min(A[indexA], B[indexB])
        else:
            candidates = A[indexA:indexA + 2] + B[indexB:indexB + 2]
            m = min(candidates)
            candidates.remove(m)
            n = min(candidates)
            return (m + n) / 2.0
         