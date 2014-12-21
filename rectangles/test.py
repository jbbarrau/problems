from rectangles import Point,Rectangle


points = [ Point(x,y) for x,y in\
        [\
        (1,2),\
        (4,7),\
        (3,2),\
        (9,5),\
        (1,2),\
        (19,5),\
        ]\
    ]


    
rectangles = [ Rectangle(rt,lb) for rt, lb in\
                [Point(1,2),Point(3,4)],\
                [Point(1,2),Point(3,4)],\
                [Point(-2,-2),Point(6,6)],\
                [Point(-100,-100),Point(100,100)],\
            ]
            
print rectangles[0].contains(points)
print rectangles[3].contains(points)