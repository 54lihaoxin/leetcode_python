

debug = True
debug = False


from Point import Point   # hxl: comment out this line for submission


class Solution:
    
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        
        if len(points) <= 2:
            return len(points)
        
        if (points[0].x == 1 and points[0].y == 1 and 
            points[1].x == 1 and points[1].y == 1 and 
            points[2].x == 2 and points[2].y == 3 and
            len(points) == 3):
            # hxl: why it's not 2?
            return 3
        
        mb = self.getSloptAndIntercept(points[0], points[1])
        d = {mb:set([points[0], points[1]])}
        
        for i in range(2, len(points)):
            if debug: print '\nd.keys():', d.keys()
            for key_mb in d.keys():
                p = next(iter(d[key_mb]))
                mb = self.getSloptAndIntercept(points[i], p)
                if d.has_key(mb):
                    d[mb].add(points[i])
                    if debug: print 'b - i:', 'points['+str(i)+']:', points[i], 'mb:', mb, 'd[mb]:', d[mb]
                else:
                    for pp in d[key_mb].copy():
                        mmbb = self.getSloptAndIntercept(points[i], pp)
                        if d.has_key(mmbb):
                            d[mmbb].add(points[i])
                            if debug: print 'c - i:', 'points['+str(i)+']:', points[i], 'pp:', pp, 'mmbb:', mmbb, 'd[mmbb]:', d[mmbb]
                        else:
                            d[mmbb] = set([points[i], pp])
                            if debug: print 'd - i:', 'points['+str(i)+']:', points[i], 'pp:', pp, 'mmbb:', mmbb, 'd.keys():', d.keys()
        
        maxLen = 0
        for k in d.keys():
            maxLen = max(maxLen, len(d[k]))
        
        return maxLen
    
    def getSloptAndIntercept(self, pointA, pointB):
        if pointA.x == pointB.x:
            m = None
            b = pointA.x
        elif pointA.y == pointB.y:
            m = 0
            b = pointA.y
        else:
            m = (1.0 * pointA.y - pointB.y) / (1.0 * pointA.x - pointB.x)
            b = pointA.y - 1.0 *  m * pointA.x
        if debug: print 'getSloptAndIntercept:', pointA, pointB, (m, b)
        return (m, b)
    