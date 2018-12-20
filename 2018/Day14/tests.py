import unittest
import main

class Test_convertLastTenRecepiesToString(unittest.TestCase):
    def test_excatly_ten_length(self):
        self.assertEqual(main.convertLastTenRecepiesToString([1,2,3,4,5,6,7,8,9,0]), '1234567890')
    def test_more_than_ten_length(self):
        self.assertEqual(main.convertLastTenRecepiesToString([1,2,3,4,5,6,7,8,9,0,1,2,3]), '4567890123')

class Test_generateRecepies(unittest.TestCase):
    def test_example(self):
        recepies = main.generateRecepies(9)
        last_ten_recepies = main.convertLastTenRecepiesToString(recepies)
        self.assertEqual(last_ten_recepies, '5158916779')

class Test_find_recepies(unittest.TestCase):
    def test_first_example(self):
        tracking_sequence = bytearray([5, 1, 5, 8, 9])
        recepies = main.find_recepies(tracking_sequence)
        length_of_recipies_prior_to_sequence = recepies.index(tracking_sequence)
        self.assertEqual(length_of_recipies_prior_to_sequence, 9)
    def test_last_example(self):
        tracking_sequence = bytearray([5, 9, 4, 1, 4])
        recepies = main.find_recepies(tracking_sequence)
        length_of_recipies_prior_to_sequence = recepies.index(tracking_sequence)
        self.assertEqual(length_of_recipies_prior_to_sequence, 2018)

class Test_move_index(unittest.TestCase):
    def test_first(self):
        self.assertEqual(main.move_index(1, len([3,7]), 4), 1)

if __name__ == '__main__':
    unittest.main()

