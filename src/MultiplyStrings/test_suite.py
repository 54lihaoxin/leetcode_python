

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
        
        a = '123'
        b = '45'
        
        startTime = time.clock()
        r = Solution().multiply(a, b)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(a, b)
        print '  expect:\t{0}'.format(123 * 45)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        a = '123456789'
        b = '9876543210'
        
        startTime = time.clock()
        r = Solution().multiply(a, b)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(a, b)
        print '  expect:\t{0}'.format(123456789 * 9876543210)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        a = '123'
        b = '4'
        
        startTime = time.clock()
        r = Solution().multiply(a, b)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(a, b)
        print '  expect:\t{0}'.format(123 * 4)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test003(self):
        
        print 'test 003\n'
        
        a = '9369162965141127216164882458728854782080715827760307787224298083754'
        b = '7204554941577564438'
        
        startTime = time.clock()
        r = Solution().multiply(a, b)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(a, b)
        print '  expect:\t{0}'.format(9369162965141127216164882458728854782080715827760307787224298083754 * 7204554941577564438)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
    
        

def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    