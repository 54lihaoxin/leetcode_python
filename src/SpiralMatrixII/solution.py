# Spiral Matrix II
# 
# Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @return a list of lists of integer
    def generateMatrix(self, n):
        
        if n == 0:
            return []
        
        matrix = []
        c = 1
        
        # hxl: initialize the matrix
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)
                
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
        
        while c <= n * n:
            if debug: print c, curRow, curColumn, matrix[curRow][curColumn]
            matrix[curRow][curColumn] = c
            c += 1
            
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
                
        return matrix
    