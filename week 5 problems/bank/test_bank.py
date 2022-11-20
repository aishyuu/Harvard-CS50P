from bank import greet_check


def test_0():
    assert greet_check("hello") == "$0"
    assert greet_check("HELLO") == "$0"
    assert greet_check("HeLlO") == "$0"


def test_20():
    assert greet_check("Hi") == "$20"
    assert greet_check("Heyo") == "$20"
    assert greet_check("hoyo") == "$20"


def test_100():
    assert greet_check("Yo") == "$100"
    assert greet_check("Sup") == "$100"