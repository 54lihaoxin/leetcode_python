

from CommonClasses import *
from solution import Solution


class TestSuite:
    
    def run(self):
        self.test000()
#         self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        n = 1
        
        while n < 100:  #4000:
            
            r = Solution().intToRoman(n) 
            
            print '  input:\t', n
#             print '  expect:\t', ?
            print '  output:\t', r
            print
            
            n += 1
        
def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    