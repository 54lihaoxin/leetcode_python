

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    # @return a list of lists of integers
    def combine(self, n, k):
        
        r = []
        
        if k == 1:
            for i in range(1, n + 1):
                r.append([i])
        
        i = n
        while i != 1:
            t = self.combine(i - 1, k - 1)
            for l in t:
                r.append(l + [i])   # hxl: switching l and [i] will end up with individual result list in reverse order
            i -= 1
        
        return r
