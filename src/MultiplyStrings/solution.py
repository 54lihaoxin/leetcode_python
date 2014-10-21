# Multiply Strings
#  
# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note: The numbers can be arbitrarily large and are non-negative.


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    def __init__(self):
        self.multiplicationCache = {}
    
    # @param a, a string
    # @param b, a string
    # @return a string
    def add(self, a, b):
        
        # hxl: longer might have the same length as shorter
        longer = a
        shorter = b
        if len(a) < len(b):
            longer = b
            shorter = a
        
        sum = ''
        carry = 0
        
        # hxl: consume the shorter string
        for i in range(1, len(shorter) + 1):
             digitA = int(longer[-i])
             digitB = int(shorter[-i])
             sumNum = digitA + digitB + carry
             sum = str(sumNum % 10) + sum
             carry = sumNum / 10
        
        # hxl: consume the rest of the longer string
        for i in range(len(shorter) + 1, len(longer) + 1):
            sumNum = int(longer[-i]) + carry
            sum = str(sumNum % 10) + sum
            carry = sumNum / 10
        
        # hxl: don't forget about the carry
        if carry > 0:
            sum = str(carry) + sum
        
        return sum
        
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        
        r = self.multiplicationCache.get((num1, num2))
        
        if r != None:
            return r
        elif num1 == '0' or num2 == '0':
            return '0'
        elif len(num2) == 1:
            num2 = int(num2)
            carry = 0
            i = len(num1) - 1
            r = ''
            while 0 <= i:
                digit = int(num1[i])
                calculate = digit * num2 + carry
                carry = calculate / 10
                r = str(calculate % 10) + r
                i -= 1
            if carry > 0:
                r = str(carry) + r
            self.multiplicationCache[(num1, num2)] = r
            return r
        else:   # hxl: split num2 digit by digit like we do the daily multiplication
            sum = '0'
            i = len(num2) - 1
            zeros = 0
            while 0 <= i:
                product = self.multiply(num1, num2[i])
                for j in range(zeros):
                    product += '0'
                sum = self.add(sum, product)
                zeros += 1
                i -= 1
#             self.multiplicationCache[(num1, num2)] = sum    # hxl: no need to cache this result
            return sum
        
#     # @param num1, a string
#     # @param num2, a string
#     # @return a string
#     def multiply(self, num1, num2):
#         
#         # hxl: this solution takes advantage of the Python feature...
#         
#         return str(long(num1) * long(num2))
                