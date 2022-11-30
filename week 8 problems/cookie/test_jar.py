from jar import Jar

def test_init():
    test = Jar()
    assert test.capacity == 12
    assert test.size == 0

def test_str():
    test = Jar()
    assert str(test) == ""
    test.deposit(2)
    assert str(test) == "🍪🍪"
    test.deposit(10)
    assert str(test) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    test.withdraw(5)
    assert str(test) == "🍪🍪🍪🍪🍪🍪🍪"