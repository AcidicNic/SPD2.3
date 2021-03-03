from math import log

T_HALF = 5730
DECAY_CONSTANT = -0.693

class InvalidCarbon14Ratio(Exception):
    pass

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 in the
    sample conpared to the amount in living tissue (unitless)."""
    try:
        if 0 < float(carbon_14_ratio) and float(carbon_14_ratio) < 1:
            return round(log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF, 2)
        raise InvalidCarbon14Ratio(
            f"carbon_14_ratio should be a float between 0 and 1, not {carbon_14_ratio}")
    except:
        raise InvalidCarbon14Ratio(
            f"carbon_14_ratio should be a float between 0 and 1, not {carbon_14_ratio}")

# TODO: Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test against
# this special case.
