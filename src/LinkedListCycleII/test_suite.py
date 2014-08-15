

import sys
from solution import Solution
from classes import ListNode


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
        
        nA = ListNode('A')
        nB = ListNode('B')
        nC = ListNode('C')
        nD = ListNode('D')
        nE = ListNode('E')
        nF = ListNode('F')
        nG = ListNode('G')
        nA.next = nB
        nB.next = nC
        nC.next = nD
        nD.next = nE
        nE.next = nF
        nF.next = nG
        
        r = Solution().detectCycle(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print
    
    def test002(self):
        
        print "test 002"
        
        nA = ListNode('A')
        
        r = Solution().detectCycle(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print

    def test003(self):
        
        print "test 003"
        
        nA = ListNode('A')
        nA.next = nA
        
        r = Solution().detectCycle(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print

    def test004(self):
        
        print "test 004"
        
        nA = ListNode('A')
        nB = ListNode('B')
        nA.next = nB
        nB.next = nA
        
        r = Solution().detectCycle(nA)
        
        print "  input:\t", nA
        print "  output:\t", r
        print
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    