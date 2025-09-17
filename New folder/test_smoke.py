
# test_smoke.py
from calculator import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(4, 2) == 8



# ✅ If all pass → Build is stable → Proceed to detailed testing
# ❌ If one fails → Stop testing → Fix code first