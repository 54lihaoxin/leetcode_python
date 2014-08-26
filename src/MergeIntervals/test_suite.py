

import sys
from solution import Solution
from Interval import Interval


class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        a = [Interval(1, 3),
             Interval(2, 6),
             Interval(8, 10),
             Interval(15, 18)]
        
        r = Solution().merge(a)
        print '  input:\t', a 
#         print '  expect:\t', 
        print '  output:\t', r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    