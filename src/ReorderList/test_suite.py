

import sys
from solution import Solution
from ListNode import ListNode


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
        self.test004()
#         self.test005()
#         self.test006()
#         self.test007()

    def test001(self):
        print "test 001"
        
        n0 = ListNode(0)
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n0.next = n1
        n1.next = n2
        n2.next = n3
        
        r = Solution().reorderList(n0)
        
        print "  input:\t", n0
        print "  output:\t", r
        print
    
    def test002(self):
        print "test 002"
        
        n0 = ListNode(0)
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n0.next = n1
        n1.next = n2
        n2.next = n3
        n3.next = n4
        
        r = Solution().reorderList(n0)
        
        print "  input:\t", n0
        print "  output:\t", r
        print
    
    def test003(self):
        print "test 003"
        
        n0 = ListNode(0)
        n1 = ListNode(1)
        n0.next = n1
        
        r = Solution().reorderList(n0)
        
        print "  input:\t", n0
        print "  output:\t", r
        print
    
    def test004(self):
        print "test 004"
        
        n0 = ListNode(0)
        
        r = Solution().reorderList(n0)
        
        print "  input:\t", n0
        print "  output:\t", r
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    