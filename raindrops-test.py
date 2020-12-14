import unittest

from raindrops import get_raindrops


class RaindropsTest(unittest.TestCase):
    def test_output_for_3_is_pling(self):
        self.assertEqual(get_raindrops(3), "Pling")
    def test_output_for_5_is_plang(self):
        self.assertEqual(get_raindrops(5), "Plang")
    def test_output_for_7_is_plong(self):
        self.assertEqual(get_raindrops(7), "Plong")
    def test_output_for_15_is_pling_plang(self):
        self.assertEqual(get_raindrops(15), "PlingPlang")
    def test_output_for_21_is_pling_plong(self):
        self.assertEqual(get_raindrops(21), "PlingPlong")
    def test_output_for_21_is_plang_plong(self):
        self.assertEqual(get_raindrops(35), "PlangPlong")
    def test_output_for_105_is_plang_plang_plong(self):
        self.assertEqual(get_raindrops(105), "PlingPlangPlong")
    def test_output_for_17_is_17(self):
        self.assertEqual(get_raindrops(17), "17")


if __name__ == "__main__":
    unittest.main()