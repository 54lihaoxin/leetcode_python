# Longest Valid Parentheses
# 
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# 
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# 
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
    
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        
        
        # hxl: The idea of this solution is merge the valid parentheses as much as possible.
        #      The code here works but too ugly due to all the IF / ELSE cases.
        #      Could be refactored by not holding too much information in the stack.
        #      This problem can also be solved be using 1-dimension dynamic programming.
        
        
        stack = []
        
        for c in s:
            if debug: print c, stack
            if c == '(':
                stack.append(c)
            else:   # hxl: ')'
                if len(stack) > 0:
                    if stack[-1] == '(':    # hxl: now we have a pair
                        stack.pop(-1)                        
                        if len(stack) > 0:
                            if stack[-1] == '(' or stack[-1] == ')':                                
                                stack.append(2)
                            else:
                                count = stack.pop(-1) + 2
                                while (len(stack) > 0
                                       and stack[-1] != '(' and stack[-1] != ')'):
                                    count += stack.pop(-1)
                                stack.append(count)
                        else:
                            stack.append(2)
                    elif stack[-1] == ')':
                        stack.append(c)
                    else:   # hxl: it's a number
                        if len(stack) == 1:
                            stack.append(c)
                        else:
                            if stack[-2] == '(':
                                count = stack.pop(-1) + 2
                                stack.pop(-1)
                                while (len(stack) > 0
                                       and stack[-1] != '(' and stack[-1] != ')'):
                                    count += stack.pop(-1)
                                stack.append(count)
                            else:   # hxl: ')'
                                stack.append(c)
                else:
                    stack.append(c)
        
        maxCount = 0
        for element in stack:
            if element != '(' and element != ')':
                maxCount = max(element, maxCount)
        
        return maxCount
    