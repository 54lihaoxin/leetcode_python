

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        
        d = {0:0, 1:1, 2:2}

        for i in range(n + 1):
            if i not in d:
                d[i] =  d[i - 1] + d[i - 2]
            if i - 2 in d:  # hxl: We don't need this cached result any more
                d.pop(i - 2)
            if n in d:
                return d[n]
    