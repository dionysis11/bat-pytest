import pytest
from bat_functions import calculate_bat_power, signal_strength

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