# Subsets
# 
# Given a set of distinct integers, S, return all possible subsets.
# 
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
# 
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


debug = True
debug = False


class Solution:
    
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        
        S.sort()
        return self.sortedSubsets(S)

    def sortedSubsets(self, S):
        r = [[]]    # hxl: empty set is the subset of all set
        
        if len(S) == 1: # hxl: base case
            r.append(S)
            return r
        
        if len(S) > 0:
            smallSet = self.sortedSubsets(S[1:])
            for x in smallSet:
                if len(x) > 0:
                    r.append(x)
                    r.append([S[0]] + x)
            r.append([S[0]])
            
        return r