"""
There is a list of rectangles and a list of points in a 2d space. 
Note that the edge of each rectangle are aligned to XY axis. 
How to find rectangles with point or points inside?
"""


"""

Data model:

Points is a list of tuples (x,y)
Rectangles is a list of list of 2 points: Left bottom corner, Right top corner 
--> Because edges are aligned to X,Y

Worst case: O(n)

"""


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

class Rectangle:
    def __init__(self,lb,rt):
        self.LeftBottom = lb
        self.RightTop = rt
        
        
    def contains(self,points):
        for point in points:
            if point.x < self.LeftBottom.x or point.x > self.RightTop.x or point.y < self.LeftBottom.y or point.y > self.RightTop.y:
                return False
        return True