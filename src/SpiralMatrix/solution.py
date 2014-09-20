# Spiral Matrix
# 
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# For example,
# Given the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 
# You should return [1,2,3,6,9,8,7,4,5].


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        r = []
        remaining = len(matrix) * len(matrix[0])
        
        topLimit = 1    # hxl: because it starts in the first row, so the next limit is row 1 (if there is one)
        bottomLimit = len(matrix) - 1
        leftLimit = 0
        rightLimit = len(matrix[0]) - 1
        curRow = 0
        curColumn = 0
        
        toRight = 0
        toDown = 1
        toLeft = 2
        toUp = 3
        direction = toRight
        
        while remaining > 0:
            if debug: print curRow, curColumn, matrix[curRow][curColumn], r
            r.append(matrix[curRow][curColumn])
            remaining -= 1
            
            # hxl: move the cur pointer
            if direction == toRight:
                if curColumn == rightLimit:
                    rightLimit -= 1
                    direction = (direction + 1) % 4 # hxl: next direction
                    curRow += 1
                else:
                    curColumn += 1
            elif direction == toDown:
                if curRow == bottomLimit:
                    bottomLimit -= 1
                    direction = (direction + 1) % 4 # hxl: next direction
                    curColumn -= 1
                else:
                    curRow += 1
            elif direction == toLeft:
                if curColumn == leftLimit:
                    leftLimit += 1
                    direction = (direction + 1) % 4 # hxl: next direction
                    curRow -= 1
                else:
                    curColumn -= 1
            elif direction == toUp:
                if curRow == topLimit:
                    topLimit += 1
                    direction = (direction + 1) % 4 # hxl: next direction
                    curColumn += 1
                else:
                    curRow -= 1 
        
        return r
        