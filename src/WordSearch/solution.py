# Word Search
#  
# Given a 2D board and a word, find if the word exists in the grid.
#   
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#  
# For example,
# Given board =
#  
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


# import CommonClasses    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        
        initCoordinates = []
        
        # hxl: search for the first character of the given word in the board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    initCoordinates.append((i, j))
        
        found = False
        
        for (i, j) in initCoordinates:
            found |= self.existWithInitCoordinate(board, word, (i, j), set())
            if found: return found  # hxl: return early if found
        
        return found
        
    def existWithInitCoordinate(self, board, word, (i, j), visitedCoordinates):
        
        if debug: print word, (i, j), visitedCoordinates
        
        found = False
        
        if len(word) == 1:
            if debug: print '  -->  ', word == board[i][j]
            return word == board[i][j]
        elif word[0] == board[i][j]:
            visitedCoordinates.add((i, j))
            
            newCoordinate = (i - 1, j)
            if not found and newCoordinate[0] >= 0 and newCoordinate not in visitedCoordinates:
                found |= self.existWithInitCoordinate(board, word[1:], newCoordinate, visitedCoordinates)
            
            newCoordinate = (i, j - 1)
            if not found and newCoordinate[1] >= 0 and newCoordinate not in visitedCoordinates:
                found |= self.existWithInitCoordinate(board, word[1:], newCoordinate, visitedCoordinates)
            
            newCoordinate = (i + 1, j)
            if not found and newCoordinate[0] < len(board) and newCoordinate not in visitedCoordinates:
                found |= self.existWithInitCoordinate(board, word[1:], newCoordinate, visitedCoordinates)
            
            newCoordinate = (i, j + 1)
            if not found and newCoordinate[1] < len(board[i]) and newCoordinate not in visitedCoordinates:
                found |= self.existWithInitCoordinate(board, word[1:], newCoordinate, visitedCoordinates)

            visitedCoordinates.remove((i, j))
                
        return found
        