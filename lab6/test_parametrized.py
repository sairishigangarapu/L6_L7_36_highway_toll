import pytest
from highway_toll import toll_for, toll_charge, pass_advice


class TestTollForParametrized:
    @pytest.mark.parametrize("axles,expected", [
        (2, 100),
        (3, 150),
        (4, 250),
        (5, 400),
        (6, 400),
        (10, 400),
    ])
    def test_base_toll_by_axles(self, axles, expected):
        assert toll_for(axles, False, False) == expected

    @pytest.mark.parametrize("axles,is_peak,has_fastag,expected", [
        (2, False, False, 100.00),
        (2, True, False, 125.00),
        (2, False, True, 90.00),
        (2, True, True, 112.50),
        (3, False, False, 150.00),
        (3, True, False, 187.50),
        (3, False, True, 142.50),
        (3, True, True, 178.12),
        (4, False, False, 250.00),
        (4, True, False, 312.50),
        (4, False, True, 237.50),
        (4, True, True, 296.88),
        (5, False, False, 400.00),
        (5, True, False, 500.00),
        (5, False, True, 380.00),
        (5, True, True, 475.00),
    ])
    def test_toll_combinations(self, axles, is_peak, has_fastag, expected):
        assert toll_for(axles, is_peak, has_fastag) == expected

    @pytest.mark.parametrize("invalid_axles", [0, 1, -1, -5])
    def test_invalid_axles_raises(self, invalid_axles):
        with pytest.raises(ValueError, match="invalid axle count"):
            toll_for(invalid_axles, False, False)


class TestTollChargeParametrized:
    @pytest.mark.parametrize("vehicle", ["ambulance", "fire_engine"])
    def test_exempt_vehicles(self, vehicle):
        assert toll_charge(vehicle, 2, True, True) == 0

    @pytest.mark.parametrize("vehicle,axles,is_peak,has_fastag,expected", [
        ("car", 2, False, False, 100.00),
        ("truck", 3, True, False, 187.50),
        ("bus", 4, False, True, 237.50),
        ("van", 5, True, True, 475.00),
    ])
    def test_non_exempt_vehicles(self, vehicle, axles, is_peak, has_fastag, expected):
        assert toll_charge(vehicle, axles, is_peak, has_fastag) == expected


class TestPassAdviceParametrized:
    @pytest.mark.parametrize("trips,axles,pass_price,expected", [
        ([(True, False), (False, True), (True, True)], 2, 250, "buy_pass"),
        ([(False, False), (False, False)], 2, 200, "either"),
        ([(False, False)], 2, 500, "pay_per_trip"),
        ([], 2, 100, "pay_per_trip"),
        ([(True, True), (True, True)], 4, 600, "pay_per_trip"),
        ([(True, False)], 3, 187.50, "either"),
    ])
    def test_pass_advice_scenarios(self, trips, axles, pass_price, expected):
        assert pass_advice(trips, axles, pass_price) == expected