import b


def load_main():
    with open("5/input.txt", 'r') as myfile:
        return myfile.read().splitlines()[0]


def test_1():
    assert b.strip_react(lambda: "dabAcCaCBAcCcaDA") == 4


def test_main_case():
    assert b.strip_react(load_main) == 5774
