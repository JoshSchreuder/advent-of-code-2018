import unittest
import a


def load_main():
    with open("3/input.txt", 'r') as myfile:
        return myfile.readlines()


def test_1(self):
    assert a.overlap(
        lambda: ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]) == 4


def test_main_case(self):
    assert a.overlap(load_main) == 103482
