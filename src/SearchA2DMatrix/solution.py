# Search a 2D Matrix
# 
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# 
# Given target = 3, return true.


debug = True
# debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        
        # hxl: this is nothing more than a binary search
        
        totalLen = len(matrix) * len(matrix[0])
        cur = totalLen / 2
        low = 0
        high = totalLen - 1
        
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
                
        while low < high:
            (row, column) = self.getMatrixPositionFromLinearIndex(matrix, cur)
            
            if debug: print 'matrix[{0}][{1}] = {2} / {3} ~ {4} ~ {5}'.format(row, column, matrix[row][column], low, cur, high)
            
            if target < matrix[row][column]:
                high = max(0, cur - 1)
            elif matrix[row][column] < target:
                low = min(cur + 1, totalLen - 1)
            else:
                return True
            
            cur = low + (high - low) / 2
            
            if debug: print '\t {3} ~ {4} ~ {5}'.format(row, column, matrix[row][column], low, cur, high)
            
            if high - low <= 1: # hxl: this is kind of like base case handling
                (rowLow, columnLow) = self.getMatrixPositionFromLinearIndex(matrix, low)
                (rowHigh, columnHigh) = self.getMatrixPositionFromLinearIndex(matrix, high)
                return matrix[rowLow][columnLow] == target or matrix[rowHigh][columnHigh] == target
        
        return False
    
    def getMatrixPositionFromLinearIndex(self, matrix, index):
        row = index / len(matrix[0])
        column = index % len(matrix[0])
        return (row, column)
    