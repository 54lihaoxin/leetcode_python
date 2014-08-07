

import sys
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()

    def test001(self):
        n = 0
        r = Solution().reverse(n)
        print "test 001"
        print "  input:\t", n
        print "  expect:\t", 0
        print "  output:\t", r
        print
    
    def test002(self):
        n = 123
        r = Solution().reverse(n)
        print "test 002"
        print "  input:\t", n
        print "  expect:\t", 123
        print "  output:\t", r
        print
    
    def test003(self):
        n = -321
        r = Solution().reverse(n)
        print "test 003"
        print "  input:\t", n
        print "  expect:\t", -123
        print "  output:\t", r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    