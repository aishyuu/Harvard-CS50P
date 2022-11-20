from plates import is_valid

def test_fails():
    assert is_valid("AAA22A") == False
    assert is_valid("2222") == False
    assert is_valid("A234") == False
    assert is_valid("AA22.") == False
    
def test_correct():
    assert is_valid("AIB222") == True
    assert is_valid("AU22") == True