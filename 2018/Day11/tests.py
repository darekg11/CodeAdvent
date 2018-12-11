import unittest
import main

class Test_CalculatePowerOfACell(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(main.calculatePowerOfACall(3,5,8), 4)
    def test_second_example(self):
        self.assertEqual(main.calculatePowerOfACall(122,79,57), -5)
    def test_third_example(self):
        self.assertEqual(main.calculatePowerOfACall(217,196,39), 0)
    def test_fourth_example(self):
        self.assertEqual(main.calculatePowerOfACall(101,153,71), 4)

class Test_CalculateLarger3x3Square(unittest.TestCase):
    def test_first_example(self):
        serial_number = 18
        grid = main.createAGridWithEveryCellCalculatedPower(serial_number)
        largest_x, largest_y, largest_power = main.findLargest3x3Square(grid)
        self.assertEqual(largest_x, 33)
        self.assertEqual(largest_y, 45)
        self.assertEqual(largest_power, 29)
    def test_second_example(self):
        serial_number = 42
        grid = main.createAGridWithEveryCellCalculatedPower(serial_number)
        largest_x, largest_y, largest_power = main.findLargest3x3Square(grid)
        self.assertEqual(largest_x, 21)
        self.assertEqual(largest_y, 61)
        self.assertEqual(largest_power, 30)

if __name__ == '__main__':
    unittest.main()

