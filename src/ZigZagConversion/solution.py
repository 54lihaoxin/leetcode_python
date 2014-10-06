# ZigZag Conversion
# 
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
        
    # @return a ZigZag string
    def convert(self, s, nRows):
        
        # hxl: don't forget the base case!
        if nRows == 1:
            return s
        
        r = ''
        
        for row in range(nRows):
            i = row
            if row == 0 or row == nRows - 1:    # hxl: the first and last row                
                while i < len(s):
                    r += s[i]
                    i += (nRows - 1) * 2
            else:   # hxl: any row not the first or the last: need to add one more character in zig-zag
                while i < len(s):
                    r += s[i]
                    j = i + (nRows - row - 1) * 2
                    if j < len(s):
                        r += s[j]
                    i += (nRows - 1) * 2
            
        return r
                