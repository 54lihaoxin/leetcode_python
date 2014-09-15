# Pascal's Triangle II
# 
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @return a list of integers
    def getRow(self, rowIndex):
        
        r = [1]
        
        if rowIndex == 0:
            return r
        else:
            for i in range(0, rowIndex):
                lastLine = r
                thisLine = []
                for j in range(len(lastLine) + 1):
                    if j == 0:
                        thisLine.append(lastLine[0])
                    elif j == len(lastLine):
                        thisLine.append(lastLine[-1])
                    else:
                        thisLine.append(lastLine[j - 1] + lastLine[j])
                r = thisLine
            return r
        