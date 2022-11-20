from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""
    
def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""
    
def test_mixedcase():
    assert shorten("HellO") == "Hll"
    assert shorten("AeIou") == ""
    assert shorten("TwItTer") == "TwtTr"