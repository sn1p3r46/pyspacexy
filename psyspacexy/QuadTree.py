#!/usr/bin/python3

from psyspacexy.box import Box
from psyspacexy.point import Point

class QuadTree:

    def __init__(self,coordList,maxPoints=1):

        if maxPoints < 1:
            ValueError("MaxPoints MUST be a positive integer")

        if not coordList:
            ValueError("The input provided e is not valid.")

        self.maxPoints = maxPoints
        self.maxx, self.maxy = map(max,zip(*coordList)) if len(coordList) > 1 else (coordList[0][0],coordList[0][1])
        self.minx, self.miny = map(min,zip(*coordList)) if len(coordList) > 1 else (coordList[0][0],coordList[0][1])
        self.pList = [Point(p[0],p[1]) for p in coordList]
        self.root = self._makeTree(self.pList,Box(Point(0.5*(self.minx+self.maxx),0.5*(self.miny+self.maxy)), Point(self.maxx-self.minx,self.maxy-self.miny)))


    class Node:

        def __init__(self,box,children=[],points=[]):

            self.box = box
            self.children = children
            self.points = points


    def _makeTree(self,pList,box):
        n = QuadTree.Node(box)

        if len(pList) <= self.maxPoints:
            n.points = pList

        else:
            tlq = box.tlq()
            trq = box.trq()
            brq = box.brq()
            blq = box.blq()

            n.children = [
                self._makeTree([p for p in pList if tlq.containsPoint(p)], tlq),
                self._makeTree([p for p in pList if trq.containsPoint(p)], trq),
                self._makeTree([p for p in pList if brq.containsPoint(p)], brq),
                self._makeTree([p for p in pList if blq.containsPoint(p)], blq)
                ]

        return n


    def _findNeighbourPoint(self,node,nP,bestP,distBestP):

        dist = node.box.size.half()
        if node.box.center.distancePoint(nP) - ((dist.x)**2+(dist.y)**2)**0.5 > distBestP:
            return bestP

        if (node.points):
            for p in node.points:
                nDist = p.distancePoint(nP)
                if nDist <= distBestP:
                    distBestP = nDist
                    bestP = p
                    #print(bestP,distBestP,nP)

        sortedChildren = [x for (y,x) in sorted(zip([nP.distancePoint(y.box.center) \
                                for y in node.children],node.children), \
                                    key=lambda pair: pair[0])]

        for p in sortedChildren:
            NBP = self._findNeighbourPoint(p,nP,bestP,distBestP)
            if NBP!=bestP:
                bestP = NBP
                distBestP = NBP.distancePoint(nP)

        return bestP


    def findNeighbourPoint(tree,newPoint):

        if isinstance(newPoint,tuple) and len(newPoint)==2:
            newPoint = Point(newPoint[0],newPoint[1])

        initial_distance = tree.root.box.size.x + tree.root.box.size.y
        return tree._findNeighbourPoint(tree.root,newPoint,None,initial_distance)
