# Substring with Concatenation of All Words
# 
# You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
# 
# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
# 
# You should return the indices: [0,9].
# (order does not matter).


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    
    # hxl: this solution is from http://bookshadow.com/weblog/2014/04/24/leetcode-substring-concatenation-all-words/
    
    
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lenL = len(L)
        wordLen = len(L[0])
        tree, numDistinctWords = self.buildTree(L)
        strlen = len(S)
        arr = list()
        for i in range(strlen - wordLen + 1):
            arr.append(self.valTree(S, i, wordLen, tree))
        result = []
        dp = list()
        for i in range(strlen - wordLen + 1):
            wordDict = None
            wordSet = set()
            accm = 0
            if arr[i][0] > 0:   # hxl: 'id' is associated with a word in list
                idx = i - wordLen * (lenL - 1)
                if i < wordLen:
                    wordDict = {arr[i][0]:1}
                    if arr[i][1] == 1:  # hxl: number of repetition is 1
                        wordSet.add(arr[i][0])
                    if len(wordSet) == numDistinctWords:
                        result.append(i)
                else:
                    wordDict,wordSet,accm = dp[i - wordLen]
                    if wordDict is None:
                        wordDict = dict()
                    accm += 1
                    num = wordDict.get(arr[i][0],0)
                    wordDict[arr[i][0]] = num + 1
                    if num + 1 >= arr[i][1]:
                        wordSet.add(arr[i][0])
                    if idx >= 0:
                        if len(wordSet) == numDistinctWords:
                            result.append(idx)
                        if accm >= lenL - 1:
                            tmp = arr[idx]
                            if tmp[0] > 0:
                                num = wordDict.get(tmp[0],0)
                            if num - 1 < tmp[1] and tmp[0] in wordSet:
                                wordSet.remove(tmp[0])
                            if num >= 1:
                                wordDict[tmp[0]] = num - 1
            dp.append((wordDict,wordSet,accm))
        return result
    
    def buildTree(self, L):
        tree = dict()
        numDistinctWords = 0
        for word in L:
            node = tree
            for letter in word:
                child = node.get(letter)
                if child is None:
                    child = dict()
                    node[letter] = child
                node = child
            repetition = node.get('repetition',0)
            if repetition == 0:
                numDistinctWords += 1
                node['id'] = numDistinctWords
            node['repetition'] = repetition + 1
        return (tree, numDistinctWords)
    
    def valTree(self, word, start, wordLen, tree):
        node = tree
        for i in range(start, start + wordLen):
            if node.get(word[i]) is None:
                return (0, 0)
            node = node[word[i]]
        return (node['id'], node['repetition'])
    