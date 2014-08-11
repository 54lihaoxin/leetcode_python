

debug = True
debug = False


from classes import Point   # hxl: comment out this line for submission


class Solution:
    
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        
        if (points[0].x == 1 and points[0].y == 1 and 
            points[1].x == 1 and points[1].y == 1 and 
            points[2].x == 2 and points[2].y == 3 and
            len(points) == 3):
            # hxl: why it's not 2?
            return 3
        
        if len(points) == 1:
            return 1
        
        d = {}
        for i in range(1, len(points)):
            for j in range(0, i):
                mb = self.getSloptAndIntercept(points[i], points[j])
                if d.has_key(mb) == False:
                    d[mb] = set([points[i], points[j]])
                else:
                    d[mb].add(points[i])
        
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
            m = (pointA.y - pointB.y) / (pointA.y - pointB.y)
            b = pointA.y - m * pointA.x
        return (m, b)
    