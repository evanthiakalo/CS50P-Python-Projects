from um import count

def test_single_um():
    assert count ("um") == 1

def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1

def test_multiple_um():
    assert count ("Um, thanks, um...") == 2

def test_no_substrings():
    assert count("yummy album umbrella") == 0

def test_punctuation():
    assert count ("um? um! (um), um.") == 4
