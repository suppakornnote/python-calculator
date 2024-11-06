# 6588077 Suppakorn Pojsomphong
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 6), 11)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 9), 8)
        self.assertEqual(self.calc.subtract(3, 10), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 10), 2)
        self.assertEqual(self.calc.divide(36, 9), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(20, 3), 2)
        self.assertEqual(self.calc.modulo(9, 3), 0)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()