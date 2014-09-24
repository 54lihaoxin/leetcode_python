# Decode Ways
# 
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
# 
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
# 
# The number of ways decoding "12" is 2.


# from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


# hxl: Think about this problem as a depth first search problem, 
#      which +1 to the result counter when reaching a last node in the path.
#      Save the result of the visited node to avoid unnecessary computation!


class Solution:
    
    def __init__(self):
        self.K_word_VS_V_numDecoding = {}
    
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if s == '0':    # hxl: don't forget this base case!
                return 0
            else:
                return 1
        else:
            # hxl: we will consume the string from the back because we need to consider the a non-0 combine with 0
            r = 0
            if int(s[-1]) != 0:  # hxl: handle cases 1 ~ 9
                word = s[:-1]
                if word not in self.K_word_VS_V_numDecoding:
                    self.K_word_VS_V_numDecoding[word] = self.numDecodings(word)
                r += self.K_word_VS_V_numDecoding[word]
            if 10 <= int(s[-2:]) and int(s[-2:]) <= 26:   # hxl: handle cases 10 ~ 26
                if len(s) == 2:
                    r += 1  # hxl: this is a base case as well: the first two digit in the string
                else:
                    word = s[:-2]
                    if word not in self.K_word_VS_V_numDecoding:
                        self.K_word_VS_V_numDecoding[word] = self.numDecodings(word)
                    r += self.K_word_VS_V_numDecoding[word]
            return r
        