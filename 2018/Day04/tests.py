import unittest
import main

class Test_ParsingGuardIdLine(unittest.TestCase):
    def test_one_letter_id(self):
        self.assertEqual(main.parseGuardLine('[1518-03-03 00:04] Guard #2 begins shift'), 2)
    def test_two_letter_id(self):
        self.assertEqual(main.parseGuardLine('[1518-03-03 00:04] Guard #25 begins shift'), 25)
    def test_three_letter_id(self):
        self.assertEqual(main.parseGuardLine('[1518-03-03 00:04] Guard #381 begins shift'), 381)

class Test_ParsingRegularTimeLine(unittest.TestCase):
    def test_below_10_minutes(self):
        self.assertEqual(main.parseReguarTimeLine('[1518-03-03 00:04] Guard #2 begins shift'), 4)
    def test_above_9_minutes(self):
        self.assertEqual(main.parseReguarTimeLine('[1518-03-03 00:55] Guard #25 begins shift'), 55)

if __name__ == '__main__':
    unittest.main()

