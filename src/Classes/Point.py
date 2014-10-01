
# Definition for a point
class Point:
    
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
        
    def __repr__(self):
        return '({0},{1})'.format(self.x, self.y)
        