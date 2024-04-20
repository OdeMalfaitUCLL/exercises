from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    #mijn testen
    assert overlapping_intervals((0,3), (2,5))
    assert overlapping_intervals((6,10),(8,12))
    assert not overlapping_intervals((1,8),(9,13))
    assert overlapping_intervals((0,0),(0,1))
    assert not overlapping_intervals((8,2),(3,5))