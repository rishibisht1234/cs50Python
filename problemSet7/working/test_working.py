import pytest
from working import convert


def test_simple_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_hours_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed_times():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_wraparound():
    # avoids false positives on overnight formatting
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_invalid_format_dash():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")


def test_invalid_24_hour_input():
    with pytest.raises(ValueError):
        convert("09:00 AM to 17:00 PM")
