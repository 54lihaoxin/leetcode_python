# Integer to Roman
# 
# Given an integer, convert it to a roman numeral.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
# hxl: see this for 1 - 100:
#         http://www.educationoasis.com/curriculum/Math/ff/romannumerals1to100.htm


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
     
    # @return a string
    def intToRoman(self, num):
        
        r = ''
        d = {1000:'M',
             900:'CM',
             500:'D',
             400:'CD',
             100:'C',
             90:'XC',
             50:'L',
             40:'XL',
             10:'X',
             9:'IX',
             5:'V',
             4:'IV',
             1:'I'}
        units = d.keys()
        units.sort()
        units.reverse()
        
        i = 0
        while num != 0:
            a = num / units[i]
            num -= a * units[i]
            for j in range(a):
                r += d[units[i]]
            i += 1
                
        return r
                
        