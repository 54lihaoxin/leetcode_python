

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        n = ListNode.listFromList([0,1,2,3,4,5,6])
        k = 2
        startTime = time.clock()
        r = Solution().reverseKGroup(n, k)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, k)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = ListNode.listFromList([0,1,2,3,4,5,6])
        k = 3
        startTime = time.clock()
        r = Solution().reverseKGroup(n, k)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, k)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = ListNode.listFromList([0,1,2,3,4,5,6])
        k = 4
        startTime = time.clock()
        r = Solution().reverseKGroup(n, k)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, k)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        n = ListNode.listFromList([0,1,2,3,4,5,6])
        k = 5
        startTime = time.clock()
        r = Solution().reverseKGroup(n, k)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, k)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        n = ListNode.listFromList([0,1,2,3,4,5,6])
        k = 6
        startTime = time.clock()
        r = Solution().reverseKGroup(n, k)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, k)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    