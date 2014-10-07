# Word Break
# 
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        
        if s in dict:
            return True
        elif len(s) == 0:
            return False
        elif len(dict) == 0:
            return False
        
        candidates = [0]    # hxl: this serves as a ordered stack, with larger elements on top (greedy)
        visited = set()
        
        while len(candidates) > 0:
            startIndex = candidates.pop(-1)
            visited.add(startIndex)
            for word in dict:
                scope = startIndex + len(word)
                if scope == len(s): # hxl: the length is matching
                    if s[startIndex:] in dict:  # hxl: the last word is matching
                        return True
                elif scope < len(s):
                    if (s[startIndex:scope] in dict
                        and scope not in visited):
                        candidates.append(scope)    # hxl: add the start index of the remaining string
                            
        return False
    