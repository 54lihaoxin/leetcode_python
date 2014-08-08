

import sys
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()
        self.test005()
        self.test006()
        self.test007()
#         self.test008()

    def test000(self):
        n = 0
        
        ret = Solution().numTrees(n)
        print "test 000"
        print "  input:\t", n
        print "  expect:\t", 0
        print "  output:\t", ret
        print
    
    def test001(self):
        n = 1
        
        ret = Solution().numTrees(n)
        print "test 001"
        print "  input:\t", n
        print "  expect:\t", 1
        print "  output:\t", ret
        print
    
    def test002(self):
        n = 2
        
        ret = Solution().numTrees(n)
        print "test 002"
        print "  input:\t", n
        print "  expect:\t", 2
        print "  output:\t", ret
        print
    
    def test003(self):
        n = 3
        
        ret = Solution().numTrees(n)
        print "test 003"
        print "  input:\t", n
        print "  expect:\t", 5
        print "  output:\t", ret
        print
    
    def test004(self):
        n = 4
        
        ret = Solution().numTrees(n)
        print "test 004"
        print "  input:\t", n
        print "  expect:\t", 14
        print "  output:\t", ret
        print
    
    def test005(self):
        n = 5
        
        ret = Solution().numTrees(n)
        print "test 005"
        print "  input:\t", n
        print "  expect:\t", 42
        print "  output:\t", ret
        print
    
    def test006(self):
        n = 6
        
        ret = Solution().numTrees(n)
        print "test 006"
        print "  input:\t", n
        print "  expect:\t", 132
        print "  output:\t", ret
        print
    
    def test007(self):
        n = 7
        
        ret = Solution().numTrees(n)
        print "test 007"
        print "  input:\t", n
        print "  expect:\t", 429
        print "  output:\t", ret
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    