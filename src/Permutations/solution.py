

debug = True
debug = False


# from ? import ?   # hxl: comment out this line for submission
 
 
class Solution:
    
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        tuples = self.permuteTuple(num)
        r = []
        for t in tuples:
            r.append(list(t))
        return r
        
    def permuteTuple(self, num):
        if len(num) == 1:
            return [tuple(num)]
        r = set([])
        for i in range(len(num)):
            subPermutations = self.permuteTuple(num[:i] + num[i+1:])
            for p in subPermutations:
                p = tuple([num[i]]) + p
                r.add(p)
        return list(r)
    