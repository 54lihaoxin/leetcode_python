

import sys
from solution import Solution
from classes import Point


class TestSuite:
    
    def run(self):
        self.test001()
        self.test002()
        self.test003()
        self.test004()
        self.test005()

    def test001(self):
        print "test 001"
        
        points = [Point(1,1),
                  Point(2,2),
                  Point(3,3),
                  Point(4,4),
                  Point(7,7),
                  Point(0,0),
                  Point(0,1),
                  Point(0,2),
                  Point(0,3),
                  Point(0,4),
                  Point(0,5),
                  Point(0,0),
                  Point(0,0),
                  Point(0,8),
                  Point(0,9),
                  Point(1,1),
                  Point(1,2),
                  Point(1,3),
                  Point(1,4),
                  Point(2,1),
                  Point(3,1),
                  Point(4,1),
                  Point(5,1),
                  ]
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", points
        print "  expect:\t", 10
        print "  output:\t", r
        print
    
    def test002(self):
        print "test 002"
        
        points = [Point(0,0),
                  Point(0,0),
                  Point(0,0),
                  ]
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", points
        print "  expect:\t", 3
        print "  output:\t", r
        print
    
    def test003(self):
        print "test 003"
        
        points = [Point(0,0),
                  Point(1,1),
                  Point(1,-1),
                  ]
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", points
        print "  expect:\t", 2
        print "  output:\t", r
        print
    
    def test004(self):
        print "test 004"
        
        points = [Point(0,0),
                  Point(-1,-1),
                  Point(2,2),
                  ]
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", points
        print "  expect:\t", 3
        print "  output:\t", r
        print
    
    def test005(self):
        print "test 005"
        
        points = [Point(1,1),
                  Point(1,1),
                  Point(2,3),
                  ]
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", points
        print "  expect:\t", 3, "// hxl: I think it should be 2..."
        print "  output:\t", r
        print
    
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    