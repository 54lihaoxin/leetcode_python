

import sys
from solution import Solution
from ListNode import ListNode
from ListNode import listFromList


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
        
        l1 = listFromList([2,4,3])
        l2 = listFromList([5,6,4])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([7,0,8])
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001\n'
        
        l1 = listFromList([2,4,3])
        l2 = listFromList([5,6,8,1])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([7,0,2,2])
        print '  output:\t', r
        print

    def test002(self):
        
        print 'test 002\n'
        
        l1 = listFromList([2,4,7,1])
        l2 = listFromList([5,6,4])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([7,0,2,2])
        print '  output:\t', r
        print

    def test003(self):
        
        print 'test 003\n'
        
        l1 = listFromList([2,4,3])
        l2 = listFromList([5,6,8,1,1])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([7,0,2,2,1])
        print '  output:\t', r
        print

    def test004(self):
        
        print 'test 004\n'
        
        l1 = listFromList([2,4,7,1,1])
        l2 = listFromList([5,6,4])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([7,0,2,2,1])
        print '  output:\t', r
        print

    def test005(self):
        
        print 'test 005\n'
        
        l1 = listFromList([5])
        l2 = listFromList([5])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([0,1])
        print '  output:\t', r
        print

    def test006(self):
        
        print 'test 006\n'
        
        l1 = listFromList([9,9])
        l2 = listFromList([1])
        r = Solution().addTwoNumbers(l1, l2)
        print '  input:\t', l1, l2
        print '  expect:\t', listFromList([0,0,1])
        print '  output:\t', r
        print
        
        

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    