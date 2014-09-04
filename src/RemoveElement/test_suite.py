

import sys
import time
from solution import Solution
from ListNode import ListNode
from ListNode import listFromList


class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        i = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        e = 3
        startTime = time.clock()
        r = Solution().removeElement(a, e)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} - {1}'.format(i, e)
#         print '  expect:\t', ?
        print '  output:\t{0} - {1}'.format(r, a[:r])
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    