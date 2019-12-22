import pytest
from source2.source3.index4 import index4_rocks
from source2.source3.index5 import allcovered

def test_index4_rocks():
    assert index4_rocks() == False

def test_all():
    assert allcovered() == True