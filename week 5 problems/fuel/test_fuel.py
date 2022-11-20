from fuel import get_expression

def test_normal():
    assert get_expression(2, 5) == "40%"
    assert get_expression(3, 10) == "30%"
    
def test_corner():
    assert get_expression(1,1000) == "E"
    assert get_expression(999, 1000) == "F"
    assert get_expression(1,100) == "E"