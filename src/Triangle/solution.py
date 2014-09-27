# Triangle
# 
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.resultDict = {}
    
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        return self.getMin(triangle, 0, 0)
    
    def getMin(self, triangle, level, index):
        
        if (level, index) in self.resultDict:
            return self.resultDict[(level, index)]
        
        curLv =  triangle[level]
        
        if level == len(triangle) - 1:
            return curLv[index]
        else:
            # hxl: need to cache the result to avoid repeated computation!
            self.resultDict[(level, index)] = min(curLv[index] + self.getMin(triangle, level + 1, index),
                                                  curLv[index] + self.getMin(triangle, level + 1, index + 1))
            return self.resultDict[(level, index)]
        