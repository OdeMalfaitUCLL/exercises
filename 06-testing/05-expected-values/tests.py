import itertools
import pytest
from mergesort import split_in_two,merge_sorted,merge_sort
@pytest.mark.parametrize('ns', [
    list(range(k)) for k in range(101)
    ])
def test_split_in_two(ns):
    left,right = split_in_two(ns)
    assert left + right == ns
    assert abs(len(left) - len(right)) <= 1

@pytest.mark.parametrize('left', [
    [],
    [1],
    [1,2],
    [1,2,2],
    [1,2,3,4],
    [4,10,25],
    [2,5,5,9],
    [1,1,1],
    ])
@pytest.mark.parametrize('right', [
    [],
    [1],
    [1,2],
    [1,2,2],
    [1,2,3,4],
    [4,10,25],
    [2,5,5,9],
    [1,1,1],
    ])
def test_merge_sorted(left,right):
    actual = merge_sorted(left, right)
    expected = sorted(left + right)
    assert expected == actual

@pytest.mark.parametrize('expected,ns', [
    (ns,list(permutation))
    for ns in [[],[1],[1,2], [4,5], [1,4,4,8], [6,7,8,9]]
    for permutation in itertools.permutations(ns)
])
def test_merge_sort(expected,ns):
    assert merge_sort(ns) == expected