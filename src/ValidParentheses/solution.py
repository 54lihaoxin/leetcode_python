

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @return a boolean
    def isValid(self, s):
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if (len(stack) == 0
                    or c == ')' and stack[-1] != '('
                    or c == '}' and stack[-1] != '{'
                    or c == ']' and stack[-1] != '['):
                    return False
                else:
                    stack = stack[:-1]
        return len(stack) == 0
    