import pytest
from highway_toll import pass_advice


def test_pass_advice_buy_pass():
    trips = [(True, False), (False, True), (True, True)]
    assert pass_advice(trips, 2, 250) == "buy_pass"


def test_pass_advice_either():
    trips = [(False, False), (False, False)]
    assert pass_advice(trips, 2, 200) == "either"


def test_pass_advice_pay_per_trip():
    trips = [(False, False)]
    assert pass_advice(trips, 2, 500) == "pay_per_trip"


def test_pass_advice_empty_trips():
    trips = []
    assert pass_advice(trips, 2, 100) == "pay_per_trip"