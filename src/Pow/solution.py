

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        
        x = float(x)    # hxl: In case an integer is given
        
        if n == 0:
            return 1.0
        
        if n < 0:
            return 1.0 / self.pow(x, -n)
        
        t = self.pow(x * x, n / 2)
        if n % 2 == 1:
            return x * t
        else:
            return t
        