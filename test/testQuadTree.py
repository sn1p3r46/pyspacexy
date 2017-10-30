#!/usr/bin/python3

from psyspacexy.box import Box
from psyspacexy.point import Point
from psyspacexy.QuadTree import QuadTree

import unittest
import random
import sys

class testQuadTree(unittest.TestCase):

    def setUp(self):

        self.pts = ((2,2),(-2,-2),(-1,1),(0.5,-0.5),(0.4,-0.4),(0.3,-0.3),(0.5,-1.5),(1.5,-0.5),(1.5,-1.5))
        #self.pts = ([(1,1)])

    def test_QuadTree_constr(self):
        tree = QuadTree(self.pts)
        self.assertEqual(len(tree.pList),len(self.pts))
        print(tree.findNeighbourPoint(Point(2,-2)))

    def test_random(self):

        low = -50
        high = 50

        for i in range(10):
            myPoints = [(random.uniform(low, high), random.uniform(low, high)) for k in range(10000)]
            tree = QuadTree(myPoints)
            print (i)

            for j in range(10000):
                newPoint = Point(random.uniform(low, high), random.uniform(low, high))
                #print(newPoint)
                self.assertEqual(tree.findNeighbourPoint(newPoint),self.bruteforce_findNeighbourPoint(myPoints,newPoint))


    def bruteforce_findNeighbourPoint(self,points,newPoint):

        dist = float("inf")
        res  = None

        for i in points:
            nd = newPoint.distance(i[0],i[1])
            if nd <= dist:
                dist = nd
                res = i

        return Point(res[0],res[1])




if __name__ == '__main__':

    unittest.main()
