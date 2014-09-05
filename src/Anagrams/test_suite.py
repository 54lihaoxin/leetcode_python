

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
        
        s = ['asdf', 'zxcv', 'qwer', 'fdas', 'dsaf', 'zxcx']
        startTime = time.clock()
        r = Solution().anagrams(s)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(s)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    