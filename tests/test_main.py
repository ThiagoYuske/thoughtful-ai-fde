def add_numbers(a, b):
    """A simple function to add two numbers."""
    return a + b

def test_add_positive_numbers():
    """Tests the addition of two positive numbers."""
    result = add_numbers(2, 3)
    assert result == 5