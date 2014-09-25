# Longest Common Prefix
# 
# Write a function to find the longest common prefix string amongst an array of strings.

 
debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @return a string
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ''
        
        prefix = ''
        minLen = len(strs[0])
        
        for word in strs:
            minLen = min(minLen, len(word))
        
        for i in range(minLen):
            c = strs[0][i]
            for word in strs:
                if c != word[i]:    # hxl: found a mismatch, return the current prefix 
                    return prefix
            prefix += c
        return prefix
    