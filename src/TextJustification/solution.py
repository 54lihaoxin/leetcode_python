# Text Justification
# 
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is inserted between words.
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# 
# Note: Each word is guaranteed not to exceed L in length.


# from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        
        # hxl: this is not a difficult problem, but need extra attention to edge cases
        
        if len(words) == 1: # hxl: fill up the line and then return
            word = words[0]
            while len(word) != L:
                word += ' '
            return [word]
        elif L == 0:    # hxl: the original string doesn't matter any more
            return ['']
        
        r = []
        
        # hxl: each loop produce a line in the result, until there is no more word left
        while len(words) > 0:
            charCount = len(words[0])
            wordCount = 1
            while (charCount < L
                   and wordCount < len(words)):
                charCount += 1 + len(words[wordCount])  # hxl: 1 is space
                wordCount += 1
            if charCount > L:   # hxl: undo the last count that exceed the limit
                wordCount -= 1  # hxl: need to undo the wordCount first to get the right index
                charCount -= 1 + len(words[wordCount])
                
            if debug: print charCount, wordCount
            
            line = ''
            isLastLine = wordCount == len(words)
            remainingExtraSpaces = L - charCount
            remainingExtraSpacesPerGap = remainingExtraSpaces
            remainingExtraSpacesMod = remainingExtraSpaces
            if wordCount > 1:   # hxl: the number of gaps is 1 less than the number of words
                remainingExtraSpacesPerGap = remainingExtraSpaces / (wordCount - 1)
                remainingExtraSpacesMod = remainingExtraSpaces % (wordCount - 1)
            
            # hxl: each loop add a word to the line
            for i in range(wordCount):
                extraSpacesToAdd = remainingExtraSpacesPerGap
                if i == wordCount - 1:  # hxl: the last word is a special case
                    extraSpacesToAdd = remainingExtraSpaces
                elif i < remainingExtraSpacesMod:
                    extraSpacesToAdd += 1
                remainingExtraSpaces -= extraSpacesToAdd
                
                if i == 0:
                    line += words.pop(0)
                else:
                    line += ' ' + words.pop(0)
                
                if isLastLine:
                    # hxl: for the last line, all extra spaces are added to the end
                    if len(words) == 0:
                        while len(line) != L:
                            line += ' '
                else:
                    for j in range(extraSpacesToAdd):
                        line += ' '
                        
            r.append(line)
            
        return r
