

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
        
        n = '/home/'
        
        startTime = time.clock()
        r = Solution().simplifyPath(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format('/home')
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = '/a/./b/../../c/'
        
        startTime = time.clock()
        r = Solution().simplifyPath(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format('/c')
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = '/../'
        
        startTime = time.clock()
        r = Solution().simplifyPath(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format('/')
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        n = '/home//foo/'
        
        startTime = time.clock()
        r = Solution().simplifyPath(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
        print '  expect:\t{0}'.format('/home/foo')
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
        

def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    