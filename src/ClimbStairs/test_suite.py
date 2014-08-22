

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
        
        print 'test 000\n'
        
        n = 0
        r = Solution().climbStairs(n)
        print '  input:\t', n
        print '  expect:\t', 0
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = 1
        r = Solution().climbStairs(n)
        print '  input:\t', n
        print '  expect:\t', 1
        print '  output:\t', r
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = 2
        r = Solution().climbStairs(n)
        print '  input:\t', n
        print '  expect:\t', 2
        print '  output:\t', r
        print

    def test003(self):
        
        print 'test 003\n'
        
        n = 3
        r = Solution().climbStairs(n)
        print '  input:\t', n
        print '  expect:\t', 3
        print '  output:\t', r
        print

    def test004(self):
        
        print 'test 003\n'
        
        n = 4
        r = Solution().climbStairs(n)
        print '  input:\t', n
        print '  expect:\t', 5
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    