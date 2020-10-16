import unittest
from longest_adjacent_sequence import longest_adjacent_color_sequence


class TestLongestadjacentSequence(unittest.TestCase):
    def test_longest_adjacent_sequence(self):
        count = longest_adjacent_color_sequence("test_1")
        self.assertEqual(count, 2)

        count = longest_adjacent_color_sequence("test_2")
        self.assertEqual(count, 7)

        count = longest_adjacent_color_sequence("test_3")
        self.assertEqual(count, 22)

        count = longest_adjacent_color_sequence("test_4")
        self.assertEqual(count, 1000000)


if __name__ == '__main__':
    unittest.main()
