

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()

    def test000(self):
        
        print "test 000"
        
        s = "0"
        
        r = Solution().isNumber(s)
        
        print "  input:\t", s
        print "  expect:\t", True
        print "  output:\t", r
        print
    
    def test001(self):
        
        print "test 001"
        
        s = " 0.1"
        
        r = Solution().isNumber(s)
        
        print "  input:\t", s
        print "  expect:\t", True
        print "  output:\t", r
        print
    
    def test002(self):
        
        print "test 002"
        
        s = "abc"
        
        r = Solution().isNumber(s)
        
        print "  input:\t", s
        print "  expect:\t", False
        print "  output:\t", r
        print
    
    def test003(self):
        
        print "test 003"
        
        s = "1 a"
        
        r = Solution().isNumber(s)
        
        print "  input:\t", s
        print "  expect:\t", False
        print "  output:\t", r
        print
    
    def test004(self):
        
        print "test 004"
        
        s = "2e10"
        
        r = Solution().isNumber(s)
        
        print "  input:\t", s
        print "  expect:\t", True
        print "  output:\t", r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    