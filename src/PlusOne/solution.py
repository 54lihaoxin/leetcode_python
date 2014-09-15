# Plus One
# 
# Given a non-negative number represented as an array of digits, plus one to the number.
# 
# The digits are stored such that the most significant digit is at the head of the list.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        
        overflow = 0
        
        digits[-1] += 1
        if digits[-1] == 10:
            if len(digits) == 1:
                return [1, 0]
            else:
                digits[-1] = 0
                overflow = 1
        else:
            return digits
        
        i = len(digits) - 2
        
        while overflow > 0:
            
            digits[i] += 1
            
            if digits[i] == 10:
                digits[i] = 0
                overflow = 1
            else:
                overflow = 0
            
            i -= 1 
            
            if i == -1 and overflow == 1:   # hxl: add one more digit to the beginning
                return [1] + digits
            if overflow == 0:
                return digits
            