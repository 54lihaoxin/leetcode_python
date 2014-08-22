

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        # hxl: Python specific implementation
        try:
            float(s)
            return True
        except ValueError:
            return False
        