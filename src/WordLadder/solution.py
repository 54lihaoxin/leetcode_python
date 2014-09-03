

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    def __init__(self):
        # hxl: the following two dictionaries are mutual reverse
        self.wordDict = {}      # hxl: K: word key (such as "h*t", which is for "hat" and "hit") ; V: set of words that match
        self.matcherDict = {}   # hxl: K: a word; V: set of word keys that match (such is "*at", "h*t", and "ha*" for "hot")
        
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        
        r = []  # hxl: result dict
        searchQueue = []    # hxl: for BFS
        foundLadder = False
        visitedWords = set([start])
        
        self.addWordToDict(start)
        self.addWordToDict(end)
        
        for word in dict:
            self.addWordToDict(word)
        
        # hxl: initialize with the first level of children
        for match in self.matcherDict[start]:
            path = [start]
            searchQueue.append([match, path])
        # hxl: mark the end of level by an empty array
        searchQueue.append([])
        
        while len(searchQueue) != 0:
            t = searchQueue[0]
            searchQueue = searchQueue[1:]
            
            if len(t) == 0: # hxl: this represents the end of level
                if foundLadder == True:
                    break
                elif len(searchQueue) != 0:
                    searchQueue.append([])  # hxl: add the "end of level" empty array only if there is one more level
            else:
                key = t[0]  #hxl: a key is a match that is like "h*t" for "hat" and "hit"
                path = t[1]
                
                for nextWord in self.wordDict[key]:
                    if nextWord not in visitedWords:
                        visitedWords.add(nextWord)
                        if nextWord != start:
                            for key in self.matcherDict[nextWord]:
                                if nextWord not in path:    # hxl: TODO: can check against a set instead of in a list
                                    newPath = path[:] + [nextWord]
                                    searchQueue.append([key, newPath])
                        if nextWord == end:
                            foundLadder = True
                            r.append(path[:] + [nextWord])
                            return len(path) + 1        
        return 0
                
    def addWordToDict(self, w):
        if w not in self.matcherDict:
            matchers = []
            for i in range(len(w)):
                key = w[:i] + '*' + w[i + 1:]
                matchers.append(key)
                if key not in self.wordDict:
                    self.wordDict[key] = set([w])
                else:
                    self.wordDict[key].add(w)
            self.matcherDict[w] = matchers
    