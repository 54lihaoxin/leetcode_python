

import sys
from solution import Solution
from TreeNode import TreeNode


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()
#         self.test005()
#         self.test006()
#         self.test007()

    def test001(self):
        
        print "test 001"
        
        # hxl: see http://en.wikipedia.org/wiki/Tree_traversal
        
        nA = TreeNode('A')
        nB = TreeNode('B')
        nC = TreeNode('C')
        nD = TreeNode('D')
        nE = TreeNode('E')
        nF = TreeNode('F')  # hxl: root
        nG = TreeNode('G')
        nH = TreeNode('H')
        nI = TreeNode('I')
        nF.left = nB
        nF.right = nG
        nB.left = nA
        nB.right = nD
        nG.right = nI
        nD.left = nC
        nD.right = nE
        nI.left = nH
        
        r = Solution().postorderTraversal(nF)
        
        print "  input:\t", nF
        print "  output:\t", r
        print
    
    def test002(self):
        
        print "test 002"
        
        nA = TreeNode('A')
        
        r = Solution().postorderTraversal(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    