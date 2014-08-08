

import sys
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
        self.test004()

    def test001(self):
        print "test 001"
        
        #         b s   b   s b   s
        prices = [3,4,3,1,5,9,2,4,8,4]
        r = Solution().maxProfit(prices)
        
        print "  input:\t", prices
        print "  expect:\t", 15
        print "  output:\t", r
        print
    
    def test002(self):
        print "test 002"
        
        #               b   s b s b s
        prices = [4,3,3,1,4,9,2,4,2,4]
        r = Solution().maxProfit(prices)
        
        print "  input:\t", prices
        print "  expect:\t", 12
        print "  output:\t", r
        print
        
    def test003(self):
        print "test 003"
        
        prices = [1,2]
        r = Solution().maxProfit(prices)
        
        print "  input:\t", prices
        print "  expect:\t", 1
        print "  output:\t", r
        print
        
    def test004(self):
        print "test 004"
        
        prices = [0,5,5,6,2,1,1,3]
        r = Solution().maxProfit(prices)
        
        print "  input:\t", prices
        print "  expect:\t", 8
        print "  output:\t", r
        print
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    