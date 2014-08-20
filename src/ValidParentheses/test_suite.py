

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print "test 000"
        
        s = '()[]{}'
        
        r = Solution().isValid(s)
        print "  input:\t", s
        print "  expect:\t", True
        print "  output:\t", r
        print

    def test001(self):
        
        print "test 001"
        
        s = '(]'
        
        r = Solution().isValid(s)
        print "  input:\t", s
        print "  expect:\t", False
        print "  output:\t", r
        print

    def test002(self):
        
        print "test 002"
        
        s = '([)]'
        
        r = Solution().isValid(s)
        print "  input:\t", s
        print "  expect:\t", False
        print "  output:\t", r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    