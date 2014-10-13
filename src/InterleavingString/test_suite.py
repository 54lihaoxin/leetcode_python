

from CommonClasses import *
from solution import Solution

class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        s1 = 'aabcc'
        s2 = 'dbbca'
        s3 = 'aadbbcbcac'
        startTime = time.clock()
        r = Solution().isInterleave(s1, s2, s3)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1} {2}'.format(s1, s2, s3)
        print '  expect:\t{0}'.format(True)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        s1 = 'aabcc'
        s2 = 'dbbca'
        s3 = 'aadbbbaccc'
        startTime = time.clock()
        r = Solution().isInterleave(s1, s2, s3)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1} {2}'.format(s1, s2, s3)
        print '  expect:\t{0}'.format(False)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    