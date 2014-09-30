# Word Ladder II
# 
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
# 
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
#   
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
    
    def __init__(self):
        self.paths = []
        self.prevDict = {}
        
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        
        if len(start) == 1:
            return [[start, end]]
        
        level = set([start])
        visitedWords = set()
        dict.add(start)
        dict.add(end)
        map = {}    # hxl: K: word; V: set of neighbor words
        self.buildMap(map, dict, visitedWords, set(), start)
        
        while len(self.paths) == 0 and len(level) != 0:
            nextLevel = set([])
            for curWord in level:
                if curWord == end:
#                     print map
#                     print self.prevDict
                    self.depthFirstBulidPaths(start, end, [])
                elif curWord not in visitedWords:
                    visitedWords.add(curWord)
                    if curWord not in map:
                        self.buildMap(map, dict, visitedWords, level, curWord)
                    for nextWord in map[curWord]:
                        nextLevel.add(nextWord)
                        if nextWord in self.prevDict:
                            self.prevDict[nextWord].add(curWord)
                        else:
                            self.prevDict[nextWord] = set([curWord])
            level = nextLevel
        
        return self.paths
    
    def depthFirstBulidPaths(self, start, cur, curPath):
        if cur == start:
            self.paths.append([start] + curPath)
        else:
            for word in self.prevDict[cur]:
                self.depthFirstBulidPaths(start, word, [cur] + curPath)
    
    def buildMap(self, map, words, visitedWords, thisLevel, targetWord):
        map[targetWord] = set()
        for w in words:
            if (w not in visitedWords
                and w not in thisLevel
                and self.areNeighbor(targetWord, w)):
                map[targetWord].add(w)
    
    # hxl: check whether two words are different with only one character
    def areNeighbor(self, wordA, wordB):
        diff = 0
        i = 0
        while i < len(wordA):
            if wordA[i] != wordB[i]:
                diff += 1
            if diff > 2:
                return False
            i += 1
        return diff == 1
        