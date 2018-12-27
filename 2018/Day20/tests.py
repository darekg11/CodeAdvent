import unittest
import main

class Test_find_furthest_door_with_minimum_path(unittest.TestCase):
    def test_example_first(self):
        test_input = '^WNE$'
        self.assertEqual(main.calculate_shortest_path_through_as_much_doors_as_possible(test_input)[0], 3)
    def test_example_second(self):
        test_input = '^ENWWW(NEEE|SSE(EE|N))$'
        self.assertEqual(main.calculate_shortest_path_through_as_much_doors_as_possible(test_input)[0], 10)
    def test_example_thrid(self):
        test_input = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
        self.assertEqual(main.calculate_shortest_path_through_as_much_doors_as_possible(test_input)[0], 18)

if __name__ == '__main__':
    unittest.main()

