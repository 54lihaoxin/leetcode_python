

class Solution:
    
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            # hxl: f(2) * 2 + f(1) * f(1)
            return 5
        elif n == 4:
            # hxl: (f(3) + f(2)) * 2
            return 14
        elif n == 5:
            # hxl: (f(4) + f(3)) * 2 + f(2) * f(2)
            return 42
        elif n >= 6:
            # hxl: I consider general case starting from this
            c = (self.numTrees(n - 1)       # hxl: the other child of root is empty 
                 + self.numTrees(n - 2))    # hxl: the other child of root only has one node
            for i in range(2, n / 2):
                c += (self.numTrees(i)              # hxl: left child combinations
                      * self.numTrees(n - i - 1))   # hxl: right child combinations
            c *= 2  # hxl: for symmetry
            if n % 2 == 1:  # hxl: left child and right child could have the same amount of nodes
                d = self.numTrees(int(n / 2))
                c += d * d
            return c
    