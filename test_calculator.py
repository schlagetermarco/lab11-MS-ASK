import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
     def test_multiply(self): # 3 assertions
         self.assertEqual(mul(6, 8), 48)
         self.assertEqual(mul(-2, 15), -30)
         self.assertEqual(mul(22, 0), 0)

     def test_divide(self): # 3 assertions
         self.assertEqual(div(2, 15), 7.5)
         self.assertEqual(div(3, 12), 4)
         with self.assertRaises(ZeroDivisionError):
             div(0, 22)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
         with self.assertRaises(ValueError):
             logarithm(0,12)

     def test_hypotenuse(self): # 3 assertions
         self.assertAlmostEqual(hypotenuse(3, 4), 5)
         self.assertAlmostEqual(hypotenuse(-3, 4), 5)
         self.assertAlmostEqual(hypotenuse(6, 8), 10)

     def test_sqrt(self): # 3 assertions
         self.assertEqual(square_root(16), 4)
         self.assertAlmostEqual(square_root(2.25), 1.5)
         with self.assertRaises(ValueError):
             square_root(-9)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()