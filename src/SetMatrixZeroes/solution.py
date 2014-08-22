

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        
        firstColumnHasZero = False
        firstRowHasZero = False
        
        # hxl: know the status of the first row and column         
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                firstColumnHasZero = True
                break
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                firstRowHasZero = True
                break
        
        # hxl: use the first row and column to indicate which ones which be zeroed
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # hxl: set the zeros except for the first row and column
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
            
        # hxl: set the zeros for the first row and column
        if firstColumnHasZero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if firstRowHasZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0 
                