

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
        
        words = ['This','is','an','example','of','text','justification.']
        n = 16
        startTime = time.clock()
        r = Solution().fullJustify(words, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        words = ['What','must','be','shall','be.']
        n = 12
        startTime = time.clock()
        r = Solution().fullJustify(words, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        words = ['']
        n = 0
        startTime = time.clock()
        r = Solution().fullJustify(words, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        words = ['']
        n = 2
        startTime = time.clock()
        r = Solution().fullJustify(words, n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        words = ['so','fine','that','all','the','world','will','be','in','love']
        n = 25
        startTime = time.clock()
        r = Solution().fullJustify(words, n)
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
    