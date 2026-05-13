from plates import is_valid

def test_valid_plates():
    assert is_valid ("CS50") == True
    assert is_valid ("CS") == True


def test_short_or_long():
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False

def test_in_middle():
    assert is_valid("CS05") == False
    assert is_valid ("CS50P") == False


def test_starting_numbers():
    assert is_valid("50CS") == False
    assert is_valid("123ABC") == False

def test_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS-50") == False
    assert is_valid ("CS 50") == False




