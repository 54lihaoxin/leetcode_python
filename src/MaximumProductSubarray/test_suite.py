

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
#         self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()
        self.test005()

    def test000(self):
        
        print 'test 000\n'
        
        n = [2,3,-2,4]
        startTime = time.clock()
        r = Solution().maxProduct(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = [-2,3,-4]
        startTime = time.clock()
        r = Solution().maxProduct(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = [0, 2]
        startTime = time.clock()
        r = Solution().maxProduct(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        n = [-4, -3]
        startTime = time.clock()
        r = Solution().maxProduct(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        n = [-2, 0, -1]
        startTime = time.clock()
        r = Solution().maxProduct(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t', ?
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        n = [1, 0, 0, 0]
        startTime = time.clock()
        r = Solution().maxProduct(n)
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
    