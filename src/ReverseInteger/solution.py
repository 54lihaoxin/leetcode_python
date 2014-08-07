

class Solution:
    
    # @return an integer
    def reverse(self, x):
        # hxl: This is extended slice syntax. It works by doing [begin:end:step]
        #       - by leaving begin and end off and specifying a step of -1, it reverses a string.
        r = long(str(abs(x))[::-1]) 
        return r if x >= 0 else -r
        