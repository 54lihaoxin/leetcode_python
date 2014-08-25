

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        
        s = s.lower()   # hxl: don't forget to convert the case
        
        if len(s) == 0: # hxl: special case handling
            return True
        
        i = 0
        j = len(s) - 1
        
        while i <= j:   # hxl: match forward
            didFoundMatch = False
            if s[i].isalnum():
                while i <= j and didFoundMatch == False:    # hxl: match backward
                    if s[j].isalnum():
                        if s[i] != s[j]:
                            return False
                        else:
                            didFoundMatch = True
                            i += 1
                            j -= 1
                            break
                    else:   # hxl: skip none alphanumeric characters
                        j -= 1
            if didFoundMatch == False:
                i += 1
            
        return True
    