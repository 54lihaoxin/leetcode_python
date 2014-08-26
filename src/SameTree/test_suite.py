
import sys
from solution import Solution
from TreeNode import TreeNode

class TestSuite:
    
    def run(self):
        self.test001()

    def test001(self):
        p = TreeNode('p')
        q = TreeNode('q')
        
        isSameTree = Solution().isSameTree(p, q)
#         print "input:\t", isSameTree
        print "expect:\t", False
        print "output:\t", isSameTree

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
        
        