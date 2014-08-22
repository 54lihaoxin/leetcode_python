

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
        self.test003()
        self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        x = 2
        n = -1
        
        r = Solution().pow(x, n)
        print '  input:\t', x, n 
        print '  expect:\t', 0.5 
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001\n'
        
        x = 2
        n = 0
        
        r = Solution().pow(x, n)
        print '  input:\t', x, n 
        print '  expect:\t', 1.0
        print '  output:\t', r
        print

    def test002(self):
        
        print 'test 002\n'
        
        x = 2
        n = 1
        
        r = Solution().pow(x, n)
        print '  input:\t', x, n 
        print '  expect:\t', 2.0
        print '  output:\t', r
        print

    def test003(self):
        
        print 'test 003\n'
        
        x = 2
        n = 2
        
        r = Solution().pow(x, n)
        print '  input:\t', x, n 
        print '  expect:\t', 4.0
        print '  output:\t', r
        print

    def test004(self):
        
        print 'test 004\n'
        
        x = 2
        n = 3
        
        r = Solution().pow(x, n)
        print '  input:\t', x, n 
        print '  expect:\t', 8.0
        print '  output:\t', r
        print
        

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    