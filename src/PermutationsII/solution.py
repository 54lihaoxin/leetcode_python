

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    def __init__(self):
        self.permutations = set()
        self.visited = set()
    
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        
        for i in range(len(num)):
            self.depthFirstSearch(num[:i] + num[i+1:], tuple([num[i]]))
        
        r = []
        for t in self.permutations:
            r.append(list(t))   # hxl: the return result needs to be a list of lists instead of list of tuples
        return r
    
    def depthFirstSearch(self, num, curPermutation):
        if curPermutation not in self.visited:
            if len(num) > 0:
                self.visited.add(curPermutation)
                for i in range(len(num)):
                    self.depthFirstSearch(num[:i] + num[i+1:], curPermutation + tuple([num[i]]))
            else:
                # hxl: add the permutation when all integers are consumed
                self.permutations.add(curPermutation)
        