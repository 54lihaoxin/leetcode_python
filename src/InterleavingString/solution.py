# Interleaving String
# 
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
# 
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
# 
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
     
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        
        
        # hxl: This is a dynamic programming solution inspired by this article:
        #         http://blog.csdn.net/u011095253/article/details/9248073
        #      Fill out the matrix by hand to help understanding how it works!
        
        
        # hxl: watch out for corner cases
        if s1 == None or s2 == None or s3 == None:
            return False
        elif len(s1) + len(s2) != len(s3):
            return False
        elif len(s1) == 0:
            return s2 == s3
        elif len(s2) == 0:
            return s1 == s3
        
        # hxl: initialize a matrix for DP
        dp = []        
        for i in range(len(s1) + 1):
            line = []
            for j in range(len(s2) + 1):
                line.append(0)
            dp.append(line)
        
        dp[0][0] = 1
        
        # hxl: initialize the first column for s1
        for i in range(len(s1) + 1):
            if (dp[i - 1][0] == 1
                and s1[i - 1] == s3[i - 1]):
                dp[i][0] = 1     
        
        # hxl: initialize the first row for s2
        for i in range(len(s2) + 1):
            if (dp[0][i - 1] == 1
                and s2[i - 1] == s3[i - 1]):
                dp[0][i] = 1
        
        # hxl: build the path
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if ((s1[i - 1] == s3[i + j - 1] and dp[i - 1][j] == 1)
                    or 
                    ((s2[j - 1] == s3[i + j - 1] and dp[i][j - 1] == 1))):
                    dp[i][j] = 1
                    
        return dp[len(s1)][len(s2)] == 1
    