import pytest
from highway_toll import toll_charge


def test_ambulance_is_exempt():
    assert toll_charge("ambulance", 2, False, False) == 0


def test_fire_engine_is_exempt():
    assert toll_charge("fire_engine", 3, True, True) == 0


def test_car_not_exempt():
    assert toll_charge("car", 2, False, False) == 100


def test_truck_not_exempt_peak_fastag():
    assert toll_charge("truck", 4, True, True) == 296.88