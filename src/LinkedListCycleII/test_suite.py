

import sys
from solution import Solution
from ListNode import ListNode


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()

    def test000(self):
        
        print "test 000"
        
        n0 = ListNode(0)
        
        r = Solution().detectCycle(n0)
        
        print "  expect:\t", True
        print "  output:\t", r
        print
    
    def test001(self):
        
        print "test 001"
        
        n0 = ListNode(0)
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n0.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        
        r = Solution().detectCycle(n0)
        
        print "  expect:\t", True
        print "  output:\t", r
        print
    
    def test002(self):
        
        print "test 002"
        
        n0 = ListNode(0)
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n0.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n0
        
        r = Solution().detectCycle(n0)
        
        print "  expect:\t", True
        print "  output:\t", r
        print
    
    def test003(self):
        
        print "test 003"
        
        n0 = ListNode(0)
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n0.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n1
        
        r = Solution().detectCycle(n0)
        
        print "  expect:\t", True
        print "  output:\t", r
        print
    
    def test004(self):
        
        print "test 004"
        
        n0 = ListNode(0)
        n0.next = n0
        
        r = Solution().detectCycle(n0)
        
        print "  expect:\t", True
        print "  output:\t", r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    