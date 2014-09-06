

import sys
import time
import CommonClasses
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

    def test000(self):
        
        print 'test 000\n'
        
        s = '12'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
        print '  expect:\t{0}'.format(2)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        s = '1234'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        s = '12321'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        s = '123210'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        s = '1232101234'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        s = '4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test006(self):
        
        print 'test 006\n'
        
        s = '0'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test007(self):
        
        print 'test 007\n'
        
        s = '10'
        startTime = time.clock()
        r = Solution().numDecodings(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    