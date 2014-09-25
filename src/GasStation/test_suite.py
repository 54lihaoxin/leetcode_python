

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        g = [2,4,3,5,2,4,7,6]
        c = [2,1,9,2,3,1,4,2]
        startTime = time.clock()
        r = Solution().canCompleteCircuit(g, c)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(g, c)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    