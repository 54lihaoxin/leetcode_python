# Word Break II
# 
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# 
# Return all such possible sentences.
# 
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# 
# A solution is ["cats and dog", "cat sand dog"].


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        
        if s in dict:
            return [s]
        elif len(s) == 0:
            return []
        elif len(dict) == 0:
            return []
        
        newDict = {}    # hxl: K: index of matching word; V: list of the index of remaining string
        endWithMatchingWord = False
        
        # hxl: build a dictionary of matching word index
        for word in dict:
            for i in range(len(s) - len(word) + 1):
                end = i + len(word)
                if s[i:end] == word:
                    if i not in newDict:
                        newDict[i] = set([end])
                    else:
                        newDict[i].add(end)
                    endWithMatchingWord |= end == len(s)
                        
        if debug: print endWithMatchingWord, newDict
        
        if (endWithMatchingWord == False
            or 0 not in newDict):
            return []
        
        r = []
        path = [(0, list(newDict[0]))]
        
        # hxl: construct the sentences with the info in newDict
        while len(path) != 0:
            (curIndex, nextIndexes) = path[-1]
            if len(nextIndexes) == 0:
                path.pop(-1)
            else:
                nextIndex = nextIndexes.pop(0)
                if nextIndex == len(s): # hxl: now we have a sentence with matching words
                    sentence = s[path[-1][0]:]  # hxl: build the sentence from the last word
                    i = -2
                    while -len(path) <= i:
                        sentence = s[path[i][0]:path[i + 1][0]] + ' ' + sentence
                        i -= 1
                    if debug: print sentence
                    r.append(sentence)
                elif nextIndex in newDict:  # hxl: it's possible that the rest of it doesn't match
                    path.append((nextIndex, list(newDict[nextIndex])))
        
        return r
    