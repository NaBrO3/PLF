from __future__ import annotations
from typing import Iterable
from numbers import Number
from collections import namedtuple


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

    def __call__(self, *args: Iterable[Number]) -> Iterable[Number]:
        # TODO: validation
        # TODO: impl

        # for all combinations of edges find:
        # 1. len = len(args) + 1
        # 2. inner

        # solve the equation \sum cx + c = 0

        # calculate result
        return Vector()
