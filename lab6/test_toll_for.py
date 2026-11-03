import pytest
from highway_toll import toll_for


def test_axles_less_than_2_raises_error():
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(1, False, False)


def test_two_axle_base_toll():
    assert toll_for(2, False, False) == 100


def test_three_axle_base_toll():
    assert toll_for(3, False, False) == 150


def test_four_axle_base_toll():
    assert toll_for(4, False, False) == 250


def test_five_axle_base_toll():
    assert toll_for(5, False, False) == 400


def test_two_axle_peak_no_fastag():
    assert toll_for(2, True, False) == 125


def test_three_axle_peak_no_fastag():
    assert toll_for(3, True, False) == 187.5


def test_four_axle_peak_no_fastag():
    assert toll_for(4, True, False) == 312.5


def test_five_axle_peak_no_fastag():
    assert toll_for(5, True, False) == 500


def test_two_axle_no_peak_fastag():
    assert toll_for(2, False, True) == 90


def test_three_axle_no_peak_fastag():
    assert toll_for(3, False, True) == 142.5


def test_four_axle_no_peak_fastag():
    assert toll_for(4, False, True) == 237.5


def test_five_axle_no_peak_fastag():
    assert toll_for(5, False, True) == 380


def test_two_axle_peak_fastag():
    assert toll_for(2, True, True) == 112.5


def test_three_axle_peak_fastag():
    assert toll_for(3, True, True) == 178.12


def test_four_axle_peak_fastag():
    assert toll_for(4, True, True) == 296.88


def test_five_axle_peak_fastag():
    assert toll_for(5, True, True) == 475