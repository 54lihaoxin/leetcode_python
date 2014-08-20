

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        r = []
        d = {}
        for i in range(0, len(num)):
            complement = target - num[i]
            if d.has_key(complement):
                r.append((d[complement], i))   # hxl: assume there is always a match
            else:
                d[num[i]] = i
        return r

    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        r = {}  # hxl: this is used like a set
        for i in range(0, len(nums) - 2):
            subNums = nums[i+1:]
            twoSums = self.twoSum(subNums, -nums[i])
            for indexTuple in twoSums:
                triple = [nums[i], subNums[indexTuple[0]], subNums[indexTuple[1]]]
                triple.sort()
                r[tuple(triple)] = triple   # hxl: list is unhashable, while tuple is unsortable...
        return r.values()
    