# bat_functions.py

import time

def calculate_bat_power(level: int) -> int:
    """
    Calculates Batman's power level based on a given 'level'.
    For this example, power is level multiplied by 42.
    """
    return level * 42

def signal_strength(distance: float) -> float:
    """
    Calculates the strength of the Bat-Signal based on the distance.
    The strength decreases by 10 units per kilometer, but never goes below 0.
    """
    strength = 100 - (distance * 10)
    return max(0, strength)

def get_bat_vehicle(vehicle_name: str) -> dict:
    """
    Returns specifications of Batman's vehicles.
    Known vehicles: 'Batmobile', 'Batwing', and 'Batcycle'.
    """
    vehicles = {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }
    if vehicle_name in vehicles:
        return vehicles[vehicle_name]
    else:
        raise ValueError(f"Unknown vehicle: {vehicle_name}")

def fetch_joker_info() -> dict:
    """
    Simulates fetching data about Joker's mischief.
    In a real scenario, this might call an external API.
    For this exercise, it waits for 1 second (simulating network latency)
    and returns a dictionary.
    """
    time.sleep(1)
    return {'mischief_level': 100, 'location': 'unknown'}