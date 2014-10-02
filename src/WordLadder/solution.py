# Word Ladder
# 
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
# 
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission
 
 
class Solution:
    
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        
        if len(start) == 1:
            return 1
        
        level = set([start])
        visitedWords = set()
        dict.add(end)
        map = {}    # hxl: K: word; V: set of neighbor words
        self.buildMap(map, dict, visitedWords, set(), start)
        count = 0
        
        while len(level) != 0:
            count += 1
            print count
            nextLevel = set([])
            for curWord in level:
                if curWord == end:
                    return count
                elif curWord not in visitedWords:
                    visitedWords.add(curWord)
                    if curWord not in map:
                        self.buildMap(map, dict, visitedWords, level, curWord)
                    for nextWord in map[curWord]:
                        nextLevel.add(nextWord)
            level = nextLevel
        
        return 0
    
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
        