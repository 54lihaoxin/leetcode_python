

import sys
from solution import Solution
from classes import Point


class TestSuite:
    
    def run(self):
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test001(self):
        print "test 001"
        
        points = [Point(1,1),
                  Point(2,2),
                  Point(3,3),
                  Point(4,4),
                  Point(0,0),
                  Point(0,5),
                  Point(0,1),
                  Point(0,2),
                  Point(0,3),
                  Point(0,4),
                  ]
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", points
        print "  expect:\t", 6
        print "  output:\t", r
        print
    
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    