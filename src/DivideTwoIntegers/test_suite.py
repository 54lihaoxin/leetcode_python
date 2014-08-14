

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
        self.test004()
#         self.test005()
#         self.test006()
#         self.test007()

    def test001(self):
        print "test 001"
        
        a = 2
        b = 3
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  output:\t", r
        print
    
    def test002(self):
        print "test 002"
        
        a = 7
        b = 3
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  output:\t", r
        print
    
    def test003(self):
        print "test 003"
        
        a = 8
        b = 2
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  output:\t", r
        print
    
    def test004(self):
        print "test 004"
        
        a = 1
        b = 1
        r = Solution().divide(a, b)
        
        print "  input:\t", a, b
        print "  output:\t", r
        print
        
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    