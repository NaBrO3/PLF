from __future__ import annotations
from typing import Iterable
from numbers import Number
from collections import namedtuple
from itertools import combinations
from numpy import matrix
from numpy import any as npany


class Vector(tuple):
    def __new__(self, *args: Iterable[Number]) -> Vector:
        return super().__new__(self, args)


class Point(namedtuple('Point', ['x', 'y'])):
    def __new__(self, x: Vector, y: Vector) -> Point:
        return super().__new__(self, x, y)


class Edge(namedtuple('Edge', ['s', 't'])):
    def __new__(self, s: Point, t: Point) -> Edge:
        assert len(s.x) == len(t.x)
        assert len(s.y) == len(t.y)
        assert s.x != t.x
        return super().__new__(self, s, t)


class PLF(tuple):
    def __new__(self, *args: Iterable[Edge]) -> PLF:
        # TODO: validation
        return super().__new__(self, args)

    def __call__(self, *args: Iterable[Number], error: Number = 0) -> Iterable[Number]:
        # TODO: validation

        dim = len(args)
        np = dim + 1
        ne = dim*np//2
        for pack in combinations(self, ne):
            points = set()
            for edge in pack:
                points.add(edge.s)
                points.add(edge.t)
            if len(points) != np:
                continue

            points = [point for point in points]

            r = [arg for arg in args] + [1]
            r = matrix(r).T
            R = [[point.x[i] for point in points]
                 for i in range(len(args))] + [[1] * np]
            Ry = [point.y for point in points]
            Ry = matrix(Ry)
            Ry = Ry.T
            R = matrix(R)
            l = R.I * r
            if npany(l > 1+1e-10):
                continue
            if npany(l < -1e-10):
                continue
            ry = Ry * l
            return Vector(*ry.T.tolist()[0])

        raise AssertionError
