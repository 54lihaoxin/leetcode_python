# Unique Paths
# 
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# 
# Note: m and n will be at most 100.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.cachedResult = {}
    
    # @return an integer
    def uniquePaths(self, m, n):
        
        if (m, n) in self.cachedResult.keys():
            return self.cachedResult[(m, n)]
        else:
            r = 0
            
            # hxl: The base case is 1, not 0!
            if m == 1 and n == 1:
                return 1
            elif m > 1 and n == 1:
                r = self.uniquePaths(m - 1, n)
            elif m == 1 and n > 1:
                r = self.uniquePaths(m, n - 1)
            else:
                r = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
            
            self.cachedResult[(m, n)] = r
            return r
        
