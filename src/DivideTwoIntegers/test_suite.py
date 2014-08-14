

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
        self.test004()
        self.test005()
        self.test006()
        self.test007()
        self.test008()

    def test001(self):
        print "test 001"
        
        a = 2
        b = 3
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", 0
        print "  output:\t", r
        print
    
    def test002(self):
        print "test 002"
        
        a = 7
        b = 3
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", 2
        print "  output:\t", r
        print
    
    def test003(self):
        print "test 003"
        
        a = 8
        b = 2
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", 4
        print "  output:\t", r
        print
    
    def test004(self):
        print "test 004"
        
        a = 128
        b = 5
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", 25
        print "  output:\t", r
        print
    
    def test005(self):
        print "test 005"
        
        a = 1
        b = -3
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", -1
        print "  output:\t", r
        print
    
    def test006(self):
        print "test 006"
        
        a = 1
        b = -1
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", -1
        print "  output:\t", r
        print
    
    def test007(self):
        print "test 007"
        
        a = 2147483647
        b = 1
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", 2147483647
        print "  output:\t", r
        print
    
    def test008(self):
        print "test 008"
        
        a = -2147483648
        b = 2
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  expect:\t", -1073741824
        print "  output:\t", r
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    