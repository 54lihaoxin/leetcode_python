

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
        self.test006()

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

    def test006(self):
        print "test 006"
        
        original_points = [(-240,-657),(-27,-188),(-616,-247),(-264,-311),(-352,-393),(-270,-748),(3,4),(-308,-87),(150,526),(0,-13),(-7,-40),(-3,-10),(-531,-892),(-88,-147),(4,-3),(-873,-555),(-582,-360),(-539,-207),(-118,-206),(970,680),(-231,-47),(352,263),(510,143),(295,480),(-590,-990),(-236,-402),(308,233),(-60,-111),(462,313),(-270,-748),(-352,-393),(-35,-148),(-7,-40),(440,345),(388,290),(270,890),(10,-7),(60,253),(-531,-892),(388,290),(-388,-230),(340,85),(0,-13),(770,473),(0,73),(873,615),(-42,-175),(-6,-8),(49,176),(308,222),(170,27),(-485,-295),(170,27),(510,143),(-18,-156),(-63,-316),(-28,-121),(396,304),(472,774),(-14,-67),(-5,7),(-485,-295),(118,186),(-154,-7),(-7,-40),(-97,-35),(4,-9),(-18,-156),(0,-31),(-9,-124),(-300,-839),(-308,-352),(-425,-176),(-194,-100),(873,615),(413,676),(-90,-202),(220,140),(77,113),(-236,-402),(-9,-124),(63,230),(-255,-118),(472,774),(-56,-229),(90,228),(3,-8),(81,196),(970,680),(485,355),(-354,-598),(-385,-127),(-2,7),(531,872),(-680,-263),(-21,-94),(-118,-206),(616,393),(291,225),(-240,-657),(-5,-4),(1,-2),(485,355),(231,193),(-88,-147),(-291,-165),(-176,-229),(154,153),(-970,-620),(-77,33),(-60,-111),(30,162),(-18,-156),(425,114),(-177,-304),(-21,-94),(-10,9),(-352,-393),(154,153),(-220,-270),(44,-24),(-291,-165),(0,-31),(240,799),(-5,-9),(-70,-283),(-176,-229),(3,8),(-679,-425),(-385,-127),(396,304),(-308,-352),(-595,-234),(42,149),(-220,-270),(385,273),(-308,-87),(-54,-284),(680,201),(-154,-7),(-440,-475),(-531,-892),(-42,-175),(770,473),(118,186),(-385,-127),(154,153),(56,203),(-616,-247)]
        points = []
        
        for p in original_points:
            points.append(Point(p[0], p[1]))
        
        r = Solution().maxPoints(points)
        
        print "  input:\t", '[len:'+str(len(points))+']', points
        print "  expect:\t", '?'
        print "  output:\t", r
        print
    
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    