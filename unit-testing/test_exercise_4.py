import pytest
import math
from exercise_4 import extract_position

def test_extract_position_normal():
    assert extract_position('|error| blah blah blah.') is None
    assert extract_position('|debug| blah blah blah.') is None
    assert extract_position('|update| blah blah blah x:27.420') == '27.420'

def test_extract_position_edgecases():
    assert extract_position('|update| blah blah blah x:') == ''
    assert extract_position('|update| blah blah blah') is None
    assert extract_position('|something| blah blah blah') is None
    assert extract_position('') is None

    # this is a bug that should be fixed! it raises attributeError
    assert extract_position(['update', 'x:']) is None
