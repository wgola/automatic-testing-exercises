import unittest

from hamming import Hamming


class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(Hamming.distance("", ""), 0)

    def test_single_letter_identical_strands(self):
        self.assertEqual(Hamming.distance("A", "A"), 0)

    def test_single_letter_different_strands(self):
        self.assertEqual(Hamming.distance("G", "T"), 1)

    def test_long_identical_strands(self):
        self.assertEqual(Hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG"), 0)

    def test_long_different_strands(self):
        self.assertEqual(Hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

    def test_disallow_first_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            Hamming.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaisesWithMessage(ValueError):
            Hamming.distance("ATA", "AGTG")

    def test_disallow_left_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            Hamming.distance("", "G")

    def test_disallow_right_empty_strand(self):
        with self.assertRaisesWithMessage(ValueError):
            Hamming.distance("G", "")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")
