# Roman to Integer
# 
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
# hxl: see this for 1 - 100:
#         http://www.educationoasis.com/curriculum/Math/ff/romannumerals1to100.htm


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
     
    # @return an integer
    def romanToInt(self, s):
        
        units = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        d = {'M' :1000,
             'CM':900,
             'D' :500,
             'CD':400,
             'C' :100,
             'XC':90,
             'L' :50,
             'XL':40,
             'X' :10,
             'IX':9,
             'V' :5,
             'IV':4,
             'I' :1}
        r = 0
        
        for i in range(len(units)):
            while s.startswith(units[i]):                
                s = s[len(units[i]):]
                r += d[units[i]]

        return r   
        