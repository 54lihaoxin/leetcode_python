

import sys
from solution import Solution
from classes import ListNode


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        a0 = ListNode(0)
        a1 = ListNode(2)
        a2 = ListNode(4)
        a3 = ListNode(6)
        a4 = ListNode(8)
        b0 = ListNode(-123)
        b1 = ListNode(-12)
        b2 = ListNode(1)
        b3 = ListNode(2)
        b4 = ListNode(12)
        a0.next = a1
        a1.next = a2
        a2.next = a3
        a3.next = a4
        b0.next = b1
        b1.next = b2
        b2.next = b3
        b3.next = b4
        
        lists = [a0, b0]
        r = Solution().mergeKLists([a0, b0])
        print '  input:\t', lists
#         print '  expect:\t', 
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001\n'
        
        a0 = ListNode(0)
        a1 = ListNode(2)
        a2 = ListNode(4)
        a3 = ListNode(6)
        a4 = ListNode(8)
        b0 = ListNode(-123)
        b1 = ListNode(-12)
        b2 = ListNode(1)
        b3 = ListNode(2)
        b4 = ListNode(12)
        c0 = ListNode(1)
        c1 = ListNode(2)
        c2 = ListNode(3)
        c3 = ListNode(4)
        c4 = ListNode(5)
        a0.next = a1
        a1.next = a2
        a2.next = a3
        a3.next = a4
        b0.next = b1
        b1.next = b2
        b2.next = b3
        b3.next = b4
        c0.next = c1
        c1.next = c2
        c2.next = c3
        c3.next = c4
        
        lists = [a0, b0, c0]
        r = Solution().mergeKLists([a0, b0, c0])
        print '  input:\t', lists
#         print '  expect:\t', 
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    