# Letter Combinations of a Phone Number
# 
# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.numDict = {'2':'abc',
                        '3':'def',
                        '4':'ghi',
                        '5':'jkl',
                        '6':'mno',
                        '7':'pqrs',
                        '8':'tuv',
                        '9':'wxyz'}
    
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        
        r = self.combinations(digits)
        
        if len(r) == 0:
            r = ['']
                
        return r
    
    # @return a list of strings, [s1, s2]
    def combinations(self, digits):
        
        r = []
        
        if len(digits) == 0:
            return r
        
        sub = self.combinations(digits[1:])
        
        for char in self.numDict[digits[0]]:
            if len(digits) == 1:
                r.append(char)
            else:
                for s in sub:
                    r.append(char + s)
        
        return r
    