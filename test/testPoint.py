#!/usr/bin/python3

from psyspacexy.point import Point

import unittest


class testPoint(unittest.TestCase):

    def setUp(self):
        self.pts = [(0,1),(0,-1),(-1,0),(1,0)]
        self.pts_non_0 = [(1,1),(-1,1),(1,-1),(-1,-1)]
        self.pts_half = [(x[0]/2,x[1]/2) for x in self.pts]
        self.pts_quarter = [(x[0]*0.5,x[1]*0.5) for x in self.pts_half]


    def test_distancePoint(self):
        p = Point(0,0)
        self.assertEqual(p.distancePoint(Point(0,0)),0)

        for pt in self.pts:
            self.assertEqual(p.distancePoint(Point(*pt)),1)

        for pt in self.pts_non_0:
            self.assertEqual(p.distancePoint(Point(*pt)),2**0.5)

        exp_res = [0,2,2,8**0.5]
        for i in range(0,len(self.pts_non_0)):
            self.assertEqual(Point(1,1).distancePoint(Point(*self.pts_non_0[i])),exp_res[i])


    def test_half(self):
        for i in range(0,len(self.pts)):
            self.assertEqual(Point(*self.pts[i]).half(),Point(*self.pts_half[i]))

    def test_quarter(self):
        for i in range(0,len(self.pts)):
            self.assertEqual(Point(*self.pts[i]).quarter(),Point(*self.pts_quarter[i]))

    def test_scale(self):
        for i in range(0,len(self.pts)):
            self.assertEqual(Point(*self.pts[i]).scale(0.25),Point(*self.pts_quarter[i]))

if __name__ == '__main__':

    unittest.main()
