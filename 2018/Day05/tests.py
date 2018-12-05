import unittest
import main

class Test_ReactPolimer(unittest.TestCase):
    def test_no_reaction(self):
        self.assertEqual(main.reactPolimer('sdhYujkIYGGh'), 'sdhYujkIYGGh')
    def test_example_reaction(self):
        self.assertEqual(main.reactPolimer('dabAcCaCBAcCcaDA'), 'dabCBAcaDA')

if __name__ == '__main__':
    unittest.main()

