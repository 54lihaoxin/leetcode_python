# Remove Duplicates from Sorted Array II
# 
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array A = [1,1,1,2,2,3],
# 
# Your function should return length = 5, and A is now [1,1,2,2,3].


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        if len(A) < 3:
            return len(A)
        
        writeIndex = 0
        curInfo = (A[0] - 1, 1) # hxl: pretend there is one more small number before the array
        
        for readIndex in range(len(A)):
            
            curNum = curInfo[0]
            curNumCount = curInfo[1]
            
            if A[readIndex] == curNum:
                if curNumCount < 2:
                    A[writeIndex] = A[readIndex]
                    writeIndex += 1
                curInfo = (A[readIndex], curNumCount + 1)
            else:
                A[writeIndex] = A[readIndex]
                writeIndex += 1
                curInfo = (A[readIndex], 1)
        
        return writeIndex
    