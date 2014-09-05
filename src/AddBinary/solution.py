

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        r = ''
        overflow = 0
        for i in range(max(len(a), len(b))):
            digitA = 0
            digitB = 0
            indexA = len(a) - i - 1
            indexB = len(b) - i - 1
            if indexA >= 0:
                digitA = int(a[indexA])
            if indexB >= 0:
                digitB = int(b[indexB])
            t = int(digitA) + int(digitB) + overflow
            if t > 1:
                overflow = 1
            else:
                overflow = 0
            r = str(t % 2) + r
        
        if overflow == 1:
            r = '1' + r
        
        return r
    