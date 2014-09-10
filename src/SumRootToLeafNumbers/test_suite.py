

import sys
import time
from CommonClasses import *
from solution import Solution

class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        n = getTreeFromString('{}')
        startTime = time.clock()
        r = Solution().sumNumbers(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format(0)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = getTreeFromString('{1,2,3}')
        startTime = time.clock()
        r = Solution().sumNumbers(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format(25)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = getTreeFromString('{1,5,1,#,#,#,6}')
        startTime = time.clock()
        r = Solution().sumNumbers(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format(131)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    