

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        a = s.split()
        a.reverse()
        r = ''
        for w in a:
            r += w + ' '
        r = r[:-1]
        return r
    