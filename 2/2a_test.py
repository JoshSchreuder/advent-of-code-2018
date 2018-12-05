import unittest
import a


def load_main():
    with open("2/input.txt", 'r') as myfile:
        return myfile.readlines()


def test_1():
    assert a.checksum(lambda: [
        "abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]) == 12


def test_main_case():
    assert a.checksum(load_main) == 7872
