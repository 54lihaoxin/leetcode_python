# Minimum Path Sum
# 
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
        
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):   
        minDict = {}     
        i = len(grid) - 1
        while 0 <= i:
            j = len(grid[0]) - 1
            while 0 <= j:
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    minDict[(i, j)] = grid[i][j]
                elif i == len(grid) - 1 and j < len(grid[0]) - 1:
                    minDict[(i, j)] = grid[i][j] + minDict[(i, j + 1)]
                elif i < len(grid) - 1 and j == len(grid[0]) - 1:
                    minDict[(i, j)] = grid[i][j] + minDict[(i + 1, j)]
                else:
                    minDict[(i, j)] = grid[i][j] + min(minDict[(i + 1, j)], minDict[(i, j + 1)])
                
                if debug: print i, j, self.minDict[(i, j)], self.minDict                
                j -= 1
            i -= 1        
        return minDict[(0, 0)]
    