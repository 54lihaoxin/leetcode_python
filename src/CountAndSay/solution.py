# Count and Say
# 
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# 
# Note: The sequence of integers will be represented as a string.


# from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @return a string
    def countAndSay(self, n):
        
        r = '1'
        temp = ''
        
        while n > 1:            
            for i in range(len(r)):
                if i == 0:
                    lastChar = r[i]
                    c = 1
                else:
                    if lastChar == r[i]:
                        c += 1
                    else:
                        temp += str(c) + lastChar
                        lastChar = r[i]
                        c = 1
                if i == len(r) - 1: # hxl: don't forget to write after reading the last digit
                    temp += str(c) + lastChar
            r = temp
            temp = ''
            n -= 1
            
        return r
