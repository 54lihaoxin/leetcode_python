

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission

# hxl: see http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm 

class Solution:
    
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        
        if len(haystack) < len(needle):
            return None
        if len(needle) == 0:    # hxl: an empty string is always leading...
            return haystack
        
        m = 0
        nextStartIndex = 0
        
        # hxl: pay attention to the boundary!
        #        len(haystack) - len(needle) could be 0!
        while m <= len(haystack) - len(needle):
            for i in range(0, len(needle)):
                if haystack[m + i] == needle[i]:
                    if i != 0 and nextStartIndex == m:
                        nextStartIndex = i
                    if i == len(needle) - 1:
                        # hxl: return the rest of haystack
                        return haystack[m:]
                else:
                    break;
            if m < nextStartIndex:
                m = nextStartIndex
            else:
                m += 1
                nextStartIndex = m
                
        return None
    