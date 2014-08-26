

import sys
from solution import Solution
from TreeNode import TreeNode
from TreeNode import getTreeFromString

class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
        self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        s = '{1,2,3,#,#,4,#,#,5}'
        root = getTreeFromString(s)
        r = Solution().isValidBST(root)
        print '  input:\t', s
        print '  expect:\t', False 
        print '  output:\t', r
        print

    def test001(self):
        
        print 'test 001\n'
        
        s = '{0,#,-1}'
        root = getTreeFromString(s)
        r = Solution().isValidBST(root)
        print '  input:\t', s
        print '  expect:\t', False 
        print '  output:\t', r
        print

    def test002(self):
        
        print 'test 001\n'
        
        s = '{10,5,15,#,#,6,20}'
        root = getTreeFromString(s)
        r = Solution().isValidBST(root)
        print '  input:\t', s
        print '  expect:\t', False 
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    