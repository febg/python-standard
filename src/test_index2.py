import pytest
from source2.index2 import fully_covered2
from source2.index3 import uncovered_if3

def test_fully_covered2():
    assert fully_covered2() == True

def test_uncovered_if():
    assert uncovered_if3() == False
