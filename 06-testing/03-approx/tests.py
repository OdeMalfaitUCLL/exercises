import pytest
from mystatistics import average
from pytest import approx
@pytest.mark.parametrize("ns,expected", [
    ([0.1,0.1,0.1],0.1),
    ([0.2,0.2,0.2],0.2),
    ([0.3,0.3,0.3],0.3),
    ([1,2],1.5),
    ([1,2,3,4,5],3.0)])
def test_average(ns,expected):
    result = average(ns)
    assert result == approx(expected, abs=0.01)

