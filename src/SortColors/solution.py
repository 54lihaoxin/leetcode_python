# Sort Colors
# 
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# click to show follow up.
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# 
# Could you come up with an one-pass algorithm using only constant space?


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        
        if len(A) < 2:
            return
        
        red = 0
        white = 1
        blue = 2
        redCount = 0
        whiteCount = 0
        blueCount = 0
        
        for i in range(len(A)):
            if A[i] == red:
                redCount += 1
            elif A[i] == white:
                whiteCount += 1
            elif A[i] == blue:
                blueCount += 1
        for i in range(redCount):
            A[i] = red
        for i in range(redCount, redCount + whiteCount):
            A[i] = white
        for i in range(redCount + whiteCount, len(A)):
            A[i] = blue

            