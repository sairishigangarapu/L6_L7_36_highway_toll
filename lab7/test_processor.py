from hypothesis import given, strategies as st
import pytest
from processor import parse_plate, trip_cost, axle_class


@given(st.text() | st.none())
def test_parse_plate_validates_input(s):
    if isinstance(s, str) and s.count('-') == 3 and all(part for part in s.split('-')):
        try:
            result = parse_plate(s)
            assert isinstance(result, tuple)
            assert len(result) == 3
            assert isinstance(result[0], str)
            assert isinstance(result[1], int)
            assert isinstance(result[2], int)
        except ValueError:
            pass
    else:
        with pytest.raises(ValueError):
            parse_plate(s)


@given(st.text() | st.none())
def test_trip_cost_validates_input(s):
    if isinstance(s, str) and s.strip():
        parts = s.strip().lower().split('x')
        if len(parts) == 2 and parts[0] and parts[1]:
            try:
                count = int(parts[0])
                rate = int(parts[1])
                result = trip_cost(s)
                assert result == count * rate
            except ValueError:
                pass
            else:
                return
    with pytest.raises(ValueError):
        trip_cost(s)


@given(st.text() | st.none())
def test_axle_class_validates_input(s):
    if isinstance(s, str) and s.strip():
        try:
            n = int(s)
            if n >= 0:
                result = axle_class(s)
                assert result in ('car', 'truck', 'heavy')
                if n == 2:
                    assert result == 'car'
                elif n <= 4:
                    assert result == 'truck'
                else:
                    assert result == 'heavy'
                return
        except ValueError:
            pass
    with pytest.raises(ValueError):
        axle_class(s)