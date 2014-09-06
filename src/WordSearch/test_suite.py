

import sys
import time
import CommonClasses
from solution import Solution

class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        board = ['ABCE',
                 'SFCS',
                 'ADEE']
        word = 'ABCCED'
        startTime = time.clock()
        r = Solution().exist(board, word)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(board, word)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        board = ['ABCE',
                 'SFCS',
                 'ADEE']
        word = 'SEE'
        startTime = time.clock()
        r = Solution().exist(board, word)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(board, word)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        board = ['ABCE',
                 'SFCS',
                 'ADEE']
        word = 'ABCB'
        startTime = time.clock()
        r = Solution().exist(board, word)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(board, word)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        board = ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaab']
        word = 'baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        startTime = time.clock()
        r = Solution().exist(board, word)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}, {1}'.format(board, word)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    