# Jump Game
# 
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# A = [3,2,1,0,4], return false.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        
        lastBaseIndex = 0
        i = A[lastBaseIndex]
        if i >= len(A) - 1: # hxl: the goal is "reaching the last index"
            return True
        
        # hxl: kepp trying to jump to the farthest place; if it's not a legal jump, 
        #      then reduce the step one by one until going back to the jump spot 
        while i != lastBaseIndex:
            if A[i] > 0:
                lastBaseIndex = i
                i = i + A[i]                
                if i >= len(A) - 1: # hxl: the goal is "reaching the last index"
                    return True
            else:                
                i -= 1
        
        return False
    