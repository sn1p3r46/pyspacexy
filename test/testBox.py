#!/usr/bin/python3

from psyspacexy.box import Box
from psyspacexy.point import Point
import unittest

class testBox(unittest.TestCase):

    def setUp(self):

        self.boxes = [
            Box(Point(3,3),2),
            Box(Point(3,3),0)
        ]

        self.pts = [(1,2),(3,3),Point(1,2),Point(3,3),
                    (0,0),(4,4),(2,2),(2,4),(4,2)]

        self.ps = [(2,4),(4,4),(4,2),(2,2)]

    def test_containsPoint(self):

        expRes = [False, True, False, True, False, True, True, True, True]
        for i in range(0,len(self.pts)):
            res = self.boxes[0].containsPoint(self.pts[i])
            self.assertEqual(res,expRes[i])

        expRes = [False, True, False, True, False, False, False, False, False]
        for i in range(0,len(self.pts)):
            res = self.boxes[1].containsPoint(self.pts[i])
            self.assertEqual(res,expRes[i])

    def test_tlq(self):
        expRes = [True, False, False, False]
        for i in range(0,len(self.ps)):
            res = self.boxes[0].tlq().containsPoint(self.ps[i])
            self.assertEqual(res,expRes[i])

    def test_trq(self):
        expRes = [False, True, False, False]
        for i in range(0,len(self.ps)):
            res = self.boxes[0].trq().containsPoint(self.ps[i])
            self.assertEqual(res,expRes[i])

    def test_brq(self):
        expRes = [False, False, True, False]
        for i in range(0,len(self.ps)):
            res = self.boxes[0].brq().containsPoint(self.ps[i])
            self.assertEqual(res,expRes[i])

    def test_blq(self):
        expRes = [False, False, False, True]
        for i in range(0,len(self.ps)):
            res = self.boxes[0].blq().containsPoint(self.ps[i])
            self.assertEqual(res,expRes[i])

    def test_maxx(self):
        box = Box(Point(0,0),Point(1,1))
        self.assertEqual(1/2,box.maxx())

    def test_minx(self):
        box = Box(Point(0,0),Point(1,1))
        self.assertEqual(-1/2,box.minx())

    def test_maxy(self):
        box = Box(Point(0,0),Point(1,1))
        self.assertEqual(1/2,box.maxy())

    def test_miny(self):
        box = Box(Point(0,0),Point(1,1))
        self.assertEqual(-1/2,box.miny())

    def test_intersect(self):

        box0 = Box(Point(1,1),1)
        box1 = Box(Point(2,2),1)
        box2 = Box(Point(2.5,2.5),1/2)

        self.assertTrue(box0.intersects(box1))
        self.assertTrue(box1.intersects(box2))
        self.assertFalse(box0.intersects(box2))

        box0 = Box(Point(1,1),1)
        box1 = Box(Point(0,0),1)
        box2 = Box(Point(-1,-1),1)

        self.assertTrue(box0.intersects(box1))
        self.assertTrue(box1.intersects(box2))
        self.assertFalse(box0.intersects(box2))

        box0 = Box(Point(-1,-1),1)
        box1 = Box(Point(0,0),1)
        box2 = Box(Point(1,1),1)

        self.assertTrue(box0.intersects(box1))
        self.assertTrue(box1.intersects(box2))
        self.assertFalse(box0.intersects(box2))

        box0 = Box(Point(0,0),0)
        box1 = Box(Point(0,0),0)
        box2 = Box(Point(1,1),1)
        box3 = Box(Point(1,1),0)

        self.assertTrue(box0.intersects(box1))
        self.assertFalse(box1.intersects(box2))
        self.assertFalse(box0.intersects(box2))
        self.assertTrue(box2.intersects(box3))
        self.assertFalse(box1.intersects(box3))




if __name__ == '__main__':

    unittest.main()
