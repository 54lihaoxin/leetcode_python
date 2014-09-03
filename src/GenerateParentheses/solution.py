

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    def __init__(self):
        self.result = []
    
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        
        if n == 0:
            return []
        
        self.depthFirstSearch(n, 1, 0, '(')
        
        return self.result
    
    def depthFirstSearch(self, n, nOpen, nClose, curString):
        if nOpen >= nClose: # hxl: existing closing parenthesis cannot be more than the opening ones
            if n > nOpen:
                self.depthFirstSearch(n, nOpen + 1, nClose, curString + '(')
            if n > nClose:
                self.depthFirstSearch(n, nOpen, nClose + 1, curString + ')')
            if n == nClose: # hxl: no need to check n == nOpen since nOpen >= nClose
                self.result.append(curString)
        