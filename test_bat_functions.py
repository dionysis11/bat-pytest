import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle, fetch_joker_info

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

def test_fetch_joker_info_without_delay(monkeypatch):
    """Test fetch_joker_info without the 1-second delay using monkeypatch."""
    # Mock the time.sleep function to do nothing
    monkeypatch.setattr('time.sleep', lambda x: None)
    
    # Call the function and verify it returns the expected result
    result = fetch_joker_info()
    assert result == {'mischief_level': 100, 'location': 'unknown'}

def test_fetch_joker_info_mock_return(monkeypatch):
    """Test fetch_joker_info with a custom mocked return value."""
    # Mock data we want to return
    mock_data = {'mischief_level': 0, 'location': 'captured'}
    
    # Create a mock function that returns our mock data
    def mock_fetch_joker_info():
        return mock_data
    
    # Replace the original function with our mock
    monkeypatch.setattr('bat_functions.fetch_joker_info', mock_fetch_joker_info)
    
    # Import the function again to get the mocked version
    import bat_functions
    result = bat_functions.fetch_joker_info()
    
    # Verify the mocked function returns our mock data
    assert result == mock_data
    assert result['mischief_level'] == 0
    assert result['location'] == 'captured' 