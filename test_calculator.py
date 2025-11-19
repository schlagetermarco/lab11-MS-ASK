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
    ##########################

    ######## Partner 1
    # def test_multiply(self):  # 3 assertions
    #     fill in code
    #
    # def test_divide(self):  # 3 assertions
    #     fill in code
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
    ##########################

    ######## Partner 1
    # def test_log_invalid_argument(self):  # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    #
    # def test_hypotenuse(self):  # 3 assertions
    #     fill in code
    #
    # def test_sqrt(self):  # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
