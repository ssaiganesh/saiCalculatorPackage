import unittest
import saicalculator


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(saicalculator.add(10, 5), 15)
        self.assertEqual(saicalculator.add(-1, -1), -2)
        self.assertEqual(saicalculator.add(-5, 0), -5)
        self.assertEqual(saicalculator.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(saicalculator.subtract(10, 5), 5)
        self.assertEqual(saicalculator.subtract(-1, -1), 0)
        self.assertEqual(saicalculator.subtract(-5, 0), -5)
        self.assertEqual(saicalculator.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(saicalculator.multiply(10, 5), 50)
        self.assertEqual(saicalculator.multiply(-1, -1), 1)
        self.assertEqual(saicalculator.multiply(-5, 0), 0)
        self.assertEqual(saicalculator.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(saicalculator.divide(10, 5), 2)
        self.assertEqual(saicalculator.divide(-1, -1), 1)
        self.assertEqual(saicalculator.divide(-1, 1), -1)
        self.assertEqual(saicalculator.divide(5, 2), 2.5)
        # self.assertRaises(ValueError, calc.divide(10, 0))  # does not work for this
        with self.assertRaises(ValueError):
            saicalculator.divide(10, 0)


# The following code helps to reduce the need of doing "python -m unittest test_saicalculator.py
if __name__ == "__main__":
    unittest.main()