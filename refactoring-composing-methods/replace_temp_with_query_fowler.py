# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.

def get_discount_factor(base_price):
    """Returns the discount factor for 'base_price'."""
    if base_price > 1000:
        return 0.95
    return 0.98

def get_price():
    """Returns the total price of discounted items."""
    base_price = quantity * item_price
    return base_price * get_discount_factor(base_price)
