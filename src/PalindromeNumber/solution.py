# Palindrome Number
# 
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# 
# Some hints:
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# 
# There is a more generic way of solving this problem.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @return a boolean
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        elif x < 10:    # hxl: handle single digit case
            return True
        
        # hxl: learn the number of digits
        t = x
        numDigits = 0        
        while t != 0:
            t /= 10
            numDigits += 1
        
        # hxl: obtain the revers of right half of input x, and cut the right half temp number t
        rev = 0
        i = 0
        t = x            
        while i < numDigits / 2:
            rev = rev * 10 + t % 10
            t /= 10
            i += 1
        
        # hxl: remove the middle digit from t if the number of digit is odd
        if numDigits % 2 == 1:
            t /= 10
            
        return t == rev
