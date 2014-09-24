

import sys
import time
import CommonClasses
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
        
        n = ["...5.....",
             ".86..45..",
             "..6......",
             ".9.....1.",
             "1........",
             "....6....",
             "9.4......",
             "...4.....",
             "2..3....."]
        startTime = time.clock()
        r = Solution().isValidSudoku(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = [".87654321",
             "2........",
             "3........",
             "4........",
             "5........",
             "6........",
             "7........",
             "8........",
             "9........"]
        startTime = time.clock()
        r = Solution().isValidSudoku(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    