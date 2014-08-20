

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print "test 000"
        
        nums = [-1,0,1,2,-1,-4]
        
        hasCycle = Solution().threeSum(nums)
        print "  input:\t", nums
        print "  expect:\t", False
        print "  output:\t", hasCycle
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    