# Zestaw nr 6, Dominika Jadach

# W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami.
# Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych,
# o końcu w położeniu (x, y). Napisać kod testujący moduł points.

from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):   # zwraca string "Point(x, y)"
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):   # obsługa point1 == point2
        return False if self.x != other.x else False if self.y != other.y else True

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):   # długość wektora
        return sqrt(self.x * self.x + self.y * self.y)
