# Zestaw nr 6, Dominika Jadach

# Kod testujący moduł.

import unittest
from zestaw6 import rectangles
from zestaw6.points import Point

p1 = rectangles.Rectangle(1, 1, 3, 2)
p2 = rectangles.Rectangle(1, 1, 3, 2)
p3 = rectangles.Rectangle(1, 1, 4, 3)
p4 = rectangles.Rectangle(3, 3, 5, 4)


class TestRectangle(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(rectangles.Rectangle.__eq__(p1, p2), True)
        self.assertEqual(rectangles.Rectangle.__eq__(p1, p3), False)
        self.assertEqual(rectangles.Rectangle.__eq__(p1, p4), False)

    def test_center(self):
        self.assertEqual(rectangles.Rectangle.center(p1), Point(2, 1.5))
        self.assertEqual(rectangles.Rectangle.center(p3), Point(2.5, 2))
        self.assertEqual(rectangles.Rectangle.center(p4), Point(4, 3.5))

    def test_area(self):
        self.assertEqual(rectangles.Rectangle.area(p2), 2)
        self.assertEqual(rectangles.Rectangle.area(p3), 6)
        self.assertEqual(rectangles.Rectangle.area(p4), 2)

    def test_move(self):
        self.assertEqual(rectangles.Rectangle.move(p1, 2, 2), p4)
        self.assertEqual(rectangles.Rectangle.move(p2, 0, 0), p2)
        self.assertEqual(rectangles.Rectangle.move(p4, -2, -2), p2)
