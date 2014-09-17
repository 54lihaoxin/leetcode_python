# Search in Rotated Sorted Array
# 
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        pivot = self.searchForPivotPoint(A, 0, len(A) - 1)
        r = self.binarySearch(A, pivot, len(A) - 1, target)
        if r == -1 and 0 < pivot:
            r = self.binarySearch(A, 0, pivot - 1, target)
        return r
    
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
        