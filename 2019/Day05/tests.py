import unittest
import main

class Test_decode_opcode(unittest.TestCase):
    def test_single_digit_opcode(self):
        test_program = [ 1, 3, 3, 4]
        opcode_decoded = main.decode_opcode(test_program, 0)
        self.assertEqual(opcode_decoded['OP_CODE'], 1)
        self.assertEqual(opcode_decoded['FIRST_PARAM_MODE'], 0)
        self.assertEqual(opcode_decoded['SECOND_PARAM_MODE'], 0)
        self.assertEqual(opcode_decoded['THIRD_PARAM_MODE'], 0)

    def test_three_digit_opcode(self):
        test_program = [ 111, 3, 3, 4]
        opcode_decoded = main.decode_opcode(test_program, 0)
        self.assertEqual(opcode_decoded['OP_CODE'], 11)
        self.assertEqual(opcode_decoded['FIRST_PARAM_MODE'], 1)
        self.assertEqual(opcode_decoded['SECOND_PARAM_MODE'], 0)
        self.assertEqual(opcode_decoded['THIRD_PARAM_MODE'], 0)

    def test_four_digit_opcode(self):
        test_program = [ 1011, 3, 3, 4]
        opcode_decoded = main.decode_opcode(test_program, 0)
        self.assertEqual(opcode_decoded['OP_CODE'], 11)
        self.assertEqual(opcode_decoded['FIRST_PARAM_MODE'], 0)
        self.assertEqual(opcode_decoded['SECOND_PARAM_MODE'], 1)
        self.assertEqual(opcode_decoded['THIRD_PARAM_MODE'], 0)

if __name__ == '__main__':
    unittest.main()

