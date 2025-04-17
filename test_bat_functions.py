import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle

def test_calculate_bat_power():
    """Test that calculate_bat_power returns the correct power level."""
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(2) == 84
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(100) == 4200

@pytest.mark.parametrize("distance,expected", [
    (0, 100),    # At the source, full strength
    (5, 50),     # 5km away, half strength
    (10, 0),     # 10km away, no signal
    (12, 0),     # Beyond 10km, still no signal (not negative)
])
def test_signal_strength(distance, expected):
    """Test signal_strength with various distances using parametrization."""
    assert signal_strength(distance) == expected

@pytest.fixture
def bat_vehicles():
    """Fixture that provides a dictionary of Batman's vehicles."""
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    """Test that get_bat_vehicle returns correct specs for known vehicles."""
    for vehicle_name, expected_specs in bat_vehicles.items():
        specs = get_bat_vehicle(vehicle_name)
        assert specs == expected_specs
        assert specs['speed'] == expected_specs['speed']
        assert specs['armor'] == expected_specs['armor']

def test_get_bat_vehicle_unknown():
    """Test that get_bat_vehicle raises ValueError for unknown vehicles."""
    with pytest.raises(ValueError) as excinfo:
        get_bat_vehicle("BatSubmarine")
    assert "Unknown vehicle: BatSubmarine" in str(excinfo.value) 