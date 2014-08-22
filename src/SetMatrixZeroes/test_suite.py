

import sys
from solution import Solution
from copy import deepcopy
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        m = [[1,0,1],
             [0,1,1],
             [1,1,1],]
        input = deepcopy(m)
        r = Solution().setZeroes(m)
        print '  input:\t', input
        print '  expect:\t', [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        print '  output:\t', m
        print

    def test001(self):
        
        print 'test 001\n'
        
        m = [[1],[0]]
        input = deepcopy(m)
        r = Solution().setZeroes(m)
        print '  input:\t', input
        print '  expect:\t', [[0], [0]] 
        print '  output:\t', m
        print
    

    def test002(self):
        
        print 'test 002\n'
        
        m = [[0,0,0,5],
             [4,3,1,4],
             [0,1,1,4],
             [1,2,1,3],
             [0,0,1,1]]
        input = deepcopy(m)
        r = Solution().setZeroes(m)
        print '  input:\t', input
        print '  expect:\t', [[0,0,0,0],
                              [0,0,0,4],
                              [0,0,0,0],
                              [0,0,0,3],
                              [0,0,0,0]]
        print '  output:\t', m
        print
        
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    