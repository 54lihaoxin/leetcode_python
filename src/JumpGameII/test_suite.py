

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
#         self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()
#         self.test005()
        self.test006()

    def test000(self):
        
        print 'test 000\n'
        
        n = [2,3,1,1,4]
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = [3,2,1,0,4]
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = []
        i = 25000
        while 0 < i:
            n.append(i)
            i -= 1        
        n += [1, 0]
        
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        n = [0]
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test004(self):
        
        print 'test 004\n'
        
        n = [1, 2]
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test005(self):
        
        print 'test 005\n'
        
        n = [5,9,3,2,1,0,2,3,3,1,0,0]
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test006(self):
        
        print 'test 006\n'
        
        n = [9,4,5,4,1,8,1,2,0,7, 8,7,0,6,6,1,1, 2,5,0,9, 8,4,7,9,6,8,1,4,0, 8,5,5,3,9, 8,1,2,2,3,0,1,3,2, 7,9,3,0,1]
        startTime = time.clock()
        r = Solution().jump(n)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    