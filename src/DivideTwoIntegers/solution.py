

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @return an integer
    def divide(self, dividend, divisor):
        
        # hxl: assume divisor is not 0
        
        if dividend == 0:
            return 0
        elif abs(dividend) < abs(divisor):
            if (dividend > 0 and divisor < 0
                or dividend < 0 and divisor > 0):
                return -1
            else:
                return 0
        elif dividend == divisor:
            return 1
        
        if dividend > 0 and divisor < 0:
            if self.isJMultipleOfK(dividend, divisor) != 0:
                return - self.divide(dividend, -divisor)
            else:
                return - self.divide(dividend, -divisor) - 1
        elif dividend < 0 and divisor > 0:
            if self.isJMultipleOfK(dividend, divisor) != 0:
                return - self.divide(-dividend, divisor)
            else:
                return - self.divide(-dividend, divisor) - 1
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
            
        # hxl: For example, 128 = 5 * (2 ^ 4 + 2 ^ 3 + 2 ^ 0) + 3 = 5 * (16 + 8 + 1) + 3, and 16 + 8 + 1 = 25 
        
        q = 0
        n = dividend
        d = divisor
        
        while n - d > divisor:
            if q != 0:
                n = n - d   # hxl: don't do this in the first loop
            d = divisor
            curQ = 1
            while d << 1 <= n:
                d <<= 1
                curQ <<= 1
            q += curQ
        return q
    
    # @return 0 if not; otherwise, return the efficient
    def isJMultipleOfK(self, j, k):
        a = abs(j)
        b = abs(k)
        while b << 1 <= b:
            b <<= 1
        if a == b:
            return j / k
        else:
            return 0
        