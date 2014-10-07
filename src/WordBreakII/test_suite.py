

from CommonClasses import *
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
        
        n = 'catsanddog'
        d = ['cat','cats','and','sand','dog']
        startTime = time.clock()
        r = Solution().wordBreak(n, d)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, d)
        print '  expect:\t{0}'.format(['cat sand dog','cats and dog'])
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = 'leetcode'
        d = ['leet','code']
        startTime = time.clock()
        r = Solution().wordBreak(n, d)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, d)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


    def test002(self):
        
        print 'test 002\n'
        
        n = 'abcd'
        d = ['a','abc','b','cd']
        startTime = time.clock()
        r = Solution().wordBreak(n, d)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, d)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


    def test003(self):
        
        print 'test 003\n'
        
        n = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
        d = ['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','aaaaaaaa','aaaaaaaaa','aaaaaaaaaa']
        startTime = time.clock()
        r = Solution().wordBreak(n, d)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, d)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    