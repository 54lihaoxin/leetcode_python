# Longest Consecutive Sequence
# 
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# 
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# 
# Your algorithm should run in O(n) complexity.

 
debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, nums):
        
        if nums == None or len(nums) == 0:
            return 0
        
        r = 0
        countDict = {}
        headSet = set()
        
        for n in nums:
            if ((n in countDict and countDict[n] == 0)
                or n not in countDict):
                if n - 1 not in countDict:
                    countDict[n - 1] = 0
                    headSet.add(n - 1)
                countDict[n] = 1
                if n in headSet:
                    headSet.remove(n)         
        
        if debug: print countDict, headSet
        
        for head in headSet:
            c = 1
            while (head + c in countDict
                   and countDict[head + c] != 0):   # hxl: watch out! next value might exists but it's just a head
                c += 1
            r = max(r, c - 1)   # hxl: c - 1 because c has been incremented before ending the WHILE loop
            if debug: print head, c - 1, r
        
        return r
