import pytest
from datetime import date, timedelta

from seasons import date_parser, calculate



def test_valid_date():
    d = date_parser("2000-01-01")
    assert isinstance(d, date)


def test_future_date():
    future = (date.today() + timedelta(days=1)).isoformat()
    with pytest.raises(SystemExit):
        date_parser(future)


def test_calculate_today():
    today = date.today()
    assert calculate(today) == "Zero minutes"



