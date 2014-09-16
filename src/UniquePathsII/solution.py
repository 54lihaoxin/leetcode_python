# Unique Paths II
# 
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        if obstacleGrid[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] == 1:
            return 0
        
        resultDict = {}
        i = len(obstacleGrid) - 1
        while 0 <= i:
            j = len(obstacleGrid[0]) - 1
            while 0 <= j:
                if obstacleGrid[i][j] == 1: # hxl: has obstacle
                    resultDict[(i, j)] = 0
                else:
                    if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                        resultDict[(i, j)] = 1
                    elif i < len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                        resultDict[(i, j)] = resultDict[(i + 1, j)]
                    elif i == len(obstacleGrid) - 1 and j < len(obstacleGrid[0]) - 1:
                        resultDict[(i, j)] = resultDict[(i, j + 1)]
                    else:
                        resultDict[(i, j)] = resultDict[(i + 1, j)] + resultDict[(i, j + 1)] 
                j -= 1
                # hxl: end of j loop
            i -= 1  
            # hxl: end of i loop
            
        return resultDict[(0, 0)]
        