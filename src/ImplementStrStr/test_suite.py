

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
        
        print 'test 000'
        
        s = 'ABC ABCDAB ABCDABCDABDE'
        t = 'ABCDABD'
        
        r = Solution().strStr(s, t)
        print '  input:\t', s, ' // substring:', t 
        print '  expect:\t', 'ABCDABDE'
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001'
        
        s = ''
        t = ''
        
        r = Solution().strStr(s, t)
        print '  input:\t', s, ' // substring:', t 
        print '  expect:\t', ''
        print '  output:\t', r
        print

    def test002(self):
        
        print 'test 002'
        
        s = 'a'
        t = 'a'
        
        r = Solution().strStr(s, t)
        print '  input:\t', s, ' // substring:', t 
        print '  expect:\t', 'a'
        print '  output:\t', r
        print

    def test003(self):
        
        print 'test 003'
        
        s = 'aaa'
        t = 'a'
        
        r = Solution().strStr(s, t)
        print '  input:\t', s, ' // substring:', t 
        print '  expect:\t', 'aaa'
        print '  output:\t', r
        print

    def test004(self):
         
        print 'test 004'
         
        s = 'a'
        t = ''
         
        r = Solution().strStr(s, t)
        print '  input:\t', s, ' // substring:', t 
        print '  expect:\t', 'a'
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    