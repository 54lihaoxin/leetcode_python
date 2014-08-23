

debug = True
debug = False


# from classes import ?   # hxl: comment out this line for submission


class Solution:
    
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        
        if m == 0:
            for i in range(n):
                A[i] = B[i]
            return
        if n == 0:
            return
        
        a = m - 1
        b = n - 1
        
        while a + b >= 0:
            if A[a] >= B[b]:
                A[a + b + 1] = A[a]
                a -= 1
                if a < 0:
                    # hxl: If A is exhausted early, copy the remaining of B to the beginning of A
                    for i in range(0, b + 1):
                        A[i] = B[i]
                    return
            else:
                A[a + b + 1] = B[b]
                b -= 1
                if b < 0:
                    return
    