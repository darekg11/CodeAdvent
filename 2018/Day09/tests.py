import unittest
import main

class Test_HighestScore(unittest.TestCase):
    def test_first_example(self):
        player_number, score = main.findHighestRankedElve(10, 1618)
        self.assertEqual(score, 8317)
    def test_second_example(self):
        player_number, score = main.findHighestRankedElve(13, 7999)
        self.assertEqual(score, 146373)
    def test_third_example(self):
        player_number, score = main.findHighestRankedElve(17, 1104)
        self.assertEqual(score, 2764)
    def test_fourth_example(self):
        player_number, score = main.findHighestRankedElve(21, 6111)
        self.assertEqual(score, 54718)
    def test_fifth_example(self):
        player_number, score = main.findHighestRankedElve(30, 5807)
        self.assertEqual(score , 37305)

if __name__ == '__main__':
    unittest.main()

