# Rotate Image
# 
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Follow up:
# Could you do this in-place?
# 
# hxl: The origin of the image of at the top-left corner 
# 
# Input:      [[1,2],[3,4]]
# Expected:   [[3,1],[4,2]]


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        
        # hxl: only loop through the top-left 1/4 square corner of the image
        for i in range(int(math.ceil(len(matrix) / 2.0))):
            for j in range(int(math.floor(len(matrix[i]) / 2.0))):
                # hxl: in the inner loop range, if use ceil instead of floor, 
                #        middle elements will be rotated one more time while n is odd
                self.rotatePosition(matrix, (i, j))
        
        return matrix
    
    def rotatePosition(self, matrix, (i, j)):
        
        n = len(matrix)
        temp = matrix[i][j]
        
        iLowerLeft = n - 1 - j
        jLowerLeft = i
        matrix[i][j] = matrix[iLowerLeft][jLowerLeft]
        
        iLowerRight = n - 1 - i
        jLowerRight = n - 1 - j
        matrix[iLowerLeft][jLowerLeft] = matrix[iLowerRight][jLowerRight]
        
        iTopRight = j
        jTopRight = n - 1 - i
        matrix[iLowerRight][jLowerRight] = matrix[iTopRight][jTopRight]
        
        matrix[iTopRight][jTopRight] = temp
        