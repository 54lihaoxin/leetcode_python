# Maximum Product Subarray
# 
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.


# from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        
        if debug: print A
        
        if len(A) == 1:
            return A[0]
        
        # hxl: if there is any zero in the array, calculate the product for each part divided by zero
        lastIndexOfZero = -1    # hxl: assume a zero before the first element
        maxProduct = A[0]
        for i in range(len(A)):
            if A[i] == 0 and i - lastIndexOfZero > 0:
                if i == 0:
                    maxProduct = 0
                elif i - lastIndexOfZero == 1:  # hxl: handles the consecutive zero's case
                    maxProduct = max(0, maxProduct)
                else:
                    maxProduct = max(0, maxProduct, self.maxProduct(A[lastIndexOfZero + 1:i]))
                lastIndexOfZero = i
            elif i == len(A) - 1 and lastIndexOfZero > -1 and A[i] != 0:
                # hxl: there is a zero but the ending number of the array is not zero
                maxProduct = max(0, maxProduct, self.maxProduct(A[lastIndexOfZero + 1:i + 1]))
        
        # hxl: all math done in sub-calls
        if lastIndexOfZero != -1:
            return maxProduct
        
        # hxl: the following code is for array that has no zero in it
        leftMostNegative = -1
        rightMostNegative = len(A)
        leftNegativeProduct = 1     # hxl: such as -24 for array [1, 2, 3, -4, ...]
        rightNegativeProduct = 1    # hxl: such as -24 for array [..., -4, 3, 2, 1]
        product = 1
        
        for i in range(len(A)):
            if A[i] < 0:
                if leftMostNegative == -1:
                    leftMostNegative = i
                    leftNegativeProduct = product * A[i]
                rightMostNegative = i
                rightNegativeProduct = 1    # hxl: reset the right product
            rightNegativeProduct *= A[i]
            product *= A[i]
            
        if debug: print leftMostNegative, rightMostNegative, leftNegativeProduct, rightNegativeProduct
        
        if product >= 0:
            return product
        else:   # hxl: either discards the left side of the right side 
            return max(product / leftNegativeProduct, product / rightNegativeProduct) 
                
