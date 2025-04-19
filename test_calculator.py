import unittest
import add
import subtract
import multiply
import divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.add(5, 3), 8)
        self.assertEqual(add.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract.subtract(10, 5), 5)
        self.assertEqual(subtract.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply.multiply(4, 2), 8)
        self.assertEqual(multiply.multiply(-1, 3), -3)

    def test_divide(self):
        self.assertEqual(divide.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
