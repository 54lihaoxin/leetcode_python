

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        matrix = [[ 1, 2, 3 ],
                  [ 4, 5, 6 ],
                  [ 7, 8, 9 ]]
        startTime = time.clock()
        r = Solution().spiralOrder(matrix)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        matrix = [[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]]
        startTime = time.clock()
        r = Solution().spiralOrder(matrix)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        matrix = [[1,2,3,4,5,6,7,8,9,10],
                  [11,12,13,14,15,16,17,18,19,20],
                  [21,22,23,24,25,26,27,28,29,30],
                  [31,32,33,34,35,36,37,38,39,40],
                  [41,42,43,44,45,46,47,48,49,50],
                  [51,52,53,54,55,56,57,58,59,60],
                  [61,62,63,64,65,66,67,68,69,70],
                  [71,72,73,74,75,76,77,78,79,80],
                  [81,82,83,84,85,86,87,88,89,90],
                  [91,92,93,94,95,96,97,98,99,100]]
        startTime = time.clock()
        r = Solution().spiralOrder(matrix)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(matrix)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    