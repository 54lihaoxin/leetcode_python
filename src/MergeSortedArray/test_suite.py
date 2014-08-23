

import sys
from solution import Solution
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
        
        a = [0,2,4,6,8]
        b = [-123,-12,1,2,12]
        ab = a + [None,None,None,None,None]
        m = len(a)
        n = len(b)
        r = Solution().merge(ab, m, b, n)
        print '  input:\t', a, b
#         print '  expect:\t', 
        print '  output:\t', ab
        print

    def test001(self):
        
        print 'test 001\n'
        
        a = []
        b = [1]
        ab = a + [None]
        m = len(a)
        n = len(b)
        r = Solution().merge(ab, m, b, n)
        print '  input:\t', a, b
#         print '  expect:\t', 
        print '  output:\t', ab
        print

    def test002(self):
        
        print 'test 002\n'
        
        a = []
        b = [1,2,3,4,5]
        ab = a + [None,None,None,None,None]
        m = len(a)
        n = len(b)
        r = Solution().merge(ab, m, b, n)
        print '  input:\t', a, b
#         print '  expect:\t', 
        print '  output:\t', ab
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    