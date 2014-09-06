

import sys
import time
from CommonClasses import *
from solution import Solution

class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        numbers = [-2,1,-3,4,-1,2,1,-5,4]
        startTime = time.clock()
        r = Solution().maxSubArray(numbers)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(numbers)
        print '  expect:\t{0}'.format(6)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        numbers = [-1]
        startTime = time.clock()
        r = Solution().maxSubArray(numbers)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(numbers)
        print '  expect:\t{0}'.format(-1)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        numbers = [-2,-1]
        startTime = time.clock()
        r = Solution().maxSubArray(numbers)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(numbers)
        print '  expect:\t{0}'.format(-1)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        numbers = [-1,1,2,1]
        startTime = time.clock()
        r = Solution().maxSubArray(numbers)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(numbers)
        print '  expect:\t{0}'.format(4)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    