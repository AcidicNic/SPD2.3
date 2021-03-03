import pytest
import math
from exercise_2 import get_age_carbon_14_dating, InvalidCarbon14Ratio

def test_get_age_carbon_14_dating_normal():
    assert get_age_carbon_14_dating(0.35) == 8680.35

def test_get_age_carbon_14_dating_int():
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating(1)
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating(0)
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating(-1)
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating(27)

def test_get_age_carbon_14_dating_invalid():
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating(1.1)
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating("0.27")
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating([0, 1, 3, 4])
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating([])
    with pytest.raises(InvalidCarbon14Ratio):
        get_age_carbon_14_dating(None)
