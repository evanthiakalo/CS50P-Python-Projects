from seasons import get_minutes, format_words
from datetime import date

def test_get_minutes():
    assert get_minutes (date(2022, 1, 1), date(2023, 1, 1)) == 525600
    assert get_minutes (date(2020, 1, 1), date(2021, 1, 1)) == 527040


def test_format_words():
    assert format_words (525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert format_words (1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert format_words (1440) == "One thousand, four hundred forty minutes"

