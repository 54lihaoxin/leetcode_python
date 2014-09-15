# Combination Sum
# 
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: 
# [7] 
# [2, 2, 3] 


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.result = []    
    
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        
        candidates.sort()   # hxl: need to sort the candidates to avoid repeated results
        
        for n in candidates:
            self.combination(candidates, target - n, [n])
        
        return self.result
    
    def combination(self, candidates, target, curCombination):
         
        if target == 0:
            self.result.append(curCombination)
        elif target < 0:
            return
        else:
            for n in candidates:
                if curCombination[-1] <= n: # hxl: avoid repeated results 
                    self.combination(candidates, target - n, curCombination + [n])
        