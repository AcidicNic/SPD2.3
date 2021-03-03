import pytest
import math
from exercise_3 import calculate_stat, InvalidGradeList

def test_calculate_stat_normal():
    avg1, sd1 = calculate_stat([10, 12, 23, 23, 16, 23, 21, 16])
    assert math.isclose(avg1, 18.0, abs_tol = 0.01)
    assert math.isclose(sd1, 4.89, abs_tol = 0.01)

    avg2, sd2 = calculate_stat([1])
    assert math.isclose(avg2, 1)
    assert math.isclose(sd2, 0)

def test_calculate_stat_errors():
    with pytest.raises(InvalidGradeList):
        calculate_stat([])
    with pytest.raises(InvalidGradeList):
        calculate_stat("12345")
    with pytest.raises(InvalidGradeList):
        calculate_stat(None)
    with pytest.raises(InvalidGradeList):
        calculate_stat(100)
    with pytest.raises(InvalidGradeList):
        calculate_stat(["1", "2", "3"])
