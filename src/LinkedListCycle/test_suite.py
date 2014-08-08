

import sys
from solution import Solution
from classes import ListNode


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()

    def test000(self):
        n0 = ListNode(0)
        
        hasCycle = Solution().hasCycle(n0)
        print "test 000"
        print "  expect:\t", False
        print "  output:\t", hasCycle
        print
    
    def test001(self):
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
        
        hasCycle = Solution().hasCycle(n0)
        print "test 001"
        print "  expect:\t", False
        print "  output:\t", hasCycle
        print
    
    def test002(self):
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
        
        hasCycle = Solution().hasCycle(n0)
        print "test 002"
        print "  expect:\t", True
        print "  output:\t", hasCycle
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    