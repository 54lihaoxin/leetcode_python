

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
        
        exp = ["2", "1", "+", "3", "*"]
        
        r = Solution().evalRPN(exp)
        
        print "  input:\t", exp
        print "  expect:\t", ((2 + 1) * 3)
        print "  output:\t", r
        print

    def test002(self):
        
        print "test 002"
        
        exp = ["4", "13", "5", "/", "+"]
        
        r = Solution().evalRPN(exp)
        
        print "  input:\t", exp
        print "  expect:\t", (4 + (13 / 5))
        print "  output:\t", r
        print

    def test003(self):
        
        print "test 003"
        
        exp = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
        
        r = Solution().evalRPN(exp)
        
        print "  input:\t", exp
        print "  expect:\t", 163
        print "  output:\t", r
        print

    def test004(self):
        
        print "test 004"
        
        exp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        
        r = Solution().evalRPN(exp)
        
        print "  input:\t", exp
        print "  expect:\t", 22 # hxl: I think this should be 12...
        print "  output:\t", r
        print

        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    