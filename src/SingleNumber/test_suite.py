

import sys
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test001()

    def test001(self):
        s = Solution()
        numbers = [5,2,5,1,4,3,6,4,3,2,6]
        n = s.singleNumber(numbers)
        print "input:\t", numbers
        print "expect:\t", 1
        print "output:\t", n


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)