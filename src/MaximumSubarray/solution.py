# Maximum Subarray
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# 
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


debug = True
debug = False


class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        
        sum = 0
        maxSum = A[0]
         
        for n in A:
            if maxSum < n:
                maxSum = n
        
        for i in range(len(A)):
            sum += A[i]
            maxSum = max(sum, maxSum)
            if sum <= 0:
                sum = 0
            
        return maxSum
    