# Combination Sum II
# 
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
# A solution set is: 
# [1, 7] 
# [1, 2, 5] 
# [2, 6] 
# [1, 1, 6] 


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.result = []
        self.resultSet = set()      # hxl: for eleminating repeated result
        self.combinationSet = set() # hxl: for reducing repeated search
    
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        
        candidates.sort()   # hxl: need to sort the candidates to avoid repeated results
        self.combination(candidates, target, [])
        return self.result
    
    def combination(self, candidates, target, curCombination):
        
        if tuple(candidates + [0] + curCombination) not in self.combinationSet:
            self.combinationSet.add(tuple(candidates + [0] + curCombination))
            
            if target == 0 and tuple(curCombination) not in self.resultSet:
                self.result.append(curCombination)
                self.resultSet.add(tuple(curCombination))
            elif len(candidates) > 0 and target > 0 and target >= candidates[0]:
                self.combination(candidates[1:], target, curCombination)
                self.combination(candidates[1:], target - candidates[0], curCombination + [candidates[0]])
        