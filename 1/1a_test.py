import a


def load_main():
    with open("1/input.txt", 'r') as myfile:
        return myfile.readlines()


def test_1():
    assert a.getFrequencies(lambda: ["+1", "-2", "+3", "+1"]) == 3


def test_2():
    assert a.getFrequencies(lambda: ["+1", "+1", "+1"]) == 3


def test_3():
    assert a.getFrequencies(lambda: ["+1", "+1", "-2"]) == 0


def test_4():
    assert a.getFrequencies(lambda: ["-1", "-2", "-3"]) == -6


def test_main_case():
    assert a.getFrequencies(load_main) == 533
