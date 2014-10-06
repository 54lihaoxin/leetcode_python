# Largest Rectangle in Histogram
# 
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# 
# 
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
# 
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param heights, a list of integer
    # @return an integer
    def largestRectangleArea(self, heights):
        
        
        # hxl: this solution is from http://fisherlei.blogspot.com/2012/12/leetcode-largest-rectangle-in-histogram.html
        
        
        s = []
        heights.append(0)
        sum = 0
        
        i = 0
        while i < len(heights):
            print i, heights[i], s, sum
            if (len(s) == 0 or heights[i] > heights[s[-1]]):
                s.append(i)
            else:
                tmp = s.pop(-1)
                k = i
                if len(s) != 0:
                    k = i - s[-1] - 1
                sum = max(sum, heights[tmp] * k)
                i -= 1
            i += 1
        
        return sum
    