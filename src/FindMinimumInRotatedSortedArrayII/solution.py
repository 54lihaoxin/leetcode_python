# Find Minimum in Rotated Sorted Array II
#  
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# The array may contain duplicates.


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        
        
        # hxl: It has to take O(n) time if duplicates are allowed. 
        
        
        minNum = num[0]
        for n in num:
            minNum = min(minNum, n)
        return minNum
        