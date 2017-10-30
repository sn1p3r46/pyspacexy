#!/usr/bin/python3

from numbers import Number
from psyspacexy.point import Point

class Box:

    def containsPoint(box, point:Point):
        """box.containsPoint(point:Point) -> bool
        Checks wether the box contains the point or not."""

        if isinstance(point,Point):
            return box._contains(point.x,point.y)
        elif isinstance(point,tuple) and len(point)==2:
            return box._contains(point[0],point[1])


    def intersects(self,other):
        return  self.maxx() >= other.minx() and other.maxx() >= self.minx() and \
                self.maxy() >= other.miny() and other.maxy() >= self.miny()


    def _contains(box,x:float,y:float):

        hsize = box.size.half()

        return  x <= box.center.x + hsize.x and x >= box.center.x - hsize.x and \
                y <= box.center.y + hsize.y and y >= box.center.y - hsize.y


    def tlq(self):
        """
        box.tlq() -> Box
        Returns the Top Left Quadrant (tlq) of the Box
        """

        half = self.size.half()
        quarter = self.size.quarter()
        return Box(Point(self.center.x - quarter.x, self.center.y + quarter.y), half)


    def trq(self):
        """
        box.trq() -> Box
        Returns the Top Right Quadrant (trq) of the Box
        """

        half = self.size.half()
        quarter = self.size.quarter()
        return Box(Point(self.center.x + quarter.x, self.center.y + quarter.y), half)


    def brq(self):
        """
        box.brq() -> Box
        Returns the Bottom Right Quadrant (brq) of the Box
        """

        half = self.size.half()
        quarter = self.size.quarter()
        return Box(Point(self.center.x + quarter.x, self.center.y - quarter.y), half)


    def blq(self):
        """
        box.blq() -> Box
        Returns the Bottom Left Quadrant (blq) of the Box
        """

        half = self.size.half()
        quarter = self.size.quarter()
        return Box(Point(self.center.x - quarter.x, self.center.y - quarter.y), half)


    def maxx(self):
        """Returns the max x of the Box """
        return self.center.x + self.size.half().x


    def minx(self):
        """Returns the min x of the Box """
        return self.center.x - self.size.half().x


    def maxy(self):
        """Returns the max y of the Box """
        return self.center.y + self.size.half().y


    def miny(self):
        """Returns the min y of the Box """
        return self.center.y - self.size.half().y



    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Box(Center:{} Size:{})".format(self.center,self.size)

    def __init__(self, center:Point, size:Point):

        self.center = center
        if isinstance(size,Point):
            self.size = size
        elif isinstance(size,Number):
            self.size = Point(size,size)
        else:
            raise TypeError('Invalid type for "size", it must be a box.point.Point or a number')

    def __eq__(self,other):
        if self == None or other == None:
            return False
        elif type(self) == type(other):
            return self.center == other.center and self.distance == self.center


if __name__ == "__main__":

    import doctest
    doctest.testmod(extraglobs={'b0': Box(Point(3,3),2), 'b1' : Box(Point(3,3),0)})

"""

    inside_points = [Point(x,y) for x in (0.4,0.6) for y in (0.4,0.6)]

    temp = [Point(x,y) for x in (0,1,-1) for y in (0,1,-1)]

    all_points = [p0 + p1 for p0 in inside_points for p1 in temp]
    b = Box(Point(0.5,0.5) , Point(1,1))

    print(b)
    print(b.tlq())
    print(b.trq())
    print(b.brq())
    print(b.blq())


    for p in all_points:
        print("{} is inside {}: {}".format(p,b,b.containsPoint(p)))

    pp0 = Point(0,0)
    pp1 = Point(1,2)
    pp2 = Point(1,2)
    pp3 = Point(1,3)

    print (pp0==pp1)
    print (pp1==pp1)
    print (pp2==pp1)
    print (pp1==pp2)

    print (pp0.distancePoint(pp1))
    print (pp1.distancePoint(pp2))
    print (pp2.distancePoint(pp1))
    print (pp2.distance(0,0))

    print (pp0.half())
    print (pp1.half())

    from matplotlib import pyplot as plt

    xs = [p.x for p in all_points]
    ys = [p.y for p in all_points]

    colors = ['b' if b.containsPoint(x) else 'r' for x in all_points ]

    plt.scatter(xs,ys,color=colors)



    plt.plot([0,1],[1,1],[0,0],[1,0],[1,1],[1,0],[0,1],[0,0],color="black")


    plt.show()

"""
