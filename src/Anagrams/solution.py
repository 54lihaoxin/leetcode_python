

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        r = []
        d = {}
        for s in strs:
            t = []
            for c in s:
                if c.isalpha():
                    t.append(c)
            t.sort()
            t = tuple(t)
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]
                
        for s in d.values():
            if len(s) > 1:
                r = r + s
            
        return r
    