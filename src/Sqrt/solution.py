

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        
        if x == 0 or x == 1:
            return x
        
        r = 0
        low = 0
        high = x
        n = long(x)
        n = n / 2
        
        while low < n and n < high: 
            if debug: print low, n, high, '^', n * n
            sq = n * n
            if sq == x:
                return n
            elif sq > x:
                high = n
                n = max(low + (n - low) / 2, low + 1)
            elif sq < x:
                low = n
                n = min(n + (high - n) / 2, high - 1)
        
        # hxl: it's possible that n is off by 1 after low and high converge... 
        if n * n > x:
            return low
        else:
            return n
