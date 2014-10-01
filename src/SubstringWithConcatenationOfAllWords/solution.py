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
        
        r = []
        wordLen = len(L[0])
        windowSize = wordLen * len(L)
        i = 0
        matchIndex = 0
        matchDict = {}
        
        while i <= len(S) - windowSize:
            while matchIndex <= i + windowSize - wordLen:
                curWord = S[matchIndex:matchIndex + wordLen]
                if curWord in L:
#                     print matchIndex, S[matchIndex:matchIndex + wordLen]
                    if curWord not in matchDict:
                        matchDict[curWord] = set()
                    matchDict[curWord].add(matchIndex)
                matchIndex += 1
            if self.containAllSubstrings(i, matchDict, L):
                r.append(i)
            i += 1
#         print r, matchDict
        return r
    
    def containAllSubstrings(self, i, d, L):
        
        wordLen = len(L[0])
        remaining = list(L)
        
        for j in range(len(L)):
            k = i + j * wordLen
            for word in d.keys():
                if k in d[word] and word in remaining:
                    remaining.remove(word)
                    break
        
        return len(remaining) == 0
    