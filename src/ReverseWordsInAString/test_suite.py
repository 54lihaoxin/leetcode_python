

import sys
from solution import Solution
# from classes import ?


class TestSuite:
    
    def run(self):
        self.test001()
        
    def test001(self):
        print "test 001"
        
        s = " the sky is  blue  "
        r = Solution().reverseWords(s)
        
        print "  input:\t", s
        print "  expect:\t", "blue is sky the"
        print "  output:\t", r
        print
    
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    