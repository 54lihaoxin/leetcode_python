

from CommonClasses import *
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

    def test000(self):
        
        print 'test 000\n'
        
        nums = [1,3,5,6]
        n = 5
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        nums = [1,3,5,6]
        n = 2
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        nums = [1,3,5,6]
        n = 7
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        nums = [1,3,5,6]
        n = 0
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        nums = [1,3]
        n = 0
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
        print '  expect:\t{0}'.format(0)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        nums = [1,3]
        n = 4
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
        print '  expect:\t{0}'.format(2)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test006(self):
        
        print 'test 006\n'
        
        nums = [1,3]
        n = 1
        startTime = time.clock()
        r = Solution().searchInsert(nums, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(nums, n)
        print '  expect:\t{0}'.format(0)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    