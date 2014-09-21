

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
        
        preOrder = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
        inOrder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        startTime = time.clock()
        r = Solution().buildTree(preOrder, inOrder)
        timeUsed = time.clock() - startTime
        
        print '  input:\t{0} {1}'.format(preOrder, inOrder)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(r)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    