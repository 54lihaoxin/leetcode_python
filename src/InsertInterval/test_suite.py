

import sys
from solution import Solution
from Interval import Interval


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        a = [Interval(1, 3),
             Interval(6, 9)]
        b = Interval(2, 5)
        r = Solution().insert(a, b)
        print '  input:\t', a, b
        print '  expect:\t', [[1,5],[6,9]] 
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001\n'
        
        a = [Interval(1, 2),
             Interval(3, 5),
             Interval(6, 7),
             Interval(8, 10),
             Interval(12, 16)]
        b = Interval(4, 9)
        r = Solution().insert(a, b)
        print '  input:\t', a, b
        print '  expect:\t', [[1,2],[3,10],[12,16]]
        print '  output:\t', r
        print

    def test002(self):
        
        print 'test 002\n'
        
        a = [Interval(2, 5),
             Interval(3, 7),
             Interval(8, 9)]
        b = Interval(0, 1)
        r = Solution().insert(a, b)
        print '  input:\t', a, b
        print '  expect:\t', [[0,1],[2,5],[3,7],[8,9]]
        print '  output:\t', r
        print

    def test003(self):
        
        print 'test 003\n'
        
        a = [Interval(1, 5)]
        b = Interval(2, 7)
        r = Solution().insert(a, b)
        print '  input:\t', a, b
        print '  expect:\t', [[1,7]]
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    