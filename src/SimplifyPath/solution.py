# Simplify Path
#  
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# 
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


# from CommonClasses import * # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        
        components = path.split('/')
        
        i = 0
        
        while i < len(components):
            if components[i] == '' or components[i] == '.':
                components.pop(i)
            elif components[i] == '..':
                if i == 0:
                    components.pop(i)
                else:
                    components.pop(i)
                    components.pop(i - 1)
                    i -= 1
            else:
                i += 1
        
        r = '/'
            
        if len(components) > 0:
            r = ''
            for c in components:
                r += '/' + c
            
        return r
    