

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        n0 = RandomListNode(0)
        n1 = RandomListNode(1)
        n2 = RandomListNode(2)
        n0.next = n1
        n1.next = n2
        n2.next = None
        n0.random = n2
        n1.random = None
        n2.random = n1
        
        startTime = time.clock()
        r = Solution().copyRandomList(n0)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n0)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    