

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
        
        tree = getTreeFromString('{1,#,-9,#,8,4,-3,#,#,-3,#,-6,#,#,-6,-4,-9,#,#,6}')
        startTime = time.clock()
        r = Solution().connect(tree)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(tree)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print

    def test001(self):
        
        print 'test 000\n'
        
        tree = getTreeFromString('{1,2,3,4,5,#,7}')
        startTime = time.clock()
        r = Solution().connect(tree)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0}'.format(tree)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    