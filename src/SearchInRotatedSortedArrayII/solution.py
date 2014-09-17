# Search in Rotated Sorted Array II
# 
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# Write a function to determine if a given target is in the array.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        
        # hxl: add this IF block to handle cases like [1,1,1,1,1,...,2,......1,1,1,1],
        #      which can only be resolved by brute force
        if A[0] == A[-1]:
            for i in range(len(A)):
                if A[i] == target:
                    return True
            return False
        
        pivot = self.searchForPivotPoint(A, 0, len(A) - 1)
        r = self.binarySearch(A, pivot, len(A) - 1, target)
        if r == -1 and 0 < pivot:
            r = self.binarySearch(A, 0, pivot - 1, target)
        return r != -1
    
    def searchForPivotPoint(self, A, start, end):
        if start == end or A[start] <= A[end]:  # hxl: the only one element or elements are in order
            return start
        else:
            if end - start < 2:    # hxl: two elementes left
                if A[start] <= A[end]:
                    return start
                else:
                    return end
            else:   # hxl: more than two elements
                mid = start + (end - start) / 2
                if A[start] > A[mid]:
                    return self.searchForPivotPoint(A, start, mid)
                else:
                    return self.searchForPivotPoint(A, mid, end)
    
    def binarySearch(self, A, start, end, target):
        mid = start + (end - start) / 2
        if end - start < 2: # at most two elements left
            if A[start] == target:
                return start
            elif A[end] == target:
                return end
            else:
                return -1   # hxl: not found
        if A[mid] == target:
            return mid
        elif target < A[mid]:
            return self.binarySearch(A, start, mid, target)
        else:
            return self.binarySearch(A, mid, end, target)
        