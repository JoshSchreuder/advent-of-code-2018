import unittest
import b


def load_main():
    with open("2/input.txt", 'r') as myfile:
        return myfile.read().splitlines()


def test_1(self):
    assert b.similar(
        lambda: ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == "fgij"


def test_main_case(self):
    assert b.similar(load_main) == "tjxmoewpdkyaihvrndfluwbzc"
