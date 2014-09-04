

import sys
import time
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
        
        i = [1,1,2]
        startTime = time.clock()
        r = Solution().permuteUnique(i)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        i = [3,3,0,0,2,3,2]
        startTime = time.clock()
        r = Solution().permuteUnique(i)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        i = [0,1,2,3,4,5,6]
        startTime = time.clock()
        r = Solution().permuteUnique(i)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    