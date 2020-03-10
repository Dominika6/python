from zadanie7.points import Point
import unittest


class Rectangles:

    def __init__(self, x1, y1, x2, y2):
        if x1 > x2 and y1 > y2:
            raise ValueError("ValueError")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "), (" + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")]"

    def __repr__(self):
        return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(
            self.pt2.y) + ")"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)
        return self

    def intersection(self, other):
        x1 = self.pt1.x
        x2 = self.pt2.x
        y1 = self.pt1.y
        y2 = self.pt2.y
        x3 = other.pt1.x
        x4 = other.pt2.x
        y3 = other.pt1.y
        y4 = other.pt2.y

        if y2 >= y4 > y1 >= y3 and x2 >= x4 > x1 >= x3:
            return Rectangles(x1, y1, x4, y4)
        elif (y2 >= y4 > y1 >= y3) and (x4 >= x2 > x3 >= x1):
            return Rectangles(x3, y1, x2, y4)
        elif (y4 >= y2 > y3 >= y1) and x2 >= x4 > x1 >= x3:
            return Rectangles(x1, y3, x4, y2)
        elif (y4 >= y2 > y3 >= y1) and (x4 >= x2 > x3 >= x1):
            return Rectangles(x3, y3, x2, y2)
        else:
            return False

    def cover(self, other):

        x1 = self.pt1.x
        x2 = self.pt2.x
        y1 = self.pt1.y
        y2 = self.pt2.y
        x3 = other.pt1.x
        x4 = other.pt2.x
        y3 = other.pt1.y
        y4 = other.pt2.y

        if (y2 >= y4 > y1 >= y3) and (x2 >= x4 > x1 >= x3):
            return Rectangles(x3, y3, x2, y2)
        elif (y2 >= y4 > y1 >= y3) and (x4 >= x2 > x3 >= x1):
            return Rectangles(x1, y3, x4, y2)
        elif (y4 >= y2 > y3 >= y1) and (x2 >= x4 > x1 >= x3):
            return Rectangles(x3, y1, x2, y4)
        elif (y4 >= y2 > y3 >= y1) and (x4 >= x2 > x3 >= x1):
            return Rectangles(x1, y1, x4, y4)

    def make4(self):

        point = self.center()

        pr1 = Rectangles(self.pt1.x, self.pt1.y, point.x, point.y)
        pr2 = Rectangles(point.x, point.y, self.pt2.x, self.pt2.y)
        pr3 = Rectangles(point.x, self.pt1.y, self.pt2.x, point.y)
        pr4 = Rectangles(self.pt1.x, point.y, point.x, self.pt2.y)

        return [pr1, pr2, pr3, pr4]


p1 = Rectangles(1, 1, 4, 3)
p2 = Rectangles(3, 2, 6, 4)
p3 = Rectangles(1, 7, 3, 8)
p4 = Rectangles(2, 6, 4, 8)


class TestRectangle(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual(Rectangles.intersection(p1, p2), Rectangles(3, 2, 4, 3))
        self.assertEqual(Rectangles.intersection(p3, p4), Rectangles(2, 7, 3, 8))
        self.assertEqual(Rectangles.intersection(p1, p4), False)

    def test_cover(self):
        self.assertEqual(Rectangles.cover(p1, p2), Rectangles(1, 1, 6, 4))
        self.assertEqual(Rectangles.cover(p3, p4), Rectangles(1, 6, 4, 8))

    def test_make4(self):
        self.assertEqual(Rectangles.make4(p1), [Rectangles(1, 1, 2.5, 2.0),
                                                Rectangles(2.5, 2.0, 4, 3),
                                                Rectangles(2.5, 1, 4, 2.0),
                                                Rectangles(1, 2.0, 2.5, 3)])

        self.assertEqual(Rectangles.make4(p4), [Rectangles(2, 6, 3.0, 7.0),
                                                Rectangles(3.0, 7.0, 4, 8),
                                                Rectangles(3.0, 6, 4, 7.0),
                                                Rectangles(2, 7.0, 3.0, 8)])


if __name__ == '__main__':
    unittest.main()
