

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
        
        l = ListNode.listFromList([1,2,3,4])
        m = 2
        n = 4
        startTime = time.clock()
        r = Solution().reverseBetween(l, m, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} <-> {1}, {2}'.format(m, n, l)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        l = ListNode.listFromList([1,2,3,4,5])
        m = 2
        n = 4
        startTime = time.clock()
        r = Solution().reverseBetween(l, m, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} <-> {1}, {2}'.format(m, n, l)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        l = ListNode.listFromList([1,2,3,4,5,6])
        m = 2
        n = 4
        startTime = time.clock()
        r = Solution().reverseBetween(l, m, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} <-> {1}, {2}'.format(m, n, l)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        l = ListNode.listFromList([1])
        m = 1
        n = 1
        startTime = time.clock()
        r = Solution().reverseBetween(l, m, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} <-> {1}, {2}'.format(m, n, l)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        l = ListNode.listFromList([3,5])
        m = 2
        n = 2
        startTime = time.clock()
        r = Solution().reverseBetween(l, m, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} <-> {1}, {2}'.format(m, n, l)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    