# Single Number II
# 
# Given an array of integers, every element appears three times except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param numbers, a list of integer
    # @return an integer
    def singleNumber(self, numbers):
        numDict = {}
        for n in numbers:
            if numDict.has_key(n):
                numDict[n] += 1
                if numDict[n] == 3:
                    numDict.pop(n)
            else:
                numDict[n] = 1  
        return numDict.keys()[0]
    