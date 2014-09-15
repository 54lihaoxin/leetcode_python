

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        n = [2,3,6,7]
        target = 7
        startTime = time.clock()
        r = Solution().combinationSum2(n, target)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, target)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 001\n'
        
        n = [10,1,2,7,6,1,5]
        target = 8
        startTime = time.clock()
        r = Solution().combinationSum2(n, target)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, target)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test002(self):
        
        print 'test 002\n'
        
        n = [28,18,28,19,26,8,14,17,10,6,31,23,33,7,10,13,16,12,6,17,19,22,14,30,16,5,29,20,29,9,28,15,22,21,29,13,17,30,17,22,23,5,33,21,7,8,30,10,8,23,15,22,10,24,9,22,24,33,29,11,7,14,21,16,23]
        target = 22
        startTime = time.clock()
        r = Solution().combinationSum2(n, target)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(n, target)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
        

def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    