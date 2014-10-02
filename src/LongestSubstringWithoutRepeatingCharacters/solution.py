# Longest Substring Without Repeating Characters
#  
# Given a string, find the length of the longest substring without repeating characters. 
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
    
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        if s == None:
            return 0
        elif len(s) < 1:
            return len(s)
        else:
            r = 0
            charDict = {}   # hxl: K: char; V: index of char in s
            toBeRemoved = 0
            
            for i in range(len(s)):
                char = s[i]
                index = charDict.get(char)
                if index != None:   # hxl: current character has been in the current word
                    r = max(r, len(charDict.keys()))
                    for j in range(toBeRemoved, index): 
                        # hxl: remove the records of all characters before the last occurrence of current duplicate
                        charToRemove = s[j] 
                        indexToRemove = charDict.get(charToRemove)
                        if indexToRemove < index: # hxl: don't remove the record of characters that is after the duplicate
                            charDict.pop(charToRemove)
                    toBeRemoved = index + 1 # hxl: record of character at "index" will be updated since it's the duplicate 
                charDict[char] = i
                if debug: print index, s[i], i, len(charDict), s[:i], charDict
                
            r = max(r, len(charDict.keys()))    # hxl: this is for the case that the longest string is at the end
            
            return r
        