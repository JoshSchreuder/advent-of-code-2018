import unittest
import b


def load_main():
    with open("3/input.txt", 'r') as myfile:
        return myfile.readlines()


class Test_Day_3b(unittest.TestCase):
    def test_1(self):
        self.assertEqual(b.not_overlap(lambda: [
            "#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]), 3)

    def test_main_case(self):
        self.assertEqual(b.not_overlap(load_main), 686)


if __name__ == '__main__':
    unittest.main()
