# GitHub link:https://github.com/schlagetermarco/lab11-MS-ASK
# Partner 1 : Marco Schlageter
# Partner 2 : Akash Kodavati

import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 5), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 3), 7)
        self.assertEqual(subtract(3, 10), -7)
        self.assertEqual(subtract(5, 0), 5)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(6, 8), 48)
        self.assertEqual(mul(-2, 15), -30)
        self.assertEqual(mul(22, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 15), 7.5)
        self.assertEqual(div(3, 12), 4)
        with self.assertRaises(ZeroDivisionError):
            div(0, 22)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # div(a, b) does b / a, and should raise if a == 0
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        # logarithm(a, b) is log base a of b
        self.assertAlmostEqual(logarithm(2, 8), 3.0)      # log_2(8) = 3
        self.assertAlmostEqual(logarithm(10, 100), 2.0)   # log_10(100) = 2
        self.assertAlmostEqual(logarithm(4, 16), 2.0)     # log_4(16) = 2

    def test_log_invalid_base(self):  # 1 assertion
        # invalid base: a == 1 should raise ValueError
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 12)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2.25), 1.5)
        with self.assertRaises(ValueError):
            square_root(-9)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
