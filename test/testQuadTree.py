#!/usr/bin/python3

from psyspacexy.box import Box
from psyspacexy.point import Point
from psyspacexy.QuadTree import QuadTree

import unittest

class testQuadTree(unittest.TestCase):

    def setUp(self):

        self.pts = ((2,2),(-2,-2),(-1,1),(0.5,-0.5),(0.4,-0.4),(0.3,-0.3),(0.5,-1.5),(1.5,-0.5),(1.5,-1.5))
        #self.pts = ([(1,1)])

    def test_QuadTree_constr(self):
        self.tree = QuadTree(self.pts)
        self.assertEqual(len(self.tree.pList),len(self.pts))
        print(self.tree.findNeighbourPoint(Point(2,-2)))


if __name__ == '__main__':

    unittest.main()
