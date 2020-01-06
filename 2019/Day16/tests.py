import unittest
import main

class Test_phases(unittest.TestCase):
    def test_first_example(self):
        input_array = '12345678'
        phases = 4
        result_expected = '01029498'
        result_actual = main.run_simulation(input_array, phases)[0:8]
        self.assertEqual(result_actual, result_expected)

    def test_second_example(self):
        input_array = '80871224585914546619083218645595'
        phases = 100
        result_expected = '24176176'
        result_actual = main.run_simulation(input_array, phases)[0:8]
        self.assertEqual(result_actual, result_expected)

    def test_third_example(self):
        input_array = '19617804207202209144916044189917'
        phases = 100
        result_expected = '73745418'
        result_actual = main.run_simulation(input_array, phases)[0:8]
        self.assertEqual(result_actual, result_expected)

    def test_fourth_example(self):
        input_array = '69317163492948606335995924319873'
        phases = 100
        result_expected = '52432133'
        result_actual = main.run_simulation(input_array, phases)[0:8]
        self.assertEqual(result_actual, result_expected)

    def test_create_pattern_array_length_8_repetition_1(self):
        repetition_count = 1
        length = 8
        result_expected = [ 1, 0, -1, 0, 1, 0, -1, 0 ]
        result_actual = main.create_pattern_array(repetition_count, length)
        self.assertEqual(result_actual, result_expected)

    def test_create_pattern_array_length_8_repetition_2(self):
        repetition_count = 2
        length = 8
        result_expected = [ 0, 1, 1, 0, 0, -1, -1, 0, 0 ]
        result_actual = main.create_pattern_array(repetition_count, length)
        self.assertEqual(result_actual, result_expected)

if __name__ == '__main__':
    unittest.main()

