# Pascal's Triangle
# 
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @return a list of lists of integers
    def generate(self, numRows):
        
        r = [[1]]
        
        if numRows == 0:
            return []
        if numRows == 1:
            return r
        else:
            for i in range(1, numRows):
                lastLine = r[-1]
                thisLine = []
                for j in range(len(lastLine) + 1):
                    if j == 0:
                        thisLine.append(lastLine[0])
                    elif j == len(lastLine):
                        thisLine.append(lastLine[-1])
                    else:
                        thisLine.append(lastLine[j - 1] + lastLine[j])
                r.append(thisLine)
            return r
        