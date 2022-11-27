import um

def test_start():
    assert um.count("Um, hello there, um, there") == 2
    assert um.count("There seems to be a bit of a, um, misunderstanding here!") == 1
    
def test_random():
    assert um.count("Um, um, um, um...hi") == 4