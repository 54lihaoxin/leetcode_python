# Find Minimum in Rotated Sorted Array
#  
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param num, a list of integer (not None or empty)
    # @return an integer
    def findMin(self, num):
        
        if len(num) == 1:
            return num[0]
        else:   # hxl: len(num) > 2:
            if num[0] < num[-1]:
                return num[0]
            else:
                return min(self.findMin(num[:len(num) / 2]), self.findMin(num[len(num) / 2:]))
        