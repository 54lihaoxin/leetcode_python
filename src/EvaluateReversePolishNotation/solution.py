

debug = True
# debug = False


#from classes import ?   # hxl: comment out this line for submission, otherwise Compiler Error on LeetCode

# hxl: for some help, see http://www.mathblog.dk/tools/infix-postfix-converter/

class Solution:
    
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        
        numStack = []
        validOperators = ['+', '-', '*', '/']
        
        for t in tokens:
#             if debug: print t,
            if t in validOperators:
                a = numStack[-2]
                b = numStack[-1]
                numStack = numStack[:-2]
                numStack.append(self.calculate(a, b, t))
            else:
                numStack.append(long(t))
                
        return numStack[0]
    
    def calculate(self, a, b, op):
#         if debug: print a, op, b
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
    