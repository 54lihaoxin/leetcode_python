

import sys
from solution import Solution
from classes import TreeNode
from classes import getTreeFromString

class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        root = getTreeFromString("{1,2,3,#,#,4,#,#,5}")
        r = Solution().isValidBST(root)
        print '  input:\t', root
        print '  expect:\t', True 
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    