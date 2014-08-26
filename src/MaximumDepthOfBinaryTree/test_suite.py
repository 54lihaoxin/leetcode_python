

import sys
from solution import Solution
from TreeNode import TreeNode


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
        self.test004()
        self.test005()

    def test001(self):
        s = Solution()
        root = TreeNode('root')
        n = s.maxDepth(root)
        print "input:\t", root
        print "expect:\t", 1
        print "output:\t", n
        
    def test002(self):
        s = Solution()
        root = TreeNode('root')
        nodeR = TreeNode('nodeR')
        root.right = nodeR
        
        n = s.maxDepth(root)
        print "input:\t", root
        print "expect:\t", 2
        print "output:\t", n
        
    def test003(self):
        s = Solution()
        root = TreeNode('root')
        nodeR = TreeNode('nodeR')
        nodeRR = TreeNode('nodeRR')
        root.right = nodeR
        nodeR.right = nodeRR
        
        n = s.maxDepth(root)
        print "input:\t", root
        print "expect:\t", 3
        print "output:\t", n
        
    def test004(self):
        s = Solution()
        root = TreeNode('root')
        nodeR = TreeNode('nodeR')
        nodeRR = TreeNode('nodeRR')
        nodeRL = TreeNode('nodeRL')
        root.right = nodeR
        nodeR.right = nodeRR
        nodeR.left = nodeRL
        
        n = s.maxDepth(root)
        print "input:\t", root
        print "expect:\t", 3
        print "output:\t", n
        
    def test005(self):
        s = Solution()
        root = TreeNode('root')
        nodeR = TreeNode('nodeR')
        nodeL = TreeNode('nodeL')
        nodeRR = TreeNode('nodeRR')
        nodeRL = TreeNode('nodeRL')
        root.right = nodeR
        root.left = nodeL
        nodeR.right = nodeRR
        nodeR.left = nodeRL
        
        n = s.maxDepth(root)
        print "input:\t", root
        print "expect:\t", 3
        print "output:\t", n



def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)  