

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @return a tuple, (index1, index2); index starts with 0
    def twoSumZeroBased(self, num, target):
        d = {}
        for i in range(0, len(num)):
            complement = target - num[i]
            if d.has_key(complement):
                return (d[complement], i)   # hxl: assume there is always a match
            else:
                d[num[i]] = i
    
    # @return a tuple, (index1, index2); index starts with 1
    def twoSum(self, num, target):
        r = self.twoSumZeroBased(num, target)
        return (r[0] + 1, r[1] + 1)
    