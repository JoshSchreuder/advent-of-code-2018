import unittest
import b


def load_main():
    with open("1/input.txt", 'r') as myfile:
        return myfile.readlines()


def test_1(self):
    assert b.getFrequencies(lambda: ["+1", "-2", "+3", "+1"]) == 2


def test_2(self):
    assert b.getFrequencies(lambda: ["+1", "-1"]) == 0


def test_3(self):
    assert b.getFrequencies(
        lambda: ["+3", "+3", "+4", "-2", "-4"]) == 10


def test_4(self):
    assert b.getFrequencies(
        lambda: ["-6", "+3", "+8", "+5", "-6"]) == 5


def test_5(self):
    assert b.getFrequencies(
        lambda: ["+7", "+7", "-2", "-7", "-4"]) == 14


def test_main_case(self):
    assert b.getFrequencies(load_main) == 73272
