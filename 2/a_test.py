import unittest
import a


def load_main():
    with open("2/input.txt", 'r') as myfile:
        return myfile.readlines()


class Test_Day_2a(unittest.TestCase):
    def test_1(self):
        self.assertEqual(a.checksum(lambda: [
                         "abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]), 12)

    def test_main_case(self):
        self.assertEqual(a.checksum(load_main), 7872)


if __name__ == '__main__':
    unittest.main()
