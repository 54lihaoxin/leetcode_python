# Container With Most Water
# 
# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.result = []    
    
    # @return an integer
    def maxArea(self, heights):
        
        area = 0
        left = 0
        right = len(heights) - 1
        
        while left <= right:
            area = max(area, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area
