# Valid Sudoku
# 
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# 
# ["...5.....",
#  ".86..45..",
#  "..6......",
#  ".9.....1.",
#  "1........",
#  "....6....",
#  "9.4......",
#  "...4.....",
#  "2..3....."]
# 
# A partially filled sudoku which is invalid.
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


# from CommonClasses import *    # hxl: comment out this line for submission


debug = True
debug = False


class Solution:
    
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board): 
        return (self.areAllRowsValid(board)
                and self.areAllColumnsValid(board)
                and self.areAllGridsValid(board))
        
    def areAllRowsValid(self, board):
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                k = board[i][j]
                if k != '.':
                    if k in s:
                        if debug: print 'areAllRowsValid False', i, j, k
                        return False
                    else:
                        if debug: print 'areAllRowsValid', i, j, k
                        s.add(k)
        return True
    
    def areAllColumnsValid(self, board):
        for j in range(len(board[0])):
            s = set()
            for i in range(len(board)):
                k = board[i][j] # hxl: pay attention to which is i and which is j
                if k != '.':
                    if k in s:
                        if debug: print 'areAllColumnsValid False', i, j, k
                        return False
                    else:
                        if debug: print 'areAllColumnsValid', i, j, k
                        s.add(k)
        return True
    
    def areAllGridsValid(self, board):
        for m in [0, 3, 6]:     # hxl: row offset
            for n in [0, 3, 6]: # hxl: column offset
                s = set()
                for i in range(3):
                    for j in range(3):
                        k = board[m + i][n + j]
                        if k != '.':
                            if k in s:
                                if debug: print 'areAllGridsValid False', i, j, k
                                return False
                            else:
                                if debug: print 'areAllGridsValid', i, j, k
                                s.add(k)
        return True
