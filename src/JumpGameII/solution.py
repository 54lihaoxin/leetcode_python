# Jump Game II
# 
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# For example:
# Given array A = [2,3,1,1,4]
# 
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        
        # hxl: this solution greedily looks for the next maximum jump
        
        left = 0
        right = A[left]
        maxStepIndex = right
        r = 0
        
        if len(A) <= 1:
            return 0
        elif right >= len(A) - 1: # hxl: the goal is "reaching the last index"
            return 1
        
        while right < len(A) - 1:
            
            if left == right:
                return 0
            
            for i in range(left + 1, right + 1):
                if maxStepIndex + A[maxStepIndex] < i + A[i]:
                    maxStepIndex = i
            
            left = maxStepIndex
            right = left + A[left]
            maxStepIndex = right
            r += 1
            
        return r + 1    # hxl: because the actual last step was skipped
    