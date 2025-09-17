
# Step 1: Create Calculator Module

#integration testing

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Integration Function: Combines add + subtract
def add_then_subtract(a, b, c):    #(a+b)-c
    sum_result = add(a, b)
    return subtract(sum_result, c)


# Here:

# First we add a + b

# Then we subtract c from the result