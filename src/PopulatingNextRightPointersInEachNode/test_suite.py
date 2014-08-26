

import sys
from solution import Solution
from TreeNode import TreeNode


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
#         self.test004()
#         self.test005()
#         self.test006()
#         self.test007()

    def test001(self):
        
        print "test 001"
        
        r = Solution().connect(None)
        
        print "  input:\t", None
        print "  output:\t", r
        print
    
    def test002(self):
        
        print "test 002"
        
        nA = TreeNode('A')
        
        r = Solution().connect(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print

    def test003(self):
        
        print "test 003"
        
        # hxl: see http://en.wikipedia.org/wiki/Tree_traversal
        
        nA = TreeNode('A')
        nB = TreeNode('B')
        nC = TreeNode('C')
        nD = TreeNode('D')
        nE = TreeNode('E')
        nF = TreeNode('F')
        nG = TreeNode('G')

        nA.left = nB
        nA.right = nC
        nB.left = nD
        nB.right = nE
        nC.left = nF
        nC.right = nG
        
        r = Solution().connect(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    