import unittest
import a


def load_main():
    with open("1/input.txt", 'r') as myfile:
        return myfile.readlines()


class Test_Day_1a(unittest.TestCase):
    def test_1(self):
        self.assertEqual(a.getFrequencies(lambda: ["+1", "-2", "+3", "+1"]), 3)

    def test_2(self):
        self.assertEqual(a.getFrequencies(lambda: ["+1", "+1", "+1"]), 3)

    def test_3(self):
        self.assertEqual(a.getFrequencies(lambda: ["+1", "+1", "-2"]), 0)

    def test_4(self):
        self.assertEqual(a.getFrequencies(lambda: ["-1", "-2", "-3"]), -6)

    def test_main_case(self):
        self.assertEqual(a.getFrequencies(load_main), 533)


if __name__ == '__main__':
    unittest.main()
