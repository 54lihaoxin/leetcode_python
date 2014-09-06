# Subsets II
# 
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
# 
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


debug = True
debug = False


class Solution:
    
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        
        S.sort()
        return self.sortedSubsetsWithDup(S)

    def sortedSubsetsWithDup(self, S):
        r = [[]]    # hxl: empty set is the subset of all set
        
        if len(S) == 1: # hxl: base case
            r.append(S)
            return r
        
        if len(S) > 0:
            smallSet = self.sortedSubsetsWithDup(S[1:])
            for x in smallSet:
                if len(x) > 0:
                    if x not in r:
                        r.append(x)
                    a = [S[0]] + x
                    if a not in r:
                        r.append(a)
            if [S[0]] not in r:
                r.append([S[0]])
            
        return r
    