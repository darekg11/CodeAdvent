import unittest
import main

class Test_sort_carts(unittest.TestCase):
    def test_every_cart_in_different_x(self):
        carts = [[0, 1, 1], [0, 2, 1], [0, 4, 1], [0, 3, 1]]
        sorted_carts = main.sort_carts(carts)
        expected_sorted_result = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1]]
        self.assertEqual(sorted_carts, expected_sorted_result)
    
    def test_every_multiple_in_the_same_x_with_dfferent_y(self):
        carts = [[0, 1, 6], [0, 1, 2], [0, 4, 1], [0, 3, 1], [0, 1, 5]]
        sorted_carts = main.sort_carts(carts)
        expected_sorted_result = [[0, 1, 2], [0, 1, 5], [0, 1, 6], [0, 3, 1], [0, 4, 1]]
        self.assertEqual(sorted_carts, expected_sorted_result)

if __name__ == '__main__':
    unittest.main()

