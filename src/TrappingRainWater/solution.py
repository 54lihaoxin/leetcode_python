# Trapping Rain Water
# 
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


# import CommonClasses    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        
        if A == None or len(A) == 0:
            return 0
        
        areaOfWaterAndContainer = 0
        areaOfContainer = 0
        leftMostDict = {}
        rightMostDict = {}   
        
        # hxl: obtain the left most and right most bar of each height
        for i in range(len(A)):
            areaOfContainer += A[i]
            if A[i] in leftMostDict:
                leftMostDict[A[i]] = min(i, leftMostDict[A[i]])
            else:
                leftMostDict[A[i]] = i            
            if A[i] in rightMostDict:
                rightMostDict[A[i]] = max(i, rightMostDict[A[i]])
            else:
                rightMostDict[A[i]] = i
        heights = list(leftMostDict.keys())
        heights.sort()  # hxl: We don't need to do this O(nlogn) sort to get the max height, but I do it anyway for debugging
        if debug: print heights, leftMostDict, rightMostDict
        
        # hxl: add the area on the left of max height area
        i = 0
        prevMax = A[i]
        while i < leftMostDict[heights[-1]]:
            prevMax = max(prevMax, A[i])
            areaOfWaterAndContainer += prevMax
            i += 1
        
        # hxl: add the max height area
        areaOfWaterAndContainer += heights[-1] * (rightMostDict[heights[-1]] - leftMostDict[heights[-1]] + 1)
        
        # hxl: add area on the right of the max height area (scan from right to left)
        i = len(A) - 1
        prevMax = A[i]
        while rightMostDict[heights[-1]] < i:
            prevMax = max(prevMax, A[i])
            areaOfWaterAndContainer += prevMax
            i -= 1
        
        if debug: print areaOfWaterAndContainer, areaOfContainer
        return areaOfWaterAndContainer - areaOfContainer
