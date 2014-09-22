# Restore IP Addresses
# 
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.result = set()
    
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.depthFirstSearch(s, '', 4)
        return list(self.result)    
    
    # @param s, a string
    def depthFirstSearch(self, remaining, s, level):
        if level == 0:
            self.result.add(s[1:])
        else:
            for i in [1, 2, 3]: # hxl: i represents the length of the current word
                newRemaining = remaining[:-i]
                curStr = remaining[-i:]
                nextLevel = level - 1
                
                if (nextLevel <= len(newRemaining) and len(newRemaining) <= nextLevel * 3
                        and int(curStr) <= 255
                        and ((i == 1)
                             or (i == 2 and curStr[0] != '0')
                             or (i == 3 and curStr[0] != '0'))):
                    self.depthFirstSearch(newRemaining, '.' + curStr + s, nextLevel)
                        