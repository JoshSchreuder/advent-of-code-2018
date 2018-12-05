import a


def load_main():
    with open("5/input.txt", 'r') as myfile:
        return myfile.read().splitlines()[0]


def test_1():
    assert a.react(lambda: "dabAcCaCBAcCcaDA") == 10


def test_2():
    assert a.react(
        lambda: "vVuyYJjUzzZPxXqQpZmgGMvNmMyYTtnVkWwKVvOosmTtMSkDdKFsSpEePhXEexzZtnNTHEeGoOmMRr") == 2


def test_3():
    assert a.react(
        lambda: "kKfQqFmMfiIBbFEesaCcWwLlxUwZEQqePpbNnQqUuVEecCKZzBlLFfbvVQqYcCypPrAXxiHiIGSdDoULlGgTZzttTMm") == 17


def test_main_case():
    assert a.react(load_main) == 10496
