

import sys
import time
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
        
        a = '11'
        b = '1'
        startTime = time.clock()
        r = Solution().addBinary(a, b)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(a, b)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    