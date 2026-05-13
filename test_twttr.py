from twttr import shorten

def test_lowercase_vowels():
    assert shorten ("twitter") == "twttr"

def test_uppercase_vowels():
    assert shorten ("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten ("TwItTeR") == "TwtTR"

def test_no_vowels():
    assert shorten ("rhythm") == "rhythm"

def test_numbers ():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("hello!") == "hll!"
