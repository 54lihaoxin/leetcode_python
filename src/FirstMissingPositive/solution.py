# First Missing Positive
# 
# Given an unsorted integer array, find the first missing positive integer.
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# Your algorithm should run in O(n) time and uses constant space.


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        # hxl: Given [3,4,-1,1], the idea is, swap the elements until end up with an array like [1, 0, 3, 4],
        #      which the each element is <index + 1>, or 0 if the element is not in the original array.
        #      Negative numbers are replaced 0, and 0 stays as 0. When the swapping is done,
        #      scan the array again for the first 0 that represents the missing positive.
        #      If no 0 is found, then the missing number is 1 larger than the largest / last element in the array.
        #
        #      Extra: what about finding the first two missing positives?
        
        empty = 0
        for i in range(len(A)):
            
            expectedValue = i + 1
            
            # hxl: swap in the same location until it's done 
            while A[i] != expectedValue and A[i] != empty:
                if A[i] < 0:    # hxl: replace negative numbers by 0
                    A[i] = empty
                elif A[i] > 0:
                    if A[i] != expectedValue:
                        if A[i] > len(A):
                            # hxl: if there is any number larger than the length,
                            #      then the missing number must be within the range [1, len(A)]
                            A[i] = empty
                        else:
                            # hxl: A[i] is within the range
                            temp = A[i]
                            if A[i] == A[temp - 1]:
                                # hxl: if the swap target has the expected value already, empty the current one
                                A[i] = empty 
                            else:
                                # hxl: swap two values
                                A[i] = A[temp - 1]
                                A[temp - 1] = temp
                                if A[i] < 1 or A[i] > len(A):
                                    # hxl: the swapped value can be out of range
                                    A[i] = empty
                                    
        # hxl: search for the first 0, which represents the missing positive
        for i in range(len(A)):
            if A[i] == empty:
                return i + 1
            
        # hxl: 0 not found, then we know len(A) + 1 is the one missing
        return len(A) + 1
