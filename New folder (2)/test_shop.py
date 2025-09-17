
from shop import login, add_to_cart, checkout , apply_coupon

def test_login():
    assert login("test", "123") == True  # Old login feature

def test_add_to_cart():
    assert add_to_cart(100, 2) == 200    # Old cart feature
    
def test_apply_coupon():
    assert apply_coupon(500-50)==450  #new feature


def test_checkout():
    assert checkout(200) == "Order placed! Total = 200"  # Old checkout feature
