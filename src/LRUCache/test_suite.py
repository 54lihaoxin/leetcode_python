

from CommonClasses import *
from solution import LRUCache


class TestSuite:
    
    def run(self):
        self.test000()
        self.test001()
#         self.test002()
#         self.test003()
#         self.test004()

    def test000(self):
        
        print 'test 000\n'
        
        startTime = time.clock()
        c = LRUCache(3)
        c.set(0, 'a')
        print c.get(0), c.get(1), c.get(2), c.get(3)
        c.set(1, 'b')
        print c.get(0), c.get(1), c.get(2), c.get(3)
        c.set(0, 'c')
        print c.get(0), c.get(1), c.get(2), c.get(3)
        c.set(2, 'd')
        print c.get(0), c.get(1), c.get(2), c.get(3)
        c.set(1, 'e')
        print c.get(0), c.get(1), c.get(2), c.get(3)
        timeUsed = time.clock() - startTime
        
#         print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(c)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print
        
    

    def test001(self):
        
        print 'test 001\n'
        
        startTime = time.clock()
        c = LRUCache(1)
        c.set(2, 1)
        print c.get(2)
        c.set(3, 2)
        print c.get(2)
        print c.get(3)
        timeUsed = time.clock() - startTime
        
#         print '  input:\t{0}'.format(n)
#         print '  expect:\t{0}'.format(?)
        print '  output:\t{0}'.format(c)
        print '  time used:\t{0:.6f}'.format(timeUsed)
        print


def main(argv):
    TestSuite().run()

if __name__ == '__main__':
    main(sys.argv)
    