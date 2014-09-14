

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        i = listFromList([5,4,3,2,1])
        head = listFromList([5,4,3,2,1])
        n = 2
        startTime = time.clock()
        r = Solution().removeNthFromEnd(head, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
    
    def test001(self):
        
        print 'test 001\n'
        
        i = listFromList([2,1])
        head = listFromList([2,1])
        n = 2
        startTime = time.clock()
        r = Solution().removeNthFromEnd(head, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(i, n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
        

def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    