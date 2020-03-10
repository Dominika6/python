# Zestaw nr 5, Dominika Jadach


##################################################
import unittest
import fracs

f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznaczność)
f5 = [0, 2]  # zero (niejednoznaczność)


class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac(f1, f2), [-1, 2])
        self.assertEqual(fracs.add_frac(f2, f3), [3, 1])
        self.assertEqual(fracs.add_frac(f3, f4), [12, 2])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac(f1, f3), [-7, 2])
        self.assertEqual(fracs.sub_frac(f3, f4), [0, 2])
        self.assertEqual(fracs.sub_frac(f5, f3), [-6, 2])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac(f2, f3), [0, 1])
        self.assertEqual(fracs.mul_frac(f4, f1), [-6, 4])
        self.assertEqual(fracs.mul_frac(f2, f5), [0, 2])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac(f4, f1), [12, -2])
        self.assertEqual(fracs.div_frac(f3, f4), [6, 6])
        self.assertEqual(fracs.div_frac(f5, f1), [0, -2])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive(f4))
        self.assertTrue(fracs.is_positive(f3))
        self.assertFalse(fracs.is_positive(f1))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero(f2))
        self.assertTrue(fracs.is_zero(f5))
        self.assertFalse(fracs.is_zero(f3))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac(f1, f3), 1)
        self.assertEqual(fracs.cmp_frac(f4, f5), -1)
        self.assertEqual(fracs.cmp_frac(f4, f3), 0)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float(f1), -0.5)
        self.assertEqual(fracs.frac2float(f3), 3)
        self.assertEqual(fracs.frac2float(f5), 0)


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
