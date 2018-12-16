import unittest
import main

class Test_find_matching_opcodes(unittest.TestCase):
    def test_example(self):
        self.assertEqual(main.find_matching_opcodes([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1]), set(['ADDI', 'MULR', 'SETI']))

if __name__ == '__main__':
    unittest.main()

