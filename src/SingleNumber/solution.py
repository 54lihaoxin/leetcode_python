
class Solution:
    
    # @param numbers, a list of integer
    # @return an integer
    def singleNumber(self, numbers):
        numDict = {}
        for n in numbers:
            if numDict.has_key(n):
                numDict.pop(n)
            else:
                numDict[n] = n   
        return numDict.keys()[0]
    