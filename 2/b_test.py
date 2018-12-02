import unittest
import b


def load_main():
    with open("2/input.txt", 'r') as myfile:
        return myfile.read().splitlines()


class Test_Day_2a(unittest.TestCase):
    def test_1(self):
        self.assertEqual(b.similar(
            lambda: ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]), "fgij")

    def test_main_case(self):
        self.assertEqual(b.similar(load_main), "tjxmoewpdkyaihvrndfluwbzc")


if __name__ == '__main__':
    unittest.main()
