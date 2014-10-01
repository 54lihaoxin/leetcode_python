

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
#         self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()
#         self.test005()
        self.test006()

    def test000(self):
        
        print 'test 000\n'
        
        i = ListNode.listFromList([1, 1, 2])
        n = ListNode.listFromList([1, 1, 2])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([2]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        i = ListNode.listFromList([1, 1, 2, 3, 3])
        n = ListNode.listFromList([1, 1, 2, 3, 3])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([2]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        i = ListNode.listFromList([1, 1, 1])
        n = ListNode.listFromList([1, 1, 1])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        i = ListNode.listFromList([1, 2])
        n = ListNode.listFromList([1, 2])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([1, 2]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        i = ListNode.listFromList([1, 1, 2, 2, 3, 4, 4, 5])
        n = ListNode.listFromList([1, 1, 2, 2, 3, 4, 4, 5])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([3, 5]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        i = ListNode.listFromList([1, 2, 2])
        n = ListNode.listFromList([1, 2, 2])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([1]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test006(self):
        
        print 'test 006\n'
        
        i = ListNode.listFromList([1, 1, 2, 3])
        n = ListNode.listFromList([1, 1, 2, 3])
        startTime = time.clock()
        r = Solution().deleteDuplicates(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i)
        print '  expect:\t{0}'.format(ListNode.listFromList([2, 3]))
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    