#!/usr/bin/python3

from numbers import Number

class Point:

    """
    This class is meant to describe and represent points in a 2D plane,it also
    implements some basic operations.
    """

    def __init__(self,x,y):

        if not isinstance(x,Number) or not isinstance(y,Number):
            TypeError("Coordinates x and y must be numbers")

        self.x = x
        self.y = y


    def __str__(self):
        return "Point(x:{} y:{})".format(self.x,self.y)


    def __repr__(self):
        return self.__str__()


    def __add__(self,other):
        if isinstance(other,Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)


    def __eq__(self,other):
        if self is None or other is None:
            return False
        return self.x == other.x and self.y == other.y


    def __mul__(self,val):
        return Point(self.x*val,self.y*val)


    def distancePoint(self,other):
        """Computers the distance with the Point provided as input"""
        return self.distance(other.x,other.y)


    def distance(self,x,y):
        """Computers the distance with the coordinates provided as input"""
        return ((self.x - x)**2+(self.y - y)**2)**0.5


    def half(self):
        """Multiplies both coordinates (x and y) by 0.5"""
        return self*(0.5)


    def quarter(self):
        """Multiplies both coordinates (x and y) by 0.25"""
        return self*(0.25)


    def scale(self,factor):
        """Multiplies both coordinates (x and y) by factor"""
        return self*factor
