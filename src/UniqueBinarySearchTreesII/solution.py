# Unique Binary Search Trees II
# 
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
# confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


debug = True
debug = False


from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    def __init__(self):
        self.treeCache = {} # hxl: K: a range tuple (rangeMin, rangeMax); V: a list of trees
    
    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0:
            return [None]
        else:
            return self.generateTreesWithRange(1, n)
    
    def generateTreesWithRange(self, rangeMin, rangeMax):
        if (rangeMin, rangeMax) in self.treeCache:
            return self.treeCache[(rangeMin, rangeMax)]
        elif rangeMin == rangeMax:  
            self.treeCache[(rangeMin, rangeMax)] = [TreeNode(rangeMin)]
            return self.treeCache[(rangeMin, rangeMax)]
        else:
            r = []
            for i in range(rangeMin, rangeMax + 1):
                if i == rangeMin:
                    rightChildren = self.generateTreesWithRange(i + 1, rangeMax)
                    for rightChild in rightChildren: 
                        newRoot = TreeNode(i)
                        newRoot.right = rightChild
                        r.append(newRoot)
                elif i == rangeMax:
                    leftChildren = self.generateTreesWithRange(rangeMin, i - 1)
                    for leftChild in leftChildren: 
                        newRoot = TreeNode(i)
                        newRoot.left = leftChild
                        r.append(newRoot)
                else:
                    leftChildren = self.generateTreesWithRange(rangeMin, i - 1)
                    rightChildren = self.generateTreesWithRange(i + 1, rangeMax)
                    for leftChild in leftChildren:
                        for rightChild in rightChildren:
                            newRoot = TreeNode(i)
                            newRoot.left = leftChild
                            newRoot.right = rightChild
                            r.append(newRoot)            
            self.treeCache[(rangeMin, rangeMax)] = r
            return self.treeCache[(rangeMin, rangeMax)]
