from bank import value

def test_hello():
    assert value ("hello") == 0
    assert value ("Hello") == 0
    assert value ("hello, there") == 0

def test_h_start_but_not_hello():
    assert value ("hi") == 20
    assert value ("hey") == 20
    assert value ("How are you") == 20

def test_other():
    assert value ("good morning") == 100
    assert value ("bye") == 100
    assert value ("cs50") == 100
