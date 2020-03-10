# Zestaw nr 6, Dominika Jadach

# Kod testujący moduł.

import unittest
from zestaw6 import points

p1 = points.Point(0, 0)
p2 = points.Point(1, 0)
p3 = points.Point(0, 1)
p4 = points.Point(1, 1)
p5 = points.Point(1, 2)


class TestPoint(unittest.TestCase):

    def test_add(self):
        self.assertEqual(points.Point.__add__(p1, p2), p2)
        self.assertEqual(points.Point.__add__(p3, p2), p4)
        self.assertEqual(points.Point.__add__(p3, p4), p5)

    def test_sub(self):
        self.assertEqual(points.Point.__sub__(p4, p1), p4)
        self.assertEqual(points.Point.__sub__(p4, p2), p3)
        self.assertEqual(points.Point.__sub__(p5, p4), p3)

    def test_mul(self):
        self.assertEqual(points.Point.__mul__(p1, p5), 0)
        self.assertEqual(points.Point.__mul__(p4, p5), 3)
        self.assertEqual(points.Point.__mul__(p2, p5), 1)

    def test_cross(self):
        self.assertEqual(points.Point.cross(p2, p5), 2)
        self.assertEqual(points.Point.cross(p3, p1), 0)
        self.assertEqual(points.Point.cross(p2, p4), 1)

    def test_length(self):
        self.assertEqual(points.Point.length(p1), 0)
        self.assertEqual(points.Point.length(p2), 1)
        self.assertEqual(points.Point.length(p3), 1)

