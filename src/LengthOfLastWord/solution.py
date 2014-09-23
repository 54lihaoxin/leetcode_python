# Length of Last Word
# 
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space characters only.
# 
# For example, 
# Given s = "Hello World",
# return 5.

 
debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        
        
        # hxl: Nothing but handling edge cases such as all-whitespace and ending-with-whitespace.
        
        
        if s == None or len(s) == 0:
            return 0
        
        c = 0
        i = len(s) - 1
        
        while 0 <= i and s[i].isalpha() == False:
            i -= 1
        
        while 0 <= i:            
            if s[i].isalpha():
                c += 1
            else:
                break
            i -= 1
                
        return c
