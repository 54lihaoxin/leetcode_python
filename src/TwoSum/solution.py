

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(0, len(num)):
            indexA = target - num[i]
            if d.has_key(num[i]):
                return (d[num[i]], i + 1)   # hxl: assume there is always a match
            else:
                d[target - num[i]] = i + 1
        