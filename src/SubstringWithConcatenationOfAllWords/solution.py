# Substring with Concatenation of All Words
# 
# You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
# 
# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# 
# You should return the indices: [0,9].
# (order does not matter).


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        
        wordLen = len(L[0])
        if wordLen > len(S):
            return []
        
        matchDict = {}
        matchList = []
        for i in range(len(S) - wordLen + 1): 
            curWord = S[i:i + wordLen]
            if debug: print curWord
            if curWord in L:
                if curWord not in matchDict:
                    matchDict[curWord] = []
                matchDict[curWord].append(i)
                matchList.append(i)
        return self.listOfValidSubstringStartIndex(S, L, matchList)
        
    def listOfValidSubstringStartIndex(self, S, L, candidates):
        
        if debug: print candidates
        if len(candidates) == 1:
            return candidates
        
        r = []
        wordLen = len(L[0])
        
        for i in range(len(candidates) - len(L) + 1):
            curWord = S[candidates[i]:candidates[i] + wordLen]
            remaining = list(L)
            remaining.remove(curWord)
            j = 1
            while j < len(L) and j < len(candidates):
                nextIndex = candidates[i] + j * wordLen
                if debug: print i, j, nextIndex
                if nextIndex in candidates:
                    curWord = S[nextIndex:nextIndex + wordLen]
                    if curWord in remaining:
                        remaining.remove(curWord)
                else:
                    break
                j += 1
            if len(remaining) == 0:
                r.append(candidates[i])
                
        return r
        