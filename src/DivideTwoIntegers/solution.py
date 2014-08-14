

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @return an integer
    def divide(self, dividend, divisor):
        
        # hxl: assume divisor is not 0
        
        if dividend == 0:
            return 0
        
        if dividend > 0 and divisor < 0:
            return - self.divide(dividend, -divisor)
        elif dividend < 0 and divisor > 0:
            return - self.divide(-dividend, divisor)
        elif dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        
        return dividend / divisor
    