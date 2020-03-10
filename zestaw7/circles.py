import math
from zadanie7.points import Point
import unittest


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("ValueError")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        x1 = self.pt.x
        y1 = self.pt.y
        x2 = other.pt.x
        y2 = other.pt.y

        x = (x1 + x2) / 2.
        y = (y1 + y2) / 2.
        r = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)) + other.radius

        return Circle(x, y, r)


c1 = Circle(1, 1, 1)
c2 = Circle(2, 2, 1)
c3 = Circle(2, 3, 4)
c4 = Circle(3, 4, 8)


class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(c1.area(), 3.141592653589793)
        self.assertEqual(c2.area(), 3.141592653589793)
        self.assertEqual(c3.area(), 50.26548245743669)
        self.assertEqual(c4.area(), 201.06192982974676)

    def test_move(self):
        self.assertEqual(c1.move(2, 3), Circle(3, 4, 1))
        self.assertEqual(c2.move(1, 4), Circle(3, 6, 1))
        self.assertEqual(c3.move(5, 1), Circle(7, 4, 4))
        self.assertEqual(c4.move(1, 5), Circle(4, 9, 8))

    def test_cover(self):
        self.assertEqual(c1.cover(c2), Circle(1.5, 1.5, 2.414213562373095))
        self.assertEqual(c2.cover(c3), Circle(2, 2.5, 5))
        self.assertEqual(c3.cover(c4), Circle(2.5, 3.5, 9.414213562373096))
        self.assertEqual(c4.cover(c1), Circle(2.0, 2.5, 4.60555127546399))

    if __name__ == '__main__':
        unittest.main()
