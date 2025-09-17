

#Step 2: Write pytest Integration Test

from cal import add_then_subtract

def test_add_then_subtract():
    result = add_then_subtract(10, 5, 3)  # (10+5)-3
    assert result == 50  # Expected 12

def test_with_zero():
    result = add_then_subtract(0, 5, 2)   # (0+5)-2
    assert result == 20