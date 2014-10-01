

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

    def test000(self):
        
        print 'test 000\n'
        
        i = ListNode.listFromList([1,4,3,2,5,2])
        l = ListNode.listFromList([1,4,3,2,5,2])
        n = 3
        startTime = time.clock()
        r = Solution().partition(l, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        i = ListNode.listFromList([4,3,2,5,2])
        l = ListNode.listFromList([4,3,2,5,2])
        n = 3
        startTime = time.clock()
        r = Solution().partition(l, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        i = ListNode.listFromList([1,1])
        l = ListNode.listFromList([1,1])
        n = 0
        startTime = time.clock()
        r = Solution().partition(l, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        i = ListNode.listFromList([3,1,2])
        l = ListNode.listFromList([3,1,2])
        n = 3
        startTime = time.clock()
        r = Solution().partition(l, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        i = ListNode.listFromList([3,3,1,2,4])
        l = ListNode.listFromList([3,3,1,2,4])
        n = 3
        startTime = time.clock()
        r = Solution().partition(l, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        i = ListNode.listFromList([1,1,2])
        l = ListNode.listFromList([1,1,2])
        n = 0
        startTime = time.clock()
        r = Solution().partition(l, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    