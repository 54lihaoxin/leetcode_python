

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        matrix = [[ 1,  3,  5,  7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 50]]
        n = 3
        startTime = time.clock()
        r = Solution().searchMatrix(matrix, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        matrix = [[1]]
        n = 1
        startTime = time.clock()
        r = Solution().searchMatrix(matrix, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        matrix = [[1]]
        n = 2
        startTime = time.clock()
        r = Solution().searchMatrix(matrix, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        matrix = [[1, 1]]
        n = 2
        startTime = time.clock()
        r = Solution().searchMatrix(matrix, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        matrix = [[1, 3]]
        n = 1
        startTime = time.clock()
        r = Solution().searchMatrix(matrix, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    