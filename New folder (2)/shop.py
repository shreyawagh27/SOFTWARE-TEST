
#Regression testing

def login(user, password):
    return user == "test" and password == "123" #old

def add_to_cart(price, qty):
    return price * qty 


def apply_coupon(total, discount):
    return total - discount


def checkout(total):
    return f"Order placed! Total = {total}"