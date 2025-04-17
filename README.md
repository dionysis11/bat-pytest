# Bat-Tech Testing Suite

This repository contains tests for Batman's critical technology systems to ensure they function flawlessly in the fight against crime in Gotham City.

## Structure

- `bat_functions.py`: Core Batman technology functions
- `test_bat_functions.py`: Pytest test suite for the bat functions
- `.github/workflows/pytest.yml`: GitHub Actions workflow for continuous integration

## Testing Approach

The test suite demonstrates:

1. **Basic pytest assertions** for simple function testing
2. **Parametrized tests** to verify functions across multiple inputs
3. **Fixtures** for reusable test data
4. **Mocking** to simulate external dependencies without delays
5. **Continuous Integration** via GitHub Actions

## Running the Tests

To run the tests locally:

```bash
pytest
```

For a coverage report:

```bash
pytest --cov=.
```

## CI/CD

Tests automatically run on every push to the repository through GitHub Actions, ensuring that Batman's systems remain reliable at all times.
