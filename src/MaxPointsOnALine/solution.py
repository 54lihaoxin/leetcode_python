

debug = True
debug = False


from classes import Point   # hxl: comment out this line for submission
from itertools import groupby
from operator import itemgetter


class Solution:
    
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        xDict = {}
        yDict = {}
        
        for p in points:
            if xDict.has_key(p.x) == False:
                 xDict[p.x] = []
            xDict[p.x].append(p.y)
        
            if yDict.has_key(p.y) == False:
                 yDict[p.y] = []
            yDict[p.y].append(p.x)
        
        if debug: print 'xDict:', xDict
        if debug: print 'yDict:', yDict
        
        maxLen = max(0, self.maxConsecutiveNumbersInDict(xDict))
        return max(maxLen, self.maxConsecutiveNumbersInDict(yDict))
    
    def maxConsecutiveNumbersInDict(self, dict):
        maxLen = 0
        for k in dict.keys():
            if len(dict[k]) > maxLen:
                dict[k].sort()
                maxLen = max(maxLen, self.maxConsecutiveNumbers(dict[k]))    
        return maxLen
        
    def maxConsecutiveNumbers(self, nums):
        maxLen = 0
        # hxl: TODO: make a faster implementation yourelf
        for k, g in groupby(enumerate(nums), lambda (i,x):x-i):
            maxLen = max(maxLen, len(map(itemgetter(1), g)))
        return maxLen
    