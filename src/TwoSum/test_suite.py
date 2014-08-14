

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()
#         self.test005()
#         self.test006()
#         self.test007()

    def test001(self):
        print "test 001"
        
        a = [2, 7, 11, 15]
        target = 9
        r = Solution().twoSum(a, target)
        
        print "  input:\t", a, target
        print "  expect:\t", (1, 2)
        print "  output:\t", r
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    