# String to Integer (atoi)
# 
# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
# 
# spoilers alert... click to show requirements for atoi.
# 
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# 
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


debug = True
debug = False


from CommonClasses import *


class Solution:
    
    # @return an integer
    def atoi(self, str):
        
        if str == None or len(str) == 0:
            return 0
        
        newStr = ''
        sign = 1
        
        while str[0] == ' ':
            str = str[1:]
        
        if len(str) > 1 and str[0] in '-+':
            if str[0] == '-':
                sign = -1
            str = str[1:]
            
        if len(str) == 0:
            return 0
                
        for c in str:
            if c in '1234567890':
                newStr += c
            else:
                break
        
        if len(newStr) == 0:
            return 0
        
        if sign == 1:
            # hxl: OJ doesn't allow sys.maxint... so hard code max of int as 2147483647 here  
            return min(2147483647, long(newStr))
        else:
            return max(-2147483648, -long(newStr))
    